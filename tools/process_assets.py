from pathlib import Path
from PIL import Image, ImageEnhance, ImageFilter

src = Path(r"C:\Users\User\Downloads\blue amaya")
dst = Path(r"C:\Users\User\Documents\Codex\2026-09-12\build-a-complete-premium-responsive-website\work\blue-amaya-site\dist\assets")
dst.mkdir(parents=True, exist_ok=True)

mapping = {
    "WhatsApp Image 2026-09-12 at 00.07.48 (1).jpeg": "project-bathroom-tiles.jpg",
    "WhatsApp Image 2026-09-12 at 00.07.48 (2).jpeg": "project-polished-floor.jpg",
    "WhatsApp Image 2026-09-12 at 00.07.48 (3).jpeg": "project-bathroom-renovation.jpg",
    "WhatsApp Image 2026-09-12 at 00.07.48.jpeg": "project-paving.jpg",
    "WhatsApp Image 2026-09-12 at 00.07.49 (1).jpeg": "project-tower-painting.jpg",
    "WhatsApp Image 2026-09-12 at 00.07.49 (2).jpeg": "project-painted-hallway.jpg",
    "WhatsApp Image 2026-09-12 at 00.07.49 (3).jpeg": "project-decorative-ceiling.jpg",
    "WhatsApp Image 2026-09-12 at 00.07.49.jpeg": "project-exterior-tiling.jpg",
    "WhatsApp Image 2026-09-12 at 00.07.50 (1).jpeg": "project-ceiling-installation.jpg",
    "WhatsApp Image 2026-09-12 at 00.07.50 (2).jpeg": "project-cupboards-progress.jpg",
    "WhatsApp Image 2026-09-12 at 00.07.50 (3).jpeg": "project-cupboards-finish.jpg",
    "WhatsApp Image 2026-09-12 at 00.07.50.jpeg": "project-ceiling-works.jpg",
    "WhatsApp Image 2026-09-12 at 00.07.51.jpeg": "project-steel-fixing.jpg",
}

for original, renamed in mapping.items():
    im = Image.open(src / original).convert("RGB")
    im = ImageEnhance.Contrast(im).enhance(1.04)
    im = ImageEnhance.Color(im).enhance(1.02)
    im = im.filter(ImageFilter.UnsharpMask(radius=1.1, percent=45, threshold=4))
    im.save(dst / renamed, quality=90, optimize=True, progressive=True)

# Preserve the exact supplied logo colours while removing only its near-white canvas.
logo = Image.open(src / "WhatsApp Image 2026-09-12 at 00.07.47 (2).jpeg").convert("RGBA")
pixels = logo.load()
for y in range(logo.height):
    for x in range(logo.width):
        r, g, b, _ = pixels[x, y]
        whiteness = min(r, g, b)
        alpha = 0 if whiteness > 246 else (255 if whiteness < 225 else int((246 - whiteness) / 21 * 255))
        pixels[x, y] = (r, g, b, alpha)
bbox = logo.getbbox()
if bbox:
    logo = logo.crop(bbox)
logo.thumbnail((1000, 900), Image.Resampling.LANCZOS)
logo = logo.filter(ImageFilter.UnsharpMask(radius=.8, percent=45, threshold=3))
logo.save(dst / "blue-amaya-logo.png", optimize=True)

symbol = logo.crop((0, 0, logo.width, int(logo.height * .68)))
symbol.thumbnail((192, 192), Image.Resampling.LANCZOS)
favicon = Image.new("RGBA", (192, 192), (0, 0, 0, 0))
favicon.alpha_composite(symbol, ((192 - symbol.width)//2, (192 - symbol.height)//2))
favicon.save(dst / "favicon.png", optimize=True)
