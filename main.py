#!/usr/bin/env python3
"""news-image-20261120: draw a one-page front page summing up the world
news of Friday 20 November 2026. Pure Python stdlib + PIL, no network,
fully deterministic: the same input always produces the same PNG bytes.
Writes entry.png to $MAKEFUN_OUTPUT_DIR (or /output by default).
"""
import os
import textwrap

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
MARGIN = 26
COL_GAP = 22
INK = (12, 12, 12)
PAPER = (252, 250, 244)
RED = (178, 24, 24)
NAVY = (16, 32, 64)
GREY = (90, 88, 82)
RULE = (150, 148, 140)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
SERIF = os.path.join(FONT_DIR, "DejaVuSerif-Bold.ttf")
SERIF_REG = os.path.join(FONT_DIR, "DejaVuSerif.ttf")
SANS = os.path.join(FONT_DIR, "DejaVuSans.ttf")
SANS_B = os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Wrap text to fit pixel width; returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


LEAD = [
    ("TRUMP DEFERS IRAN WAR DECISION TO 2027",
     "No rush on new strikes, he says: \u201cwe\u2019ll see what happens\u201d after Jan 1."),
    ("CYCLONE AKVAN DUE AT NOON TODAY",
     "Severe storm to hit the Odisha coast near Gopalpur; 300,000 evacuated."),
    ("TRUMP, XI & PUTIN MEET IN SHENZHEN",
     "First-ever trilateral: joint vow on UN reform, oil supply and nuclear risks."),
]

SECTIONS = [
    ("EUROPE", [
        "Coalition of the Willing meets in Berlin; Zelensky joins Witkoff and Kushner on a Ukraine peace push.",
        "Russian drone strike on Kyiv kills one and injures five; Dutch and Austrian embassies damaged.",
        "Putin rules out energy ceasefire talks after a new attack on the Crimean Bridge.",
        "EU proposes a \u20ac45bn loan to cover Ukraine\u2019s 2027 budget gap, repaid from Russian assets.",
        "UK shoppers a little brighter: GfK confidence rises to \u221222 in November after October\u2019s slump.",
        "Steel plant explosion in Turkey\u2019s Izmir province kills 17.",
    ]),
    ("MIDDLE EAST", [
        "Houthi missile damages Riyadh\u2019s tallest tower, the PIF Tower; Saudi coalition hits back.",
        "Israel kills a Hamas commander in a Gaza strike as the ceasefire strains.",
        "Israeli tanks push into central Gaza in the first ground operation since the ceasefire; Hamas calls it a \u201cflagrant violation\u201d.",
        "Two supertankers ablaze in the Strait of Hormuz after hitting naval mines, Iran\u2019s Guards say.",
        "US Senate rejects a resolution to curb Trump\u2019s war powers on Iran.",
    ]),
    ("AFRICA", [
        "Sudan: 10 killed as a drone strafes a gold mine in South Kordofan.",
        "Three days of strikes around Abu Kalb displace about 3,000 people in Sudan.",
        "Mozambique opposition leader Mondlane goes on trial over 2024 election protests.",
    ]),
    ("SPORT & CULTURE", [
        "GTA VI launches worldwide after 13 years: 99 on Metacritic, ~17m copies sold, $1.65bn estimated.",
        "South Africa\u2019s Temba Bavuma ruled out of the Bangladesh Test series decider.",
        "Magnus Carlsen\u2019s shock forfeit leaves the chess world fuming over \u201cfavouritism\u201d.",
    ]),
    ("AMERICAS", [
        "Jeffries nominated House speaker 251\u201311, set to become the first Black speaker.",
        "Peltola beats Sullivan in Alaska, giving Democrats a 56\u201344 Senate majority.",
        "Dow plunges 1,000+ points as Anthropic\u2019s record IPO debut rattles Wall Street.",
        "Trump\u2019s pick for a key election-security post denies Jan. 6 was an \u201cattack\u201d on the Capitol.",
        "El Salvador troops demolish a gang leader\u2019s luxury home in Haiti in a cross-border raid.",
    ]),
    ("ASIA-PACIFIC", [
        "ICJ: Myanmar committed genocide against the Rohingya \u2014 first state ever found guilty; reparations ordered.",
        "Xi pledges lower tariffs and wider market access at the APEC CEO Summit in Shenzhen.",
        "IAEA warns North Korea is expanding its Yongbyon enrichment site \u2014 \u201cserious concern\u201d.",
        "Indian judge Yashwant Varma resigns, insisting it is no admission of guilt.",
        "Prince William and Kate meet PM Modi in Delhi on a royal visit.",
        "Quad plans its first joint maritime patrol drill for 2027, with P-8 and P-3C jets.",
    ]),
    ("BUSINESS & TECH", [
        "Anthropic debuts on Nasdaq as ANT: priced $83, first trade $111.50 in a record $81.3bn IPO.",
        "Nvidia falls a sixth straight day, down 1.5%, as the Anthropic debut fails to lift chips.",
        "NASA confirms Voyager 1 is a full light-day from Earth \u2014 16bn miles, a first for any craft.",
        "Engine trouble forces Japan\u2019s Hayabusa2 to scrap its asteroid landing plan.",
    ]),
]

