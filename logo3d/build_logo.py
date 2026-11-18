"""
AWC 3D animated logo builder for Blender (bpy).

Builds the Affordable Window Cleaning logo in 3D -- three extruded, rounded
tiles stacked diagonally (A / W / C) with bevelled letters and the
"AFFORDABLE / WINDOW / CLEANING" wordmark -- and animates it:

  frames   1-48   intro : tiles pop in one after another, words wipe in,
                          a shine sweeps across, ends on the resting pose
  frames  49-120  loop  : seamless idle loop (gentle sway + shine sweep)

Run (either works):
  blender -b -P logo3d/build_logo.py -- [options]
  python  logo3d/build_logo.py [options]          # with `pip install bpy`

Options:
  --still           render the resting-pose still (renders/awc-logo-3d.png)
  --anim            render all animation frames and encode WebM videos
  --samples N       Cycles samples (default 24)
  --res WxH         animation resolution (default 960x640)
  --still-res WxH   still resolution (default 1500x1000)
  --save            also save logo3d/awc_logo.blend
With no render option it just builds the scene (and saves if --save).
"""
import math
import os
import shutil
import subprocess
import sys

import bpy  # must come first when using the pip `bpy` module
import bmesh
from mathutils import Matrix, Vector

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "renders")

BLUE = "#1a6fe0"
GREEN = "#6fe36a"

INTRO_END = 48          # last intro frame (resting pose)
LOOP_START = 49
LOOP_LEN = 72           # idle loop length in frames (3 s @ 24 fps)
FPS = 24

FONT_CANDIDATES = [
    "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf",
    "/usr/share/fonts/opentype/inter/Inter-Bold.otf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "C:/Windows/Fonts/arialbd.ttf",
    "/Library/Fonts/Arial Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
]

# ---------------------------------------------------------------- helpers


def parse_args():
    argv = sys.argv
    argv = argv[argv.index("--") + 1:] if "--" in argv else argv[1:]
    opts = {"still": False, "anim": False, "save": False, "samples": 24,
            "res": (960, 640), "still_res": (1500, 1000)}
    i = 0
    while i < len(argv):
        a = argv[i]
        if a in ("--still", "--anim", "--save"):
            opts[a[2:]] = True
        elif a == "--samples":
            i += 1; opts["samples"] = int(argv[i])
        elif a in ("--res", "--still-res"):
            i += 1; w, h = argv[i].lower().split("x")
            opts[a[2:].replace("-", "_")] = (int(w), int(h))
        i += 1
    return opts


def hex_lin(h):
    """sRGB hex -> linear RGBA tuple for Blender."""
    h = h.lstrip("#")
    out = []
    for k in range(3):
        c = int(h[2 * k:2 * k + 2], 16) / 255.0
        out.append(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4)
    return (*out, 1.0)


def px(x, y):
    """Logo reference (images/logo.jpg, 600px) pixel coords -> scene units."""
    return ((x - 298) / 100.0, -(y - 299) / 100.0)


def pick_font():
    for p in FONT_CANDIDATES:
        if os.path.exists(p):
            return bpy.data.fonts.load(p)
    return None  # Blender's built-in font


def reset_scene():
    bpy.ops.wm.read_factory_settings(use_empty=True)


# --------------------------------------------------------------- materials


