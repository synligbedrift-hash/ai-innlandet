#!/usr/bin/env python3
"""Genererer et unikt svart/hvitt hero-bilde i avis-stil basert på nåværende time."""
import random
import datetime
import math

now = datetime.datetime.utcnow()
seed = int(now.strftime('%Y%m%d%H'))
random.seed(seed)

W, H = 1400, 480

# Paper tone background, ink foreground
PAPER = '#f7f3e9'
INK = '#1a1a1a'

svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid slice">\n'

# Background
svg += f'<rect width="{W}" height="{H}" fill="{PAPER}"/>\n'

# Halftone dots across the image (newspaper printing feel)
dot_spacing = 14
for y in range(0, H, dot_spacing):
    for x in range(0, W, dot_spacing):
        # Distance from center creates radial gradient feel
        dx = (x - W/2) / (W/2)
        dy = (y - H/2) / (H/2)
        dist = math.sqrt(dx*dx + dy*dy)
        # Some noise
        noise = random.uniform(-0.15, 0.15)
        intensity = max(0, min(1, 1 - dist * 0.8 + noise))
        r = intensity * 3.5
        if r > 0.5:
            svg += f'<circle cx="{x}" cy="{y}" r="{r:.2f}" fill="{INK}" opacity="0.5"/>\n'

# Add abstract mountain/landscape silhouettes (Innlandet skyline)
def draw_ridge(base_y, peak_variance, opacity):
    points = [(0, H)]
    x = 0
    while x < W:
        step = random.randint(60, 140)
        x += step
        y = base_y + random.uniform(-peak_variance, peak_variance)
        points.append((x, y))
    points.append((W, H))
    d = 'M ' + ' L '.join([f'{px:.0f},{py:.0f}' for px, py in points]) + ' Z'
    return f'<path d="{d}" fill="{INK}" opacity="{opacity}"/>\n'

# Background ridges (lighter)
svg += draw_ridge(H * 0.65, 40, 0.12)
svg += draw_ridge(H * 0.72, 50, 0.18)
svg += draw_ridge(H * 0.80, 35, 0.35)
svg += draw_ridge(H * 0.88, 25, 0.85)

# A sun or moon
cx = random.randint(200, W - 200)
cy = random.randint(80, 180)
r = random.randint(50, 90)
svg += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{INK}" stroke-width="2" opacity="0.7"/>\n'
# Inner hatching lines inside the circle
for i in range(random.randint(4, 9)):
    angle = random.uniform(0, math.pi)
    x1 = cx + math.cos(angle) * r * 0.9
    y1 = cy + math.sin(angle) * r * 0.9
    x2 = cx - math.cos(angle) * r * 0.9
    y2 = cy - math.sin(angle) * r * 0.9
    svg += f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{INK}" stroke-width="1" opacity="0.3"/>\n'

# A few birds (small V-shapes)
for _ in range(random.randint(3, 8)):
    bx = random.randint(50, W - 50)
    by = random.randint(40, 200)
    size = random.randint(8, 16)
    svg += f'<path d="M {bx-size},{by} Q {bx-size/2},{by-size/2} {bx},{by} Q {bx+size/2},{by-size/2} {bx+size},{by}" fill="none" stroke="{INK}" stroke-width="1.5" opacity="0.6"/>\n'

# Thin horizontal rules like a newspaper
svg += f'<line x1="0" y1="2" x2="{W}" y2="2" stroke="{INK}" stroke-width="3"/>\n'
svg += f'<line x1="0" y1="10" x2="{W}" y2="10" stroke="{INK}" stroke-width="1"/>\n'
svg += f'<line x1="0" y1="{H-10}" x2="{W}" y2="{H-10}" stroke="{INK}" stroke-width="1"/>\n'
svg += f'<line x1="0" y1="{H-2}" x2="{W}" y2="{H-2}" stroke="{INK}" stroke-width="3"/>\n'

# Timestamp in small uppercase letters (newspaper meta)
ts = now.strftime('%d.%m.%Y · kl. %H:00')
svg += f'<text x="{W/2}" y="{H-20}" text-anchor="middle" fill="{INK}" '
svg += f'font-family="Georgia, serif" font-size="11" font-style="italic" opacity="0.5">'
svg += f'Utgave generert {ts} UTC</text>\n'

svg += '</svg>'

with open('hero-generated.svg', 'w') as f:
    f.write(svg)

print(f'Generated B&W newspaper hero for {ts}')
