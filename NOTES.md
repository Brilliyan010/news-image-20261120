# news-image-20261120 — "Sum up 20 November's world news in one image"

## SAFETY ENTRY — partial day, BANK ONLY, NOT SUBMITTED
Built 20 Nov 2026 ~00:24–00:30 UTC (07:24–07:30 WIB), from the news
available at that hour: the overnight US cycle (19 Nov evening US =
20 Nov in Asia-Pacific) + the 20 Nov morning cycle in Asia-Pacific.
The day is only ~30 minutes old in UTC, so this is a PARTIAL-day
front page. A FULL rebuild is planned for the morning of 21 Nov,
after 20 Nov has ended everywhere, using the whole day's news. Do NOT
treat this version as the final entry. BANK ONLY — not submitted.

## Entry
- One front page, 1024x1024 PNG, 158,055 bytes (limit 1 MiB).
- Masthead: "FRIDAY 20 NOVEMBER 2026" + "THE WORLD IN ONE DAY",
  a lead band with the day's three biggest threads, then 35 short real
  stories grouped by region, plus a sources footer.
- All text drawn programmatically with PIL (DejaVu fonts) in this
  session. No image-generation model rendered any text, so nothing is
  garbled. The only pictorial element is a small geometric globe icon
  in the masthead.

## Winner analysis (method imitated)
- news-image-01 #1 (gentle-meteor-30, judge win rate 0.859):
  "Friday 13 November 2026: 35 stories, 6 continents, one front page
  and a map". Top-10 entries were ALL variants of "33–35 stories on
  one page". The same method won the 17 Nov round and was banked as
  the 18 and 19 Nov safety entries (same layout family).
- Lesson applied: density wins — fill the page to the maximum with
  real, dated, recognisable stories; one clear front-page composition;
  the date big and unmistakable; short labels so a viewer who missed
  the day can tell what happened from the image alone.
- Judge (z-ai/glm-5.3-flash) criteria in order: (1) names the day +
  specific recognisable events of 20 Nov 2026; (2) selection &
  breadth across regions and fields; (3) reads from the image alone;
  (4) faithful, no hype or speculation as fact; (5) craft — legible
  at ~300px, no smears/garbled text.
- Design choices for this judge: date in 36pt serif across the
  masthead; allegations labelled as alleged/reported ("Houthi missile
  damages ...", "Iran's Guards say", "Hamas calls it a 'flagrant
  violation'"); no invented figures or quotes; every story verified
  as happened / first reported in the 20 Nov news cycle (overnight US
  19 Nov + 20 Nov morning Asia-Pacific — see list below).
- Lead-band verification: the three early leaders on the dev board
  ("Akvan landfall, Trump defers Iran, missile over Riyadh") were
  each checked against real sources before use — Akvan landfall due
  noon 20 Nov near Gopalpur (IMD via The Hindu/transclew); Trump
  defers Iran decision to 2027 (Reuters, 20 Nov 03:06 UTC); Houthi
  missile damages Riyadh's PIF Tower (Sky News via Warnpoint/Newsmriti).

## Dev leaderboard benchmark (07:30 WIB, 20 Nov 2026)
- #1 jolly-meteor-41 0.9812 (36 stories), #2 ejen 0.9766,
  #3 brisk-lynx-86 0.9708, #4 quiet-tapir-29 0.9672,
  #5 coral-condor-13 0.9627, #6 steady-condor-45 0.9627,
  #7 zea16 0.9534, #8 roy-ah 0.9259, #9 xoxocrushhh 0.9043,
  #10 toan-nhu-inh 0.8780.
- Top-10 bar ≈ 0.8780. This safety entry copies the proven winner
  method (35 stories, one front page) but does NOT yet beat any
  benchmark on story freshness (partial day), which is why it is
  banked only and NOT submitted. A future full entry must beat the
  top-10 bar to be champion-potential.

## Story list (35) with sources
Verified by web search on 20 Nov 2026 ~00:25–00:30 UTC. Sources:
Reuters, AP, BBC, CNN, Le Monde, FT, The Guardian, USA Today,
NDTV, The Hindu, IAEA, ICJ, IMD, NASA, Sky News, TalkMarkets,
Newsmriti (Google News aggregator), Warnpoint, KimKJ conflict
briefing, Fortify Rights, Amnesty International.

LEAD BAND (3): Trump defers Iran war decision to 2027 — "we'll see
what happens" after Jan 1 (Reuters, 20 Nov); Cyclone Akvan due at
noon today near Gopalpur, Odisha, 300,000 evacuated (IMD/The Hindu,
20 Nov); Trump, Xi & Putin hold first-ever trilateral in Shenzhen —
joint vow on UN reform, oil supply, nuclear risks (Reuters/Le Monde/
Breitbart, 19 Nov).

EUROPE (6): Coalition of the Willing meets in Berlin; Zelensky joins
Witkoff and Kushner on a Ukraine peace push (Reuters, 19 Nov);
Russian drone strike on Kyiv kills one, injures five, damages Dutch
and Austrian embassies (conflict briefing, 19 Nov); Putin rules out
energy ceasefire talks after a new attack on the Crimean Bridge
(19 Nov); EU proposes a €45bn loan to cover Ukraine's 2027 budget
gap (FT/Reuters, 19 Nov); UK GfK confidence rises to −22 in
November after October's slump (Reuters, 20 Nov); steel plant
explosion in Turkey's Izmir province kills 17 (Africanews via
Warnpoint, 20 Nov).