def shine_group():
    """Node group returning an emission strength for a diagonal shine band.
    Its 'Offset' value node is keyframed to sweep the band across the logo."""
    ng = bpy.data.node_groups.new("AWC_Shine", "ShaderNodeTree")
    ng.interface.new_socket("Strength", in_out="OUTPUT", socket_type="NodeSocketFloat")
    n = ng.nodes
    l = ng.links
    geo = n.new("ShaderNodeNewGeometry")
    sep = n.new("ShaderNodeSeparateXYZ")
    l.new(geo.outputs["Position"], sep.inputs[0])
    diag = n.new("ShaderNodeMath"); diag.operation = "MULTIPLY_ADD"
    l.new(sep.outputs["Y"], diag.inputs[0]); diag.inputs[1].default_value = 0.55
    l.new(sep.outputs["X"], diag.inputs[2])
    off = n.new("ShaderNodeValue"); off.name = "Offset"; off.outputs[0].default_value = -10
    sub = n.new("ShaderNodeMath"); sub.operation = "SUBTRACT"
    l.new(diag.outputs[0], sub.inputs[0]); l.new(off.outputs[0], sub.inputs[1])
    ab = n.new("ShaderNodeMath"); ab.operation = "ABSOLUTE"
    l.new(sub.outputs[0], ab.inputs[0])
    band = n.new("ShaderNodeMapRange")          # |d| 0..0.45 -> 1..0
    band.inputs["From Min"].default_value = 0.0
    band.inputs["From Max"].default_value = 0.45
    band.inputs["To Min"].default_value = 1.0
    band.inputs["To Max"].default_value = 0.0
    band.interpolation_type = "SMOOTHSTEP"
    l.new(ab.outputs[0], band.inputs["Value"])
    gain = n.new("ShaderNodeMath"); gain.operation = "MULTIPLY"
    gain.inputs[1].default_value = 0.55
    l.new(band.outputs[0], gain.inputs[0])
    out = n.new("NodeGroupOutput")
    l.new(gain.outputs[0], out.inputs[0])
    return ng


def make_mat(name, hexcol, shine, rough=0.35, coat=0.25):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    nt = m.node_tree
    bsdf = nt.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = hex_lin(hexcol)
    bsdf.inputs["Roughness"].default_value = rough
    bsdf.inputs["Coat Weight"].default_value = coat
    bsdf.inputs["Coat Roughness"].default_value = 0.15
    bsdf.inputs["Emission Color"].default_value = (1, 1, 1, 1)
    g = nt.nodes.new("ShaderNodeGroup"); g.node_tree = shine
    nt.links.new(g.outputs[0], bsdf.inputs["Emission Strength"])
    return m


# ---------------------------------------------------------------- geometry


def rounded_rect_mesh(name, w, h, r, depth, seg=10):
    """Extruded rounded rectangle centred on origin, back face at z=0."""
    me = bpy.data.meshes.new(name)
    bm = bmesh.new()
    pts = []
    corners = [(w / 2 - r, h / 2 - r, 0), (-w / 2 + r, h / 2 - r, 90),
               (-w / 2 + r, -h / 2 + r, 180), (w / 2 - r, -h / 2 + r, 270)]
    for cx, cy, a0 in corners:
        for s in range(seg + 1):
            a = math.radians(a0 + 90 * s / seg)
            pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    verts = [bm.verts.new((x, y, 0)) for x, y in pts]
    face = bm.faces.new(verts)
    ext = bmesh.ops.extrude_face_region(bm, geom=[face])
    top = [e for e in ext["geom"] if isinstance(e, bmesh.types.BMVert)]
    bmesh.ops.translate(bm, verts=top, vec=(0, 0, depth))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.to_mesh(me); bm.free()
    for p in me.polygons:
        p.use_smooth = True
    ob = bpy.data.objects.new(name, me)
    bpy.context.collection.objects.link(ob)
    bev = ob.modifiers.new("Bevel", "BEVEL")
    bev.width = min(0.045, depth * 0.3); bev.segments = 4
    bev.limit_method = "ANGLE"; bev.angle_limit = math.radians(40)
    bev.harden_normals = True
    ob.modifiers.new("Smooth", "WEIGHTED_NORMAL").keep_sharp = True
    return ob


def text_obj(name, body, font, size, extrude, bevel, align_x="CENTER"):
    cu = bpy.data.curves.new(name, "FONT")
    cu.body = body
    if font:
        cu.font = font
    cu.size = size
    cu.extrude = extrude
    cu.bevel_depth = bevel
    cu.bevel_resolution = 3
    cu.align_x = align_x
    cu.align_y = "CENTER"
    cu.resolution_u = 8
    ob = bpy.data.objects.new(name, cu)
    bpy.context.collection.objects.link(ob)
    return ob


