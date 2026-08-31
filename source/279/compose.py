# -*- coding: utf-8 -*-
"""Compose couple BEHIND the text overlay. Usage: py compose2.py <scale> <xoff> <ytop> <label> [grid]"""
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageOps, ImageFilter

DL = r"C:\Users\Anima\Downloads"
OUT = r"C:\Users\Anima\AppData\Local\Temp\claude\c--Users-Anima-projects-video-editor-social-media-ai\e9c3e137-0ca8-4d8d-86fa-6d672106352f\scratchpad\casal"

scale = float(sys.argv[1]); xoff = int(sys.argv[2]); ytop = int(sys.argv[3])
label = sys.argv[4]; grid = len(sys.argv) > 5 and sys.argv[5] == "grid"

orig = Image.open(DL + r"\Template 2.png").convert("RGB")
O = np.asarray(orig).astype(np.uint8)

# ---- clean base (remove old couple, keep green) ----
arr = O.copy()
R, Gc, Bc = arr[..., 0].astype(int), arr[..., 1].astype(int), arr[..., 2].astype(int)
green = (Gc > 110) & (Gc > R + 35) & (Gc > Bc + 35)
Ys, Xs = np.mgrid[0:1080, 0:1920]
regA = (Xs < 592)
regB = (Xs >= 592) & (Xs < 860) & (Ys >= 460) & (Ys < 575)
regC = (Xs >= 592) & (Xs < 860) & (Ys >= 693) & (Ys < 1012)
clean = (regA | regB | regC) & (~green)
arr[clean] = np.array([11, 11, 11], np.uint8)
base = Image.fromarray(arr)

# ---- couple grayscale ----
cut = Image.open(DL + r"\Casak_thumb.png").convert("RGBA")
alpha = cut.getchannel("A")
gray = ImageOps.grayscale(cut.convert("RGB"))
couple = Image.merge("RGBA", (gray, gray, gray, alpha))
w, h = int(round(couple.width * scale)), int(round(couple.height * scale))
couple = couple.resize((w, h), Image.LANCZOS)
px, py = xoff, ytop - int(round(32 * scale))
base.paste(couple, (px, py), couple)

# ---- foreground text/graphics overlay (title, subtitle, badge, logo) ----
# boxes contain NO couple in the original, so key-out near-black to keep only graphics
boxes = [
    (585, 290, 1460, 485),   # title
    (600, 565, 1275, 705),   # subtitle
    (850, 100, 1115, 300),   # logo
    (852, 782, 1170, 852),   # badge
]
lum = (0.299 * O[..., 0] + 0.587 * O[..., 1] + 0.114 * O[..., 2])
grn = (O[..., 1].astype(int) - np.maximum(O[..., 0], O[..., 2]).astype(int))
keep = np.maximum(lum, np.clip(grn, 0, 255))
a = np.clip((keep - 42) / 45.0, 0, 1)  # 0 for black bg, 1 for text/green
boxmask = np.zeros((1080, 1920), bool)
for (x0, y0, x1, y1) in boxes:
    boxmask[y0:y1, x0:x1] = True
a = a * boxmask
ov = np.dstack([O.astype(np.uint8), (a * 255).astype(np.uint8)])
overlay = Image.fromarray(ov, "RGBA")
# slight smooth on alpha to avoid hard edges
al = overlay.getchannel("A").filter(ImageFilter.GaussianBlur(0.4))
overlay.putalpha(al)
base.paste(overlay, (0, 0), overlay)

base.save(OUT + ("\\v_%s.png" % label))
if grid:
    gp = base.copy(); d = ImageDraw.Draw(gp)
    for x in range(0, 1920, 100):
        d.line([(x, 0), (x, 1080)], fill=(255, 0, 0)); d.text((x + 2, 2), str(x), fill=(255, 255, 0))
    for y in range(0, 1080, 100):
        d.line([(0, y), (1920, y)], fill=(255, 0, 0)); d.text((2, y + 2), str(y), fill=(255, 255, 0))
    gp.save(OUT + ("\\vgrid_%s.png" % label))
print("saved v_%s  scale=%.3f xoff=%d ytop=%d couple=(%d,%d)" % (label, scale, xoff, ytop, w, h))
