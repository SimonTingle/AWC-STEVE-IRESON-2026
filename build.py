import os
OUT = "/home/user/AWC-STEVE-IRESON-2026"
# ---- PLACEHOLDERS: replace when Steve sends details ----
PHONE = "07830 116967"; TEL = "+447830116967"; WA = "447830116967"
EMAIL = "info@example.com"; HOURS = "Mon–Sat: TBC"
FB = "#"; IG = "#"; GB = "#"
GA_ID = "G-XXXXXXXXXX"; FORM_KEY = "YOUR_WEB3FORMS_ACCESS_KEY"
DOMAIN = "https://www.a-w-c.co.uk"

I = {
 "shield": '<path d="M12 2l8 3v6c0 5-3.5 9.5-8 11-4.5-1.5-8-6-8-11V5z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
 "quote": '<path d="M4 4h16v12H8l-4 4z"/><path d="M8 9h8M8 12h5"/>',
 "home": '<path d="M3 11l9-7 9 7v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>',
 "star": '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/>',
 "bolt": '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
 "brick": '<rect x="3" y="4" width="18" height="16" rx="1"/><path d="M3 9h18M3 14h18M9 4v5M15 9v5M9 14v6"/>',
 "drop": '<path d="M12 3s6 7 6 11a6 6 0 0 1-12 0c0-4 6-11 6-11z"/>',
 "pound": '<path d="M16 6a4 4 0 0 0-7 2.5V20M6 13h8M6 20h12"/>',
 "pin": '<path d="M12 21s7-6.5 7-12a7 7 0 0 0-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/>',
 "window": '<rect x="4" y="3" width="16" height="18" rx="1"/><path d="M12 3v18M4 12h16"/>',
 "spray": '<rect x="7" y="8" width="8" height="13" rx="2"/><path d="M9 8V5h4v3M17 4h.01M19 6h.01M17 8h.01M20 3h.01"/>',
 "gutter": '<path d="M3 7h18v3a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M17 12v9"/>',
 "glass": '<path d="M5 3h14l-2 18H7z"/><path d="M8 7l3 3"/>',
 "metal": '<rect x="3" y="6" width="18" height="12" rx="1"/><circle cx="6" cy="9" r=".5"/><circle cx="18" cy="9" r=".5"/><circle cx="6" cy="15" r=".5"/><circle cx="18" cy="15" r=".5"/>',
 "wood": '<path d="M4 5h16v14H4z"/><path d="M4 10c4-2 8 2 16 0M4 15c5-2 9 2 16 0"/>',
 "stone": '<path d="M4 16l3-8 6-3 6 4 1 7-5 4H8z"/>',
 "camera": '<path d="M3 8h4l2-3h6l2 3h4v11H3z"/><circle cx="12" cy="13" r="3.5"/>',
 "leaf": '<path d="M5 19c0-9 6-14 15-14 0 9-5 15-14 15"/><path d="M5 19l8-8"/>',
 "wrench": '<path d="M14 6a4 4 0 0 0 5 5l-9 9-3-3 9-9a4 4 0 0 1-2-2z"/>',
 "sticker": '<path d="M4 4h12l4 4v12H4z"/><path d="M16 4v4h4"/>',
 "alert": '<path d="M12 3l10 18H2z"/><path d="M12 10v5M12 18h.01"/>',
 "coat": '<path d="M4 20V8l8-5 8 5v12z"/><path d="M8 20v-7h8v7"/>',
 "ladder": '<path d="M7 3v18M17 3v18M7 7h10M7 12h10M7 17h10"/>',
 "building": '<rect x="4" y="3" width="16" height="18"/><path d="M8 7h2M14 7h2M8 11h2M14 11h2M8 15h2M14 15h2"/>',
 "shop": '<path d="M3 9l2-5h14l2 5v2a3 3 0 0 1-6 0 3 3 0 0 1-6 0 3 3 0 0 1-6 0zM5 13v8h14v-8"/>',
 "school": '<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c3 2 9 2 12 0v-5"/>',
 "key": '<circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M17 6l3 3"/>',
}
def ic(n): return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{I[n]}</svg>'
WA_SVG = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.4 14.2c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.1-4.6-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.9s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.9 2.1c.1.2.1.4 0 .5l-.3.5-.4.5c-.1.1-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.3 2.4 1.5.3.1.5.1.6-.1l.9-1c.2-.3.4-.2.6-.1l2 1c.3.1.5.2.5.3.1.2.1.7-.1 1.3z"/></svg>'
SOC = {
 "Facebook": (FB, '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M14 8V6c0-.8.2-1.2 1.4-1.2H17V2h-2.6C11.7 2 11 3.6 11 6v2H9v3h2v11h3V11h2.6l.4-3z"/></svg>'),
 "Instagram": (IG, '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".5"/></svg>'),
 "Google Business": (GB, '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M21 12.2c0-.7-.1-1.3-.2-1.9H12v3.6h5.1a4.4 4.4 0 0 1-1.9 2.9v2.4h3.1c1.8-1.7 2.7-4.1 2.7-7zM12 21.5c2.6 0 4.7-.9 6.3-2.3l-3.1-2.4c-.9.6-1.9.9-3.2.9-2.5 0-4.6-1.7-5.3-3.9H3.5v2.5A9.5 9.5 0 0 0 12 21.5zM6.7 13.8a5.7 5.7 0 0 1 0-3.6V7.7H3.5a9.5 9.5 0 0 0 0 8.6zM12 6.3c1.4 0 2.6.5 3.6 1.4l2.7-2.7A9.5 9.5 0 0 0 3.5 7.7l3.2 2.5C7.4 8 9.5 6.3 12 6.3z"/></svg>'),
}
NAV = [("index.html","Home"),("commercial-window-cleaning.html","Commercial Window Cleaning"),("graffiti-removal.html","Graffiti Removal"),("gutter-cleaning.html","Gutter Cleaning & Repair"),("contact.html","Contact")]