def key(ob, path, frame, value, interp=None):
    setattr(ob, path, value)
    ob.keyframe_insert(path, frame=frame)
    if interp and ob.animation_data and ob.animation_data.action:
        for fc in _fcurves(ob):
            for kp in fc.keyframe_points:
                if int(kp.co.x) == frame:
                    kp.interpolation = interp


def _fcurves(ob):
    act = ob.animation_data.action
    if hasattr(act, "fcurves"):           # Blender < 4.4 style
        return list(act.fcurves)
    out = []                              # layered actions (4.4+/5.x)
    for layer in act.layers:
        for strip in layer.strips:
            for bag in strip.channelbags:
                out.extend(bag.fcurves)
    return out


def look_at(ob, target):
    """Aim -Z at target keeping +Y as screen-up (Track To rolls when the
    camera looks almost straight down the world Z axis)."""
    f = (Vector(target) - ob.location).normalized()
    x = f.cross(Vector((0, 1, 0))).normalized()
    y = x.cross(f)
    ob.rotation_euler = Matrix((x, y, -f)).transposed().to_euler()


# ------------------------------------------------------------------- build


def build():
    reset_scene()
    sc = bpy.context.scene
    font = pick_font()
    shine = shine_group()

    m_blue = make_mat("AWC_Blue", BLUE, shine)
    m_green = make_mat("AWC_Green", GREEN, shine)
    m_white = make_mat("AWC_White", "#ffffff", shine, rough=0.4, coat=0.2)
    m_text = make_mat("AWC_Text", BLUE, shine, rough=0.28)

    rig = bpy.data.objects.new("AWC_Rig", None)
    sc.collection.objects.link(rig)

    # Tiles traced from images/logo.jpg (pixel boxes), later tiles in front.
    tiles = [
        ("A", (48, 133, 203, 250), m_blue, m_green, 0.00),
        ("W", (113, 225, 250, 355), m_green, m_blue, 0.12),
        ("C", (153, 330, 292, 465), m_blue, m_green, 0.24),
    ]
    TILE_D = 0.32
    tile_objs = []
    for i, (ch, (x0, y0, x1, y1), tmat, lmat, z) in enumerate(tiles):
        cx, cy = px((x0 + x1) / 2, (y0 + y1) / 2)
        w, h = (x1 - x0) / 100, (y1 - y0) / 100
        pivot = bpy.data.objects.new(f"Tile_{ch}_pivot", None)
        sc.collection.objects.link(pivot)
        pivot.parent = rig
        pivot.location = (cx, cy, z)
        t = rounded_rect_mesh(f"Tile_{ch}", w, h, 0.11, TILE_D)
        t.data.materials.append(tmat)
        t.parent = pivot
        if i > 0:  # white border plate like the flat logo
            rim = rounded_rect_mesh(f"Rim_{ch}", w + 0.12, h + 0.12, 0.16, TILE_D - 0.06)
            rim.data.materials.append(m_white)
            rim.parent = pivot
            rim.location.z = -0.02
        letter = text_obj(f"Letter_{ch}", ch, font, 1.0, 0.05, 0.022)
        letter.data.materials.append(lmat)
        letter.parent = pivot
        letter.location = (0, -0.02, TILE_D + 0.06)
        bpy.context.view_layer.update()
        s = 0.72 / max(letter.dimensions.y, 1e-3)   # letter cap ~0.72 units
        letter.scale = (s, s, 1)
        tile_objs.append(pivot)

    # Wordmark, left-aligned, fitted to the reference widths.
    words = [
        ("AFFORDABLE", 215, 548, 188),
        ("WINDOW", 275, 512, 290),
        ("CLEANING", 300, 548, 405),
    ]
    word_objs = []
    for body, xl, xr, yc in words:
        ob = text_obj(f"Word_{body}", body, font, 1.0, 0.04, 0.012, align_x="LEFT")
        ob.data.materials.append(m_text)
        ob.parent = rig
        x, y = px(xl, yc)
        ob.location = (x, y, 0.18)
        bpy.context.view_layer.update()
        sx = (xr - xl) / 100 / max(ob.dimensions.x, 1e-3)
        sy = 0.38 / max(ob.dimensions.y, 1e-3)
        ob.scale = (sx, sy, 1)
        ob["final_scale"] = (sx, sy)
        word_objs.append(ob)

    # ----------------------------------------------------------- animation
    sc.render.fps = FPS
    sc.frame_start = 1
    sc.frame_end = LOOP_START + LOOP_LEN - 1

    for i, p in enumerate(tile_objs):
        f0 = 1 + i * 7
        rest_z = p.location.z
        key(p, "scale", f0, (0.001, 0.001, 0.001))
        key(p, "location", f0, (p.location.x, p.location.y, rest_z + 2.5))
        key(p, "rotation_euler", f0, (math.radians(-70), math.radians(25), 0))
        key(p, "scale", f0 + 8, (1.12, 1.12, 1.12))
        key(p, "location", f0 + 8, (p.location.x, p.location.y, rest_z))
        key(p, "rotation_euler", f0 + 8, (math.radians(6), 0, 0))
        key(p, "scale", f0 + 12, (0.96, 0.96, 0.96))
        key(p, "rotation_euler", f0 + 12, (math.radians(-2), 0, 0))
        key(p, "scale", f0 + 16, (1, 1, 1))
        key(p, "rotation_euler", f0 + 16, (0, 0, 0))

    for i, ob in enumerate(word_objs):
        f0 = 12 + i * 7
        sx, sy = ob["final_scale"]
        x, y, z = ob.location
        key(ob, "scale", f0, (0.001, 0.001, 1))
        key(ob, "location", f0, (x - 0.25, y, z))
        key(ob, "scale", f0 + 10, (sx * 1.03, sy, 1))
        key(ob, "location", f0 + 10, (x, y, z))
        key(ob, "scale", f0 + 14, (sx, sy, 1))

    # Idle sway: baked sine so the loop is seamless (frame 49 == frame 121).
    for f in range(1, LOOP_START + LOOP_LEN + 1):
        t = max(f - LOOP_START, 0) / LOOP_LEN * 2 * math.pi
        key(rig, "rotation_euler", f,
            (0.035 * math.sin(t), 0.09 * math.sin(t), 0), interp="LINEAR")

    # Shine sweeps (band travels from off-left to off-right).
    offset_sock = shine.nodes["Offset"].outputs[0]

    def sweep(start, length):
        for k in range(length + 1):
            u = k / length
            u = u * u * (3 - 2 * u)
            offset_sock.default_value = -4.5 + 9.0 * u
            offset_sock.keyframe_insert("default_value", frame=start + k)

    offset_sock.default_value = -6
    offset_sock.keyframe_insert("default_value", frame=1)
    sweep(30, 18)                          # intro: 30-48
    offset_sock.default_value = -6
    offset_sock.keyframe_insert("default_value", frame=49)
    sweep(LOOP_START + 20, 26)             # loop: 69-95
    offset_sock.default_value = -6
    offset_sock.keyframe_insert("default_value", frame=LOOP_START + LOOP_LEN)

    # ------------------------------------------------- camera / lights / world
    target = bpy.data.objects.new("CamTarget", None)
    sc.collection.objects.link(target)
    target.location = (0, 0, 0.15)
    cam_data = bpy.data.cameras.new("Cam")
    cam_data.lens = 85
    cam = bpy.data.objects.new("Camera", cam_data)
    sc.collection.objects.link(cam)
    cam.location = (0.8, -1.6, 16.5)
    look_at(cam, target.location)
    sc.camera = cam

    def area(name, loc, energy, size, color=(1, 1, 1)):
        ld = bpy.data.lights.new(name, "AREA")
        ld.energy = energy; ld.size = size; ld.color = color
        lo = bpy.data.objects.new(name, ld)
        sc.collection.objects.link(lo)
        lo.location = loc
        look_at(lo, target.location)

    area("Key", (-4, 3, 7), 260, 4)
    area("Fill", (5, -4, 5), 90, 6, (0.9, 0.95, 1.0))
    area("Rim", (2, 6, 2), 220, 3)

    world = bpy.data.worlds.new("World")
    world.use_nodes = True
    bg = world.node_tree.nodes["Background"]
    bg.inputs[0].default_value = (0.8, 0.85, 0.9, 1)
    bg.inputs[1].default_value = 0.35
    sc.world = world

    # ---------------------------------------------------------- render setup
    sc.render.engine = "CYCLES"
    sc.cycles.device = "CPU"
    sc.cycles.use_denoising = True
    sc.cycles.max_bounces = 4
    sc.render.film_transparent = True
    sc.render.image_settings.file_format = "PNG"
    sc.render.image_settings.color_mode = "RGBA"
    sc.view_settings.view_transform = "Standard"   # keep brand colours exact
    return sc