FOOTER = ("Sources: Reuters \u00b7 AP \u00b7 BBC \u00b7 CNN \u00b7 Le Monde \u00b7 FT \u00b7 Guardian \u00b7 "
          "NDTV \u00b7 The Hindu \u00b7 IAEA \u00b7 ICJ \u00b7 IMD \u00b7 NASA \u00b7 Sky News \u2014 "
          "35 stories, partial day to ~00:30 UTC, 20 Nov 2026")


def draw_globe(draw, cx, cy, r):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=NAVY, width=3)
    draw.ellipse([cx - r * 0.45, cy - r, cx + r * 0.45, cy + r],
                 outline=NAVY, width=2)
    draw.line([cx - r, cy, cx + r, cy], fill=NAVY, width=2)
    draw.arc([cx - r, cy - r * 0.55, cx + r, cy + r * 0.55],
             0, 360, fill=NAVY, width=2)


def build(story_size):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    y = 18
    # ---- masthead ----
    draw_globe(d, MARGIN + 34, 52, 30)
    f_small = font(SANS_B, 15)
    d.text((MARGIN + 76, 26), "THE WORLD IN ONE DAY", font=f_small, fill=RED)
    f_date = font(SERIF, 36)
    d.text((MARGIN + 76, 46), "FRIDAY 20 NOVEMBER 2026", font=f_date, fill=INK)
    d.text((W - MARGIN - 108, 30), "35 STORIES", font=f_small, fill=GREY)
    d.text((W - MARGIN - 108, 50), "6 REGIONS", font=f_small, fill=GREY)
    y = 96
    d.line([MARGIN, y, W - MARGIN, y], fill=INK, width=3)
    y += 10
    # ---- lead band ----
    band_h = 120
    d.rectangle([MARGIN, y, W - MARGIN, y + band_h], fill=NAVY)
    d.text((MARGIN + 12, y + 8), "THE LEAD", font=font(SANS_B, 13), fill=(255, 205, 80))
    col_w = (W - 2 * MARGIN - 24) // 3
    f_lead_h = font(SANS_B, 15)
    f_lead_b = font(SANS, 13)
    for i, (head, body) in enumerate(LEAD):
        x = MARGIN + 12 + i * (col_w + 12)
        lines = wrap(d, head, f_lead_h, col_w - 8)
        ly = y + 30
        for ln in lines:
            d.text((x, ly), ln, font=f_lead_h, fill=(255, 255, 255))
            ly += 19
        for ln in wrap(d, body, f_lead_b, col_w - 8):
            d.text((x, ly), ln, font=f_lead_b, fill=(210, 220, 235))
            ly += 17
    y += band_h + 14
    # ---- body, two columns ----
    body_top = y
    body_bottom = H - 30
    avail = body_bottom - body_top
    col_w = (W - 2 * MARGIN - COL_GAP) // 2
    left = SECTIONS[:4]
    right = SECTIONS[4:]
    f_head = font(SANS_B, 14)
    f_story = font(SANS, story_size)
    lh = story_size + 3
    gap = 5
    sec_gap = 10

    def column_height(sections):
        total = 0
        for title, stories in sections:
            total += 20 + sec_gap  # header + rule + gap
            for s in stories:
                total += len(wrap(d, s, f_story, col_w - 16)) * lh + gap
        return total - gap

    def draw_column(sections, x0):
        cy = body_top
        for title, stories in sections:
            d.text((x0, cy), title, font=f_head, fill=RED)
            d.line([x0, cy + 18, x0 + col_w, cy + 18], fill=RULE, width=1)
            cy += 24
            for s in stories:
                lines = wrap(d, s, f_story, col_w - 16)
                d.text((x0, cy), "\u2022", font=f_story, fill=RED)
                for ln in lines:
                    d.text((x0 + 14, cy), ln, font=f_story, fill=INK)
                    cy += lh
                cy += gap
            cy += sec_gap - gap
        return cy

    need = max(column_height(left), column_height(right))
    if need > avail:
        return None
    draw_column(left, MARGIN)
    draw_column(right, MARGIN + col_w + COL_GAP)
    # ---- footer ----
    d.line([MARGIN, H - 30, W - MARGIN, H - 30], fill=RULE, width=1)
    f_foot = font(SANS, 10)
    fy = H - 26
    for ln in wrap(d, FOOTER, f_foot, W - 2 * MARGIN):
        d.text((MARGIN, fy), ln, font=f_foot, fill=GREY)
        fy += 13
    return img


def main():
    img = None
    for size in (14, 13, 12):
        img = build(size)
        if img is not None:
            break
    if img is None:
        raise SystemExit("layout does not fit at smallest font size")
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(outdir, exist_ok=True)
    except OSError:
        outdir = "out"
        os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.png")
    img.save(path, format="PNG", optimize=True)
    print("wrote", path)


if __name__ == "__main__":
    main()