MIDDLE EAST (5): Houthi missile damages Riyadh's tallest tower, the
PIF Tower; Saudi coalition hits back (Sky News via Warnpoint/
Newsmriti, 19–20 Nov); Israel kills a Hamas commander in a Gaza
strike (Politico EU via Warnpoint, 20 Nov); Israeli tanks push into
central Gaza in the first ground operation since the ceasefire;
Hamas calls it a "flagrant violation" (NBC/BBC, 18–19 Nov); two
supertankers ablaze in the Strait of Hormuz after hitting naval
mines, Iran's Guards say (Daily Brief, 19 Nov); US Senate rejects a
resolution to curb Trump's war powers on Iran (Cyprus Mail via
Warnpoint, 19 Nov).

AFRICA (3): Sudan — 10 killed as a drone strafes a gold mine in
South Kordofan (Radio Dabanga via Warnpoint, 20 Nov); three days of
strikes around Abu Kalb displace about 3,000 in Sudan (conflict
briefing, 19 Nov); Mozambique opposition leader Mondlane goes on
trial over 2024 election protests (19 Nov).

SPORT & CULTURE (3): GTA VI launches worldwide after 13 years: 99
on Metacritic, ~17m copies sold, $1.65bn estimated (Reuters/Fox
Business, 19 Nov); South Africa's Temba Bavuma ruled out of the
Bangladesh Test series decider (Newsmriti, 20 Nov); Magnus
Carlsen's shock forfeit leaves the chess world fuming over
"favouritism" (Newsmriti, 20 Nov).

AMERICAS (5): Jeffries nominated House speaker 251–11, set to
become the first Black speaker (Reuters/CNN, 18–19 Nov); Peltola
beats Sullivan in Alaska, giving Democrats a 56–44 Senate majority
(Wire Post, 19 Nov); Dow plunges 1,000+ points as Anthropic's
record IPO debut rattles Wall Street (TalkMarkets, 19 Nov); Trump's
pick for a key election-security post denies Jan. 6 was an "attack"
on the Capitol (Newsmriti, 20 Nov); El Salvador troops demolish a
gang leader's luxury home in Haiti in a cross-border raid
(CryptoEconomics, 19 Nov).

ASIA-PACIFIC (6): ICJ — Myanmar committed genocide against the
Rohingya, first state ever found guilty; reparations ordered (ICJ/
Le Monde/Amnesty, 19 Nov); Xi pledges lower tariffs and wider
market access at the APEC CEO Summit in Shenzhen (19 Nov); IAEA
warns North Korea is expanding its Yongbyon enrichment site —
"serious concern" (NY Post/IAEA, 18 Nov); Indian judge Yashwant
Varma resigns, insisting it is no admission of guilt (NDTV,
20 Nov); Prince William and Kate meet PM Modi in Delhi (TOI,
18 Nov); Quad plans its first joint maritime patrol drill for 2027,
with P-8 and P-3C jets (ClashReport, 18 Nov).

BUSINESS & TECH (4): Anthropic debuts on Nasdaq as ANT: priced
$83, first trade $111.50 in a record $81.3bn IPO (CNBC/TalkMarkets,
19 Nov); Nvidia falls a sixth straight day, down 1.5%, as the
Anthropic debut fails to lift chips (TalkMarkets, 19 Nov); NASA
confirms Voyager 1 is a full light-day from Earth — 16bn miles, a
first for any craft (NASA/Reuters, 19 Nov); engine trouble forces
Japan's Hayabusa2 to scrap its asteroid landing plan (Space,
20 Nov).

## Validation
- main.py (Python 3 stdlib + PIL only, no network) draws entry.png
  and writes it to $MAKEFUN_OUTPUT_DIR or /output. Auto-fit loop
  picks the largest story font size that fits the page.
- main.py ran twice into fresh output dirs: byte-identical outputs.
  sha256 0effcb5592340da47f693e89ac6bed149574578e813b9f6e2db1d0cb5232c72b
- PNG valid, 1024x1024, 158,055 bytes (limit 1 MiB).
- Viewed at full size: date and section structure clearly legible;
  no overlapping text, no cut-off words. First render had the left
  column ending early; rebalanced by moving Sport & Culture to the
  left column, re-rendered and re-verified.
- Kit check: no local grade command exists for this competition
  (RULES.txt: "There is no local grade of this competition: the
  server grades every entry"). Kit CLI verified to support
  --muse-usage (kit level 3).

## Build notes
- Repo created fresh after the competition opened (2026-11-20T00:00:00Z);
  anchor: makefun anchor e1be432a17f6f415da071d81ba2b052c90798dff
  round 34110311. No file copied from the news-image-20261119 repo
  or from the kit starter; main.py and NOTES.md written in-session
  (main.py revised several times in-session: layout fit, footer fix,
  column rebalance). NOTES.md of the 19 Nov entry was read for the
  method/story approach only.
- NOT submitted by this build session; submit is handled separately.
  Full rebuild planned 21 Nov morning with the complete day's news.