def page(fn, title, desc, body, extra_head=""):
    nav = "".join(f'<li><a href="{h}"{" class=active" if h==fn else (" class=hot" if "graffiti" in h else "")}>{t}</a></li>' for h,t in NAV)
    soc = "".join(f'<a href="{u}" aria-label="{n}" rel="noopener">{s}</a>' for n,(u,s) in SOC.items())
    html = f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{DOMAIN}/{'' if fn=='index.html' else fn}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="{DOMAIN}/images/logo.jpg">
<link rel="icon" href="images/logo.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"LocalBusiness","name":"AWC Services","alternateName":"Affordable Window Cleaning","image":"{DOMAIN}/images/logo.jpg","telephone":"{TEL}","email":"{EMAIL}","url":"{DOMAIN}","areaServed":["Sheffield","Rotherham","Chesterfield"],"address":{{"@type":"PostalAddress","addressLocality":"Sheffield","addressCountry":"GB"}}}}</script>
<script defer src="js/parallax.js"></script>
{extra_head}
</head>
<body>
<div class="promo">Graffiti problem? Same-day / next-day removal across Sheffield, Rotherham &amp; Chesterfield — <a href="graffiti-removal.html">get a free quote</a></div>
<header><nav class="nav" aria-label="Main">
<a class="logo" href="index.html"><img src="images/logo.jpg" alt="AWC – Affordable Window Cleaning" width="150" height="150"></a>
<button class="burger" aria-label="Menu" aria-expanded="false" onclick="var m=document.getElementById('menu');m.classList.toggle('open');this.setAttribute('aria-expanded',m.classList.contains('open'))">&#9776;</button>
<ul class="menu" id="menu">{nav}</ul>
</nav></header>
<main>
{body}
</main>
<footer><div class="wrap">
<div class="grid">
<div><h3>AWC Services</h3><p>Affordable window cleaning, graffiti removal and gutter cleaning &amp; repair for homes and businesses across Sheffield, Rotherham &amp; Chesterfield. Local, family-run and fully insured.</p><div class="social">{soc}</div></div>
<div><h3>Services</h3><ul>{"".join(f'<li><a href="{h}">{t}</a></li>' for h,t in NAV[1:4])}</ul></div>
<div><h3>Contact</h3><ul><li><a href="tel:{TEL}">{PHONE}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="https://wa.me/{WA}">WhatsApp us</a></li><li>{HOURS}</li></ul></div>
</div>
<div class="copy">&copy; <span id="yr">2026</span> AWC Services · Sheffield · Rotherham · Chesterfield · <a href="privacy.html">Privacy &amp; Cookies</a></div>
</div></footer>
<a class="wa-float" href="https://wa.me/{WA}" aria-label="WhatsApp AWC">{WA_SVG}</a>
<div class="mobile-bar"><a href="tel:{TEL}">&#9742; Call</a><a href="https://wa.me/{WA}">WhatsApp</a></div>
<div class="cookie" id="cookie"><strong>Cookies</strong><p style="margin:.3em 0">We use Google Analytics cookies to see how our site is used. <a href="privacy.html">More info</a></p><div class="ctas"><button class="btn btn-blue" onclick="ck('y')">Accept</button><button class="btn" style="background:#eef2f8" onclick="ck('n')">Decline</button></div></div>
<script>
document.getElementById('yr').textContent=new Date().getFullYear();
function ga(){{var s=document.createElement('script');s.async=1;s.src='https://www.googletagmanager.com/gtag/js?id={GA_ID}';document.head.appendChild(s);window.dataLayer=window.dataLayer||[];window.gtag=function(){{dataLayer.push(arguments)}};gtag('js',new Date());gtag('config','{GA_ID}');}}
function ck(v){{try{{localStorage.setItem('awc-ck',v)}}catch(e){{}}document.getElementById('cookie').style.display='none';if(v=='y')ga();}}
(function(){{var v=null;try{{v=localStorage.getItem('awc-ck')}}catch(e){{}}if(v=='y')ga();else if(!v)document.getElementById('cookie').style.display='block';}})();
</script>
</body>
</html>
'''
    open(os.path.join(OUT, fn), "w").write(html)

BADGES = f'''<div class="badges"><ul>
<li>{ic("shield")}Fully insured</li><li>{ic("quote")}Free, no-obligation quotes</li><li>{ic("home")}Local &amp; family-run</li><li>{ic("star")}20+ years' experience</li>
</ul></div>'''
def band(h="Ready for a free quote?", p="Tell us what you need and we'll get back to you fast — no obligation, no hidden fees."):
    return f'''<section class="band"><div class="wrap"><h2>{h}</h2><p>{p}</p><div class="ctas" style="justify-content:center"><a class="btn btn-green" href="contact.html">Get a free quote</a><a class="btn btn-line" href="tel:{TEL}">Call {PHONE}</a></div></div></section>'''
def tiles(items, cls="g3"):
    return f'<div class="grid {cls}">' + "".join(f'<div class="tile"><div class="icon">{ic(i)}</div><h3>{h}</h3><p style="margin:0;color:var(--muted)">{p}</p></div>' for i,h,p in items) + '</div>'
def ticks(xs): return '<ul class="ticks">' + "".join(f"<li>{x}</li>" for x in xs) + "</ul>"

# ---------------- HOME ----------------
page("index.html",
 "Affordable Window Cleaning Sheffield | AWC Services – Commercial, Graffiti & Gutters",
 "AWC Services – affordable window cleaning in Sheffield, Rotherham & Chesterfield. Commercial window cleaning, graffiti removal and gutter cleaning & repair. Fully insured, free quotes.",
f'''<section class="hero"><div class="hero-bg" data-parallax><img src="images/commercial-glass-cherrypicker.jpg" alt="" fetchpriority="high"></div><div class="wrap">
<div class="hero-grid"><div>
<span class="tag">Sheffield • Rotherham • Chesterfield</span>
<h1>Affordable Window Cleaning<br>for Homes &amp; Businesses</h1>
<p>Welcome to AWC — your local Sheffield specialists in commercial window cleaning, graffiti removal and gutter cleaning &amp; repair. We live here, we work here, and we take pride in keeping our area looking its best.</p>
<div class="ctas"><a class="btn btn-green" href="contact.html">Get a free quote</a><a class="btn btn-line" href="tel:{TEL}">Call {PHONE}</a></div>
</div>
<div class="logo3d" id="logo3d"><img src="media/awc-logo-3d.png" alt="AWC – Affordable Window Cleaning" width="1500" height="1000" fetchpriority="high"><video id="l3-intro" muted playsinline preload="auto" aria-hidden="true"><source src="media/awc-logo-intro.webm" type="video/webm"></video><video id="l3-loop" muted playsinline loop preload="auto" aria-hidden="true"><source src="media/awc-logo-loop.webm" type="video/webm"></video></div>
</div></div></section>
{BADGES}
<section><div class="wrap split">
<div><h2>Sheffield's trusted window cleaning contractor</h2>
<p class="lead">AWC has become one of Sheffield's leading commercial and high-end residential window cleaning contractors. Our contracts range from small residential blocks to large commercial, high-rise office buildings in Sheffield city centre and the surrounding areas.</p>
<p>With the latest high-level Reach &amp; Wash water-fed pole equipment, fully trained staff, committed management and an impeccable safety record, AWC guarantees a cost-effective solution to any cleaning task.</p>
<p><strong>Call today to arrange a free quotation and on-site survey.</strong></p>
<a class="btn btn-blue" href="commercial-window-cleaning.html">Commercial window cleaning</a></div>
<img src="images/period-house-pole.jpg" alt="AWC cleaning windows of a period brick house with a water-fed pole" loading="lazy">
</div></section>
<section class="soft"><div class="wrap">
<h2>What we do</h2><p class="lead">Reliable, professional exterior cleaning and maintenance across Sheffield, Rotherham &amp; Chesterfield.</p>
<div class="grid g3" style="margin-top:28px">
<div class="card"><img src="images/office-block-pole.jpg" alt="Water-fed pole cleaning office block windows" loading="lazy"><div class="body"><h3>Commercial Window Cleaning</h3><p>Offices, shops, schools and residential blocks — streak-free glass up to 4+ storeys with pure-water Reach &amp; Wash.</p><a class="btn btn-blue" href="commercial-window-cleaning.html">Find out more</a></div></div>
<div class="card feature"><img src="images/graffiti-office-before.jpg" alt="Graffiti tags on an office building before removal" loading="lazy"><div class="body"><span class="ribbon">Fast response</span><h3>Graffiti Removal</h3><p>Spray paint, tags, stickers and fly-posters removed safely from brick, stone, glass, metal and more — same-day / next-day.</p><a class="btn btn-blue" href="graffiti-removal.html">Remove graffiti</a></div></div>
<div class="card"><img src="images/gutter-vac.jpg" alt="SkyVac high-reach gutter vacuum in use" loading="lazy"><div class="body"><h3>Gutter Cleaning &amp; Repairs</h3><p>No ladders needed — SkyVac reaches up to 4 storeys. Plus repairs, replacements and gutter guards.</p><a class="btn btn-blue" href="gutter-cleaning.html">Clear my gutters</a></div></div>
</div></div></section>
<section><div class="wrap">
<h2>Graffiti gone — like it was never there</h2><p class="lead">Graffiti removal is our fastest-growing service. Here's a recent job on a Sheffield office building.</p>
<div class="ba" style="margin-top:24px"><figure><div class="px" data-parallax data-speed="0.05"><img src="images/graffiti-office-before.jpg" alt="Office building covered in graffiti tags" loading="lazy"></div><figcaption>Before</figcaption></figure><figure><div class="px" data-parallax data-speed="0.05"><img src="images/graffiti-office-after.jpg" alt="Same office building after AWC graffiti removal" loading="lazy"></div><figcaption>After</figcaption></figure></div>
<p style="margin-top:20px"><a class="btn btn-blue" href="graffiti-removal.html">See graffiti removal</a></p>
</div></section>
<section class="soft"><div class="wrap"><h2>Why choose AWC?</h2>
{tiles([("home","Local team","We live and work in the area we serve — not a national franchise."),("shield","Fully insured","Full liability insurance, so your property is protected."),("pound","Honest pricing","Clear, upfront quotes before we start. No hidden fees."),("ladder","Safe methods","Water-fed poles and high-reach vacuums mean fewer ladders against your building."),("bolt","Fast response","Quick turnaround, with same-day / next-day graffiti removal available."),("star","20+ years' experience","Trusted by homes, businesses and property managers across South Yorkshire.")])}
</div></section>
{band()}''',
 extra_head='<script defer src="js/logo3d.js"></script>')

# ---------------- COMMERCIAL ----------------
page("commercial-window-cleaning.html",
 "Commercial Window Cleaning Sheffield, Rotherham & Chesterfield | AWC Services",
 "Professional commercial window cleaning in Sheffield, Rotherham & Chesterfield. Offices, shops, schools and residential blocks. Water-fed pole Reach & Wash. Free quotes.",
f'''<div class="page-head"><div class="wrap"><h1>Commercial Window Cleaning</h1><p>Sparkling glass for offices, shops, schools and residential blocks across Sheffield, Rotherham &amp; Chesterfield.</p></div></div>
{BADGES}
<section><div class="wrap split">
<div><h2>First impressions start at the window</h2>
<p class="lead">Clean windows tell customers, staff and visitors that you care. AWC delivers reliable, scheduled commercial window cleaning — from a single shop front to high-rise office buildings in Sheffield city centre.</p>
<p>We use the latest Reach &amp; Wash water-fed pole system with purified water. It leaves glass and frames spotless and streak-free, dries naturally without residue, and lets our team work safely from the ground — reaching up to 4+ storeys without ladders or disruption.</p>
<a class="btn btn-blue" href="contact.html">Book a free site survey</a></div>
<img src="images/office-block-pole.jpg" alt="Water-fed pole cleaning upper floor office windows" loading="lazy">
</div></section>
<section class="soft"><div class="wrap"><h2>Who we clean for</h2>
{tiles([("building","Offices","Multi-storey office blocks and business parks."),("shop","Shops &amp; retail","Shop fronts, signage and high-street units."),("school","Schools &amp; councils","Schools, public buildings and council property."),("key","Housing &amp; landlords","Residential blocks, letting agents and property managers.")],"g4")}
</div></section>
<section><div class="wrap split">
<img src="images/commercial-glass-cherrypicker.jpg" alt="AWC cleaning a large glass building facade" loading="lazy">
<div><h2>What's included</h2>
{ticks(["Windows, frames and sills cleaned","Pure-water system — no streaks, no chemicals","Weekly, fortnightly, monthly or one-off visits","Work scheduled around your opening hours","Fully trained staff and impeccable safety record","Full liability insurance","Clear, fixed quotes — no hidden fees"])}
<p style="margin-top:18px"><strong>Residential too:</strong> we also clean high-end homes and residential properties — just ask.</p>
</div></div></section>
<section class="soft"><div class="wrap"><h2>Also need&hellip;</h2>
<div class="grid g2"><div class="tile"><div class="icon">{ic("spray")}</div><h3>Graffiti removal</h3><p>Tags on your building? We remove them fast without damaging surfaces. <a href="graffiti-removal.html">Learn more</a></p></div>
<div class="tile"><div class="icon">{ic("gutter")}</div><h3>Gutter cleaning</h3><p>Combine with gutter clearing on the same visit. <a href="gutter-cleaning.html">Learn more</a></p></div></div>
</div></section>
{band("Get a free commercial quote","Call to arrange a free quotation and on-site survey — we'll find a cost-effective solution.")}''')

# ---------------- GRAFFITI ----------------
page("graffiti-removal.html",
 "Graffiti Removal Sheffield, Rotherham & Chesterfield | Fast & Safe | AWC Services",
 "Professional graffiti removal in Sheffield, Rotherham & Chesterfield. Same-day / next-day service, all surfaces, eco-friendly methods, anti-graffiti coatings. Fully insured, free quotes.",
f'''<section class="hero" style="min-height:440px"><div class="hero-bg" data-parallax><img src="images/graffiti-pressure-wash.jpg" alt="" fetchpriority="high"></div><div class="wrap">
<span class="tag">Same-day / next-day service</span>
<h1>Professional Graffiti Removal<br>You Can Trust</h1>
<p>Fast, reliable graffiti cleaning across Sheffield, Rotherham &amp; Chesterfield. We restore your property to its original condition — no damage, no mess, no hassle.</p>
<div class="ctas"><a class="btn btn-green" href="contact.html">Get a free quote</a><a class="btn btn-line" href="https://wa.me/{WA}">Send us a photo on WhatsApp</a></div>
</div></section>
{BADGES}
<section><div class="wrap">
<h2>Real results</h2><p class="lead">Whether it's your shop front, wall, fence, garage or a public building — we remove unwanted spray paint, tags, stickers and fly-posters safely and efficiently.</p>
<div class="ba" style="margin-top:24px"><figure><div class="px" data-parallax data-speed="0.05"><img src="images/graffiti-office-before.jpg" alt="Graffiti tags on office cladding and brick" loading="lazy"></div><figcaption>Before</figcaption></figure><figure><div class="px" data-parallax data-speed="0.05"><img src="images/graffiti-office-after.jpg" alt="Office cladding and brick after graffiti removal" loading="lazy"></div><figcaption>After</figcaption></figure></div>
<div class="split" style="margin-top:40px">
<div class="px px-gable" data-parallax data-speed="0.05"><img src="images/graffiti-gable-before-after.jpg" alt="Gable end wall before and after graffiti removal" loading="lazy"></div>
<div><h3>Gable end wall, Sheffield</h3><p>Heavy tagging on brickwork around a billboard, removed completely without damaging the brick or mortar.</p>
<h2 style="margin-top:28px">What we offer</h2>
{ticks(["<strong>Fast response</strong> — same-day / next-day service available","<strong>All surfaces covered</strong> — brick, stone, concrete, glass, metal, wood, uPVC &amp; more","<strong>Safe &amp; effective</strong> — environmentally friendly products, no harsh chemicals that damage your property","<strong>Fully insured</strong> — peace of mind for homes and businesses","<strong>Competitive pricing</strong> — clear, upfront quotes, no hidden fees","<strong>Local team</strong> — we live and work in the area we serve"])}
</div></div></div></section>
<section class="soft"><div class="wrap"><h2>Surfaces we clean</h2>
<div class="grid g4 surfaces">{"".join(f'<div class="tile" style="text-align:center"><div class="icon" style="margin:0 auto 10px">{ic(i)}</div><h3 style="margin:0">{t}</h3></div>' for i,t in [("brick","Brick"),("stone","Stone"),("brick","Concrete"),("glass","Glass"),("metal","Metal &amp; shutters"),("wood","Wood &amp; fences"),("window","uPVC"),("building","Cladding")])}</div>
</div></section>
<section><div class="wrap"><h2>Our graffiti services</h2>
{tiles([("spray","Graffiti &amp; tag removal","Spray paint, marker pen and tags removed from any surface."),("alert","Offensive graffiti — priority","Racist, obscene or offensive graffiti prioritised for urgent removal."),("coat","Anti-graffiti coatings","Protective coating applied after cleaning so future graffiti washes off easily."),("sticker","Fly-poster &amp; sticker removal","Posters, stickers and adhesive residue removed cleanly."),("drop","Chewing gum removal","Gum removed from pavements, entrances and forecourts."),("bolt","Fast quotes","Send a photo on WhatsApp for a quick, free price.")])}
</div></section>
<section class="soft"><div class="wrap split">
<div><h2>Who we help</h2><p class="lead">Shops, offices, schools, landlords, councils, housing associations and homeowners. Graffiti left in place attracts more — removing it quickly is the best deterrent.</p>
<a class="btn btn-blue" href="contact.html">Request removal</a></div>
<img src="images/graffiti-pressure-wash.jpg" alt="Pressure washing graffiti off a brick wall" loading="lazy">
</div></section>
{band("Get rid of graffiti fast","Snap a photo, send it over, and we'll give you a free, no-obligation quote.")}''')

# ---------------- GUTTER ----------------
page("gutter-cleaning.html",
 "Gutter Cleaning & Repair Sheffield, Rotherham & Chesterfield | SkyVac | AWC Services",
 "Gutter cleaning, repairs, replacements and gutter guards in Sheffield, Rotherham & Chesterfield. SkyVac reaches 4 storeys — no ladders. Fully insured, free quotes.",
f'''<div class="page-head"><div class="wrap"><h1>Gutter Cleaning &amp; Repair</h1><p>Keep your gutters clear and protected. Blocked or damaged gutters cause damp, leaks and costly damage — we fix it before it becomes a problem.</p></div></div>
{BADGES}
<section><div class="wrap split">
<div><h2>No ladders needed — SkyVac reaches up to 4 storeys</h2>
<p class="lead">AWC is your local expert for professional gutter cleaning, clearing and repairs across Sheffield, Rotherham &amp; Chesterfield.</p>
<p>Our SkyVac high-reach vacuum system lets us clear gutters safely from the ground — no ladders against your home, no mess left behind. With the built-in camera we can show you before &amp; after photos, so you know the job's done properly.</p>
<a class="btn btn-blue" href="contact.html">Get a free quote</a></div>
<div class="grid g2" style="gap:14px;align-items:center"><img src="images/skyvac-operator.jpg" alt="Operator using a SkyVac high-reach vacuum to clear gutters from the ground" loading="lazy" style="aspect-ratio:3/4;object-fit:cover;width:100%"><img src="images/gutter-vac.jpg" alt="AWC using SkyVac to clean gutters on a block of flats" loading="lazy" style="aspect-ratio:3/4;object-fit:cover;width:100%"></div>
</div></section>
<section class="soft"><div class="wrap"><h2>What we do</h2>
<div class="grid g3">
<div class="tile"><div class="icon">{ic("leaf")}</div><h3>Gutter cleaning</h3>{ticks(["Remove leaves, moss, dirt &amp; debris","Clear downpipes &amp; ensure free flow","Before &amp; after camera photos"])}</div>
<div class="tile"><div class="icon">{ic("wrench")}</div><h3>Repairs &amp; replacement</h3>{ticks(["Leaking joints &amp; brackets fixed","Sagging gutters realigned","Cracked sections replaced","Downpipe repairs &amp; replacements","Fascias &amp; soffits on request"])}</div>
<div class="tile"><div class="icon">{ic("shield")}</div><h3>Gutter guards</h3>{ticks(["Prevent future blockages","Reduce cleaning frequency","Fits most gutter types","Supply &amp; installation"])}</div>
</div></div></section>
<section><div class="wrap"><h2>Why choose AWC for your gutters?</h2>
{tiles([("home","Family-run","A local business — not a national franchise."),("ladder","Safe methods","High-reach vacuum means no ladders against your home."),("shield","Fully insured","Full liability insurance — your property is protected."),("pound","Fixed-price quotes","We quote before we start. No surprises."),("camera","Photo proof","Camera inspection shows you the results."),("drop","Peace of mind","Clean gutters protect your home from water damage.")])}
</div></section>
{band("Book your gutter clean","Free quotes for homes, landlords and commercial buildings.")}''')

# ---------------- CONTACT ----------------
page("contact.html",
 "Contact AWC Services | Free Quotes – Sheffield, Rotherham & Chesterfield",
 "Contact AWC Services for a free quote on window cleaning, graffiti removal or gutter cleaning in Sheffield, Rotherham & Chesterfield. Call, WhatsApp or send photos.",
f'''<div class="page-head"><div class="wrap"><h1>Get a Free Quote</h1><p>Call, WhatsApp or fill in the form — attach a photo of your graffiti or gutters for the fastest price.</p></div></div>
<section><div class="wrap split" style="align-items:start">
<div><h2>Contact us</h2>
<ul class="contact-list">
<li><strong>Phone:</strong> <a href="tel:{TEL}">{PHONE}</a></li>
<li><strong>WhatsApp:</strong> <a href="https://wa.me/{WA}">Message us</a></li>
<li><strong>Email:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a></li>
<li><strong>Hours:</strong> {HOURS}</li>
<li><strong>Areas covered:</strong> Sheffield, Rotherham, Chesterfield &amp; surrounding areas</li>
</ul>
{ticks(["Free, no-obligation quotes","Fully insured","Local &amp; family-run","20+ years' experience"])}
</div>
<form action="https://api.web3forms.com/submit" method="POST" enctype="multipart/form-data">
<input type="hidden" name="access_key" value="{FORM_KEY}">
<input type="hidden" name="subject" value="New quote request – AWC website">
<input type="checkbox" name="botcheck" style="display:none">
<div class="row2"><label>Name<input name="name" required autocomplete="name"></label><label>Phone<input name="phone" type="tel" required autocomplete="tel"></label></div>
<label>Email<input name="email" type="email" required autocomplete="email"></label>
<div class="row2"><label>Service<select name="service" required><option value="">Choose…</option><option>Commercial window cleaning</option><option>Residential window cleaning</option><option>Graffiti removal</option><option>Gutter cleaning</option><option>Gutter repair / guards</option><option>Other</option></select></label>
<label>Postcode<input name="postcode" autocomplete="postal-code"></label></div>
<label>Address (optional)<input name="address" autocomplete="street-address"></label>
<label>Details<textarea name="message" rows="5" placeholder="Tell us about the job…"></textarea></label>
<label>Photo (optional)<input type="file" name="attachment" accept="image/*"></label>
<button class="btn btn-blue" type="submit">Send my quote request</button>
<p style="font-size:.85rem;color:var(--muted);margin:0">By sending, you agree to our <a href="privacy.html">privacy policy</a>.</p>
</form>
</div></section>''')

# ---------------- PRIVACY ----------------
page("privacy.html", "Privacy & Cookies | AWC Services", "Privacy and cookie policy for AWC Services.",
f'''<div class="page-head"><div class="wrap"><h1>Privacy &amp; Cookies</h1></div></div>
<section><div class="wrap" style="max-width:800px">
<h2>Who we are</h2><p>AWC Services provides window cleaning, graffiti removal and gutter services in Sheffield, Rotherham and Chesterfield. Contact: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>What we collect</h2><p>When you use our contact form we collect your name, phone, email, address/postcode, message and any photo you attach. We use this only to respond to your enquiry and provide a quote. Form submissions are delivered to us by email via Web3Forms.</p>
<h2>How long we keep it</h2><p>We keep enquiry details only as long as needed to deal with your request and any resulting work, then delete them.</p>
<h2>Cookies</h2><p>With your consent, we use Google Analytics cookies to understand how visitors use our site. No analytics cookies are set unless you click Accept. You can change your choice by clearing your browser's site data.</p>
<h2>Your rights</h2><p>You can ask to see, correct or delete the personal data we hold about you by emailing us. You can also complain to the Information Commissioner's Office (ico.org.uk).</p>
</div></section>''')
print("ok")
