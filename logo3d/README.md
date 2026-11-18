# AWC 3D logo

A 3D, animated version of `images/logo.jpg`: three extruded, rounded tiles
(blue A, green W, blue C, with white border plates like the flat logo) and the
bevelled "AFFORDABLE / WINDOW / CLEANING" wordmark. Brand colours are
`#1a6fe0` (blue) and `#6fe36a` (green).

## Files

| File | What it is |
| --- | --- |
| `build_logo.py` | Blender script: builds the scene, animation, and renders |
| `renders/awc-logo-3d.png` | Transparent still of the resting pose (1500x1000) |
| `renders/awc-logo-intro.webm` | Intro, plays once (48 frames, 2 s): tiles pop in, words wipe in, shine sweep |
| `renders/awc-logo-loop.webm` | Seamless idle loop (72 frames, 3 s): gentle sway and a shine sweep |
| `renders/awc-logo-preview.mp4` | Intro then loop on white, for quick viewing (no transparency) |

The WebM files are VP9 with an alpha channel (transparent background), 960x640 at 24 fps.

## Re-rendering

You need Blender 4.2+ (tested with the `bpy` 5.3 module) and `ffmpeg` on the PATH.

```bash
# With Blender installed
blender -b -P logo3d/build_logo.py -- --still --anim

# Or without the Blender app
python3 -m venv .venv && .venv/bin/pip install bpy
.venv/bin/python logo3d/build_logo.py --still --anim
```

Options: `--still`, `--anim`, `--samples N` (default 24, Cycles CPU with denoising),
`--res 960x640`, `--still-res 1500x1000`, and `--save` to write `awc_logo.blend`
so you can open the scene in Blender and tweak it. A full render takes a few
minutes on a 4-core CPU.
PNG frames go to `renders/frames/`. They are gitignored and can be deleted after encoding.

The fonts are picked from the first match in `FONT_CANDIDATES` (Inter
ExtraBold, then Liberation Sans Bold, DejaVu Sans Bold, Arial Bold). Edit that
list to use the brand font. The timing constants (`INTRO_END`, `LOOP_LEN`) are at the top of the script,
and the tile boxes (pixel coordinates traced from `images/logo.jpg`) are in
`build()`.

## Embedding in the hero

Copy the renders you want into the site (for example `images/logo3d/`). Then play the
intro once and switch to the idle loop:

```html
<div class="hero-logo3d">
  <video id="awc-logo3d" autoplay muted playsinline
         poster="images/logo3d/awc-logo-3d.png" width="960" height="640"
         aria-label="AWC – Affordable Window Cleaning">
    <source src="images/logo3d/awc-logo-intro.webm" type="video/webm">
  </video>
</div>
<script>
  (function () {
    var v = document.getElementById('awc-logo3d');
    if (!v) return;
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) {
      v.removeAttribute('autoplay'); v.pause(); return;   // poster stays
    }
    v.addEventListener('ended', function () {
      v.src = 'images/logo3d/awc-logo-loop.webm';
      v.loop = true; v.play();
    }, { once: true });
  })();
</script>
<style>
  .hero-logo3d video { width: min(520px, 90vw); height: auto; display: block; }
</style>
```

Notes:

- Safari has limited support for transparent VP9 WebM. Where it can't play
  the video, the `poster` PNG still shows, so the logo is always visible. For
  animated transparency in Safari you need a HEVC-with-alpha `.mov`, which can
  only be exported on macOS (from the PNG frames, using Compressor or
  `avconvert`).
- The poster PNG on its own also works as a static hero logo:
  `<img src="images/logo3d/awc-logo-3d.png" alt="AWC – Affordable Window Cleaning">`.
- If a background is fine (no transparency needed), use `awc-logo-preview.mp4`.