# ------------------------------------------------------------------ render


def render_still(sc, samples, res):
    os.makedirs(OUT, exist_ok=True)
    sc.cycles.samples = samples * 2
    sc.render.resolution_x, sc.render.resolution_y = res
    sc.render.resolution_percentage = 100
    sc.frame_set(INTRO_END)
    sc.render.filepath = os.path.join(OUT, "awc-logo-3d.png")
    bpy.ops.render.render(write_still=True)
    print("Still ->", sc.render.filepath)


def render_anim(sc, samples, res):
    frames = os.path.join(OUT, "frames")
    os.makedirs(frames, exist_ok=True)
    sc.cycles.samples = samples
    sc.render.resolution_x, sc.render.resolution_y = res
    sc.render.resolution_percentage = 100
    sc.render.filepath = os.path.join(frames, "f_")
    bpy.ops.render.render(animation=True)
    encode(frames)


def encode(frames):
    ff = shutil.which("ffmpeg")
    if not ff:
        print("ffmpeg not found: PNG frames left in", frames)
        return
    vp9 = ["-c:v", "libvpx-vp9", "-pix_fmt", "yuva420p", "-b:v", "0",
           "-crf", "34", "-row-mt", "1", "-auto-alt-ref", "0", "-an"]
    jobs = [
        ("awc-logo-intro.webm", 1, INTRO_END),
        ("awc-logo-loop.webm", LOOP_START, LOOP_LEN),
    ]
    for name, start, count in jobs:
        subprocess.run([ff, "-y", "-framerate", str(FPS), "-start_number", str(start),
                        "-i", os.path.join(frames, "f_%04d.png"),
                        "-frames:v", str(count), *vp9,
                        os.path.join(OUT, name)], check=True)
    # Opaque preview (white background) for quick viewing / Safari fallback.
    subprocess.run([ff, "-y", "-framerate", str(FPS), "-i",
                    os.path.join(frames, "f_%04d.png"),
                    "-filter_complex",
                    "color=white:s=16x16[bg];[bg][0:v]scale2ref[bg2][fg];"
                    "[bg2][fg]overlay=format=auto:shortest=1,format=yuv420p",
                    "-c:v", "libx264", "-crf", "26", "-preset", "slow",
                    "-movflags", "+faststart", "-an",
                    os.path.join(OUT, "awc-logo-preview.mp4")], check=True)
    print("Videos ->", OUT)


def main():
    o = parse_args()
    sc = build()
    if o["save"]:
        bpy.ops.wm.save_as_mainfile(filepath=os.path.join(HERE, "awc_logo.blend"))
    if o["still"]:
        render_still(sc, o["samples"], o["still_res"])
    if o["anim"]:
        render_anim(sc, o["samples"], o["res"])


if __name__ == "__main__":
    main()
