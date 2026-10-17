"""Create a small Bsmah social preview with its own mark and Arabic headline."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "bsmah-og.webp"
image = Image.new("RGB", (1200, 630), "#142d35")
draw = ImageDraw.Draw(image)

for radius in range(260, 630, 54):
    draw.arc((830 - radius, 305 - radius, 830 + radius, 305 + radius), 180, 356, fill="#28545a", width=2)

# A fingerprint composed of restrained continuous arcs, mirroring the SVG mark.
arcs = [
    (62, 45, 238, 225, 185, 355, "#74c7b8", 11),
    (82, 65, 218, 245, 179, 367, "#e9d6b0", 10),
    (103, 87, 197, 258, 170, 382, "#74c7b8", 9),
    (123, 110, 177, 264, 165, 395, "#e9d6b0", 8),
]
for left, top, right, bottom, start, end, color, width in arcs:
    draw.arc((left, top, right, bottom), start, end, fill=color, width=width)

font_path = Path("C:/Windows/Fonts/tahoma.ttf")
bold_path = Path("C:/Windows/Fonts/tahomabd.ttf")
font = ImageFont.truetype(str(bold_path if bold_path.exists() else font_path), 86)
small = ImageFont.truetype(str(font_path), 36)
eyebrow = ImageFont.truetype(str(font_path), 24)
draw.text((1130, 150), "BSMAH", font=font, fill="#f5f1e8", anchor="ra")
draw.rounded_rectangle((1100, 275, 1130, 282), radius=3, fill="#74c7b8")
draw.text((1130, 350), "Technology Solutions", font=small, fill="#a5e1d5", anchor="ra")
draw.text((1130, 560), "DEVELOPMENT  •  INTEGRATION  •  OPERATIONS  •  EMPID", font=eyebrow, fill="#e9d6b0", anchor="ra")

image.save(OUT, "WEBP", quality=86, method=6)
print(f"Created {OUT} ({OUT.stat().st_size:,} bytes)")
