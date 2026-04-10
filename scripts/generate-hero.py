#!/usr/bin/env python3
"""Genererer et unikt SVG-hero-bilde basert på nåværende time."""
import random
import datetime
import math

now = datetime.datetime.utcnow()
seed = int(now.strftime('%Y%m%d%H'))
random.seed(seed)

W, H = 1400, 520

palette = ['#00d4ff', '#ff00ea', '#00ff88', '#8844ff', '#ff6644', '#44ddff', '#dd44ff']

def rc():
    return random.choice(palette)

svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid slice">\n'

# Defs
svg += '<defs>\n'
svg += '<linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">'
svg += '<stop offset="0%" stop-color="#0f0c29"/>'
svg += '<stop offset="50%" stop-color="#302b63"/>'
svg += '<stop offset="100%" stop-color="#24243e"/>'
svg += '</linearGradient>\n'

svg += '<filter id="glow"><feGaussianBlur stdDeviation="6" result="b"/>'
svg += '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>\n'

svg += '<filter id="softglow"><feGaussianBlur stdDeviation="20" result="b"/>'
svg += '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>\n'

# Radial gradients for orbs
for i in range(5):
    c = rc()
    svg += f'<radialGradient id="orb{i}"><stop offset="0%" stop-color="{c}" stop-opacity="0.4"/>'
    svg += f'<stop offset="100%" stop-color="{c}" stop-opacity="0"/></radialGradient>\n'

svg += '</defs>\n'

# Background
svg += f'<rect width="{W}" height="{H}" fill="url(#bg)"/>\n'

# Large soft orbs (aurora-like glow)
for i in range(random.randint(3, 5)):
    cx = random.randint(100, W - 100)
    cy = random.randint(50, H - 50)
    r = random.randint(120, 300)
    svg += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#orb{i % 5})" filter="url(#softglow)"/>\n'

# Flowing wave paths
for i in range(random.randint(4, 7)):
    color = rc()
    opacity = random.uniform(0.08, 0.3)
    sw = random.uniform(1, 3)
    y_base = random.randint(40, H - 40)
    amp = random.randint(30, 120)
    freq = random.uniform(0.003, 0.008)
    phase = random.uniform(0, math.pi * 2)

    points = []
    for x in range(0, W + 20, 20):
        y = y_base + math.sin(x * freq + phase) * amp + math.cos(x * freq * 1.7 + phase * 0.5) * amp * 0.4
        points.append((x, y))

    d = f'M {points[0][0]},{points[0][1]:.1f}'
    for j in range(1, len(points)):
        mx = (points[j-1][0] + points[j][0]) / 2
        my = (points[j-1][1] + points[j][1]) / 2
        d += f' Q {points[j-1][0]},{points[j-1][1]:.1f} {mx},{my:.1f}'

    svg += f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw:.1f}" opacity="{opacity:.2f}" filter="url(#glow)"/>\n'

    # Fill wave to bottom for some
    if random.random() > 0.5:
        fill_d = d + f' L {W},{H} L 0,{H} Z'
        svg += f'<path d="{fill_d}" fill="{color}" opacity="{opacity * 0.15:.3f}"/>\n'

# Floating particles
for _ in range(random.randint(20, 40)):
    cx = random.randint(0, W)
    cy = random.randint(0, H)
    r = random.uniform(1, 4)
    color = rc()
    opacity = random.uniform(0.15, 0.6)
    svg += f'<circle cx="{cx}" cy="{cy}" r="{r:.1f}" fill="{color}" opacity="{opacity:.2f}"/>\n'

# Subtle grid/connection lines
for _ in range(random.randint(4, 10)):
    x1, y1 = random.randint(0, W), random.randint(0, H)
    x2, y2 = random.randint(0, W), random.randint(0, H)
    svg += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{rc()}" stroke-width="0.5" opacity="{random.uniform(0.04, 0.12):.2f}"/>\n'

# Small diamond shapes
for _ in range(random.randint(3, 8)):
    cx, cy = random.randint(100, W-100), random.randint(50, H-50)
    s = random.randint(4, 12)
    svg += f'<polygon points="{cx},{cy-s} {cx+s},{cy} {cx},{cy+s} {cx-s},{cy}" fill="none" stroke="{rc()}" stroke-width="1" opacity="{random.uniform(0.1, 0.3):.2f}"/>\n'

# Timestamp
ts = now.strftime('%d.%m.%Y kl. %H:00')
svg += f'<text x="{W-16}" y="{H-12}" text-anchor="end" fill="rgba(255,255,255,0.12)" '
svg += f'font-family="monospace" font-size="10">Generert {ts} UTC</text>\n'

svg += '</svg>'

with open('hero-generated.svg', 'w') as f:
    f.write(svg)

print(f'Generated hero for {ts}')
