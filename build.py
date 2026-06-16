#!/usr/bin/env python3
"""Build Karnov (KRN) — Data East's 1987 arcade / 1988 NES fire-breathing-strongman
platformer as a UD0 game-world, themed to the source: a Babylonian-desert ember
title card (SVG of Karnov breathing fire), 8-bit/CRT styling, hobby domain.
Genesis, the Treasure-of-Babylon quest, and the .dlw birth. Render-not-invent;
the arcade-Wizard→NES-dragon boss swap and the Street-Fighter-Ryu timeline flagged.
Karnov is © Data East / G-Mode; a fan tribute."""
import os, html, base64, json, io, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

REC = {
 "name": "KARNOV", "axiom": "KRN",
 "position": "Karnov · Data East · arcade 1987 / NES 1988 (カルノフ) — the fire-breathing strongman and the Treasure of Babylon",
 "origin": "an Arabian-Babylonian fantasy world a circus strongman crosses, breathing fire, to recover the lost treasure",
 "mechanism": "Crystallized from Karnov (Data East): the 1987 arcade original and the 1987 Famicom / 1988 NES port.",
 "crystallization": "A bald, mustachioed ex-circus strongman who fights with his breath of fire alone, climbing nine stages of a Near-Eastern fantasy after the Lost Treasure of Babylon — and at the end a wizard, or, on the NES, a three-headed dragon.",
 "nature": "Karnov — Data East's side-scrolling action-platformer; a fire-breathing strongman, a row of collectible power-ups, and a quest for the Treasure of Babylon. The hero who became Data East's mascot.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "Karnov; Jinborov Karnovski; the breath of fire; the power-up row; the Treasure of Babylon; the dragon Ryu; the Wizard",
 "witness": "A villain-shaped hero who outlived his own game: the bald fire-breather became Data East's recurring face, a boss and a fighter in games long after this one.",
 "role": "the strongman game-world",
 "seal": "Throw fire across the Babylonian night after a treasure — and meet, at the end, a boss the cartridge swapped from the cabinet's.",
 "source": "Karnov, catalogued by ROOT0",
}

NATURES = {
 "natural":   ("#d8a850", "flesh and the desert — the mortal strongman, the fantasy world, the icon he became"),
 "ethereal":  ("#9a7cff", "of sorcery and the beast — the wizard, the three-headed dragon, the swapped ending"),
 "spiritual": ("#f0801a", "of the breath and the quest — the fire he throws, the treasure he chases"),
 "electrical":("#3a9bd5", "of the wire and the machine — the cartridge's own system: the stock-and-spend power-up row"),
}

TITLE_SVG = r'''<svg viewBox="0 0 680 400" role="img" aria-label="Karnov title card" preserveAspectRatio="xMidYMid meet" style="width:100%;height:auto;display:block">
<defs><linearGradient id="krndusk" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#16213f"/><stop offset="0.6" stop-color="#3a2238"/><stop offset="1" stop-color="#2a181c"/></linearGradient>
<radialGradient id="krnglow" cx="0.5" cy="0.5" r="0.5">
<stop offset="0" stop-color="#f0801a" stop-opacity="0.45"/><stop offset="1" stop-color="#f0801a" stop-opacity="0"/></radialGradient></defs>
<rect x="0" y="0" width="680" height="400" fill="#120a0e"/>
<rect x="8" y="8" width="664" height="384" fill="url(#krndusk)" stroke="#5a3a20" stroke-width="2"/>
<rect x="8" y="300" width="664" height="92" fill="#15090b"/>
<g fill="#e8d8a0"><circle cx="80" cy="50" r="1.5"/><circle cx="160" cy="40" r="1.2"/><circle cx="300" cy="36" r="1.3"/><circle cx="470" cy="44" r="1.2"/><circle cx="560" cy="120" r="1.3"/><circle cx="120" cy="100" r="1.1"/><circle cx="620" cy="60" r="1.4"/></g>
<path d="M588 44 A30 30 0 1 0 588 104 A24 24 0 1 1 588 44 Z" fill="#e9dca6"/>
<g fill="#1d2238" stroke="#3a4360" stroke-width="1"><rect x="430" y="250" width="160" height="42"/><rect x="446" y="222" width="128" height="30"/><rect x="462" y="196" width="96" height="28"/><rect x="478" y="174" width="64" height="24"/></g>
<rect x="503" y="160" width="14" height="16" fill="#d8a850"/>
<path d="M8 292 Q160 264 320 290 Q480 270 672 292 L672 300 L8 300 Z" fill="#241318"/>
<g fill="#11111c" opacity="0.92"><path d="M86 96 C 110 84 140 92 150 84 C 138 100 120 102 108 100 C 124 110 140 108 152 102 C 140 118 110 116 92 108 C 104 100 92 100 86 96 Z"/><circle cx="150" cy="86" r="5"/><circle cx="152" cy="102" r="5"/><circle cx="142" cy="118" r="4.5"/></g>
<ellipse cx="320" cy="170" rx="190" ry="80" fill="url(#krnglow)"/>
<g>
<rect x="150" y="232" width="52" height="62" rx="6" fill="#c0302a" stroke="#7a1c18" stroke-width="2"/>
<rect x="150" y="228" width="52" height="12" fill="#d8a850"/>
<rect x="156" y="290" width="16" height="12" fill="#2a1a14"/><rect x="180" y="290" width="16" height="12" fill="#2a1a14"/>
<ellipse cx="176" cy="206" rx="40" ry="34" fill="#cf9a6a" stroke="#7a4a28" stroke-width="2"/>
<ellipse cx="142" cy="214" rx="13" ry="26" fill="#cf9a6a" stroke="#7a4a28" stroke-width="2"/>
<circle cx="183" cy="152" r="25" fill="#cf9a6a" stroke="#7a4a28" stroke-width="2"/>
<path d="M178 142 L196 138 M170 144 L160 142" stroke="#3a2412" stroke-width="2.5" stroke-linecap="round"/>
<circle cx="180" cy="150" r="2.2" fill="#1a0f08"/><circle cx="194" cy="150" r="2.2" fill="#1a0f08"/>
<path d="M196 162 Q186 176 176 164 Q186 172 196 162 Q206 176 214 162 Q206 172 196 162 Z" fill="#3a2412"/></g>
<path d="M206 160 C 270 120 360 126 432 154 C 360 184 270 200 206 166 Z" fill="#d8341a"/>
<path d="M214 160 C 272 132 348 138 404 156 C 348 176 272 188 214 165 Z" fill="#f0801a"/>
<path d="M222 160 C 270 144 330 148 372 157 C 330 168 270 176 222 162 Z" fill="#ffd24a"/>
<path d="M432 154 l16 -10 l-8 12 l14 -2 l-12 10 Z" fill="#d8341a"/>
<text x="340" y="356" text-anchor="middle" font-family="'Arial Black',Impact,sans-serif" font-weight="900" font-size="50" letter-spacing="8" fill="#f0801a" stroke="#5a1c0a" stroke-width="1.5">KARNOV</text>
<text x="340" y="384" text-anchor="middle" font-family="monospace" font-size="9.5" letter-spacing="2" fill="#b08850">DATA EAST · NES · 1988 · カルノフ · THE TREASURE OF BABYLON</text>
</svg>'''

GENESIS = [
 ("Data East's Strongman", "arcade · 1987",
  "Data East built and published Karnov (カルノフ) — January 1987 in Japan, March in North America — a 9-stage side-scrolling action-platformer. The hero was modeled on a Data East director, Koji Jinbo (credited in the staff roll as 'JIMBOLOHU')."),
 ("Home, Twice", "Famicom 1987 / NES 1988",
  "Ported to the Famicom on Dec 18 1987 and the NES in January 1988 (SAS Sakata handled the programming). The console version gave Karnov 2 hits before death, redesigned stages 4 and 8, swapped some items — and changed the final boss."),
 ("The Boss Swap", "Wizard → Dragon",
  "In the arcade the final boss is THE WIZARD. On the NES it was replaced with a giant three-headed dragon named Ryu. Honest note: 竜 just means 'dragon,' and Street Fighter's Ryu (Aug 1987) actually predates this one — the shared name is coincidence."),
]

ARC = [
 ("The Lost Treasure", "the quest",
  "Karnov — Jinborov Karnovski, an ex-circus strongman and fire-breather — sets out across an Arabian-Babylonian fantasy world to recover the Lost Treasure of Babylon."),
 ("Fire and Power-Ups", "the climb",
  "Nine stages, fought with his breath of FIRE (upgradeable to double and then triple) and a row of collectible power-ups — boots, wings, bombs, the clapper, the shield — picked up and stocked along the way."),
 ("The Boss at the End", "the finale",
  "At the last stage waits the boss — the Wizard in the arcade, the three-headed dragon Ryu on the NES — and the treasure beyond it."),
]

IDEAS = [
 ("The Power-Up Row", "stock and spend", [
   "The signature look: a row of items across the top of the screen — collect them, stock them, deploy them.",
   "Boots double your jump, wings carry you through stage 8, the clapper clears the screen, the shield eats five hits." ]),
 ("Breath of Fire", "the strongman's weapon", [
   "No sword, no gun — Karnov spits fire, and the Super Fireball upgrades it to double then triple.",
   "A bald, bare-chested circus strongman as an action hero: pure Data East." ]),
 ("Karnov Became the Mascot", "bigger than his game", [
   "The fire-breather outlived his own game to become Data East's recurring face.",
   "A boss in Bad Dudes (1988), the final boss of Fighter's History (1993), playable in its 1994 sequel." ]),
]

SECTIONS = [
 ("The Releases", "arcade to NES", [
   ("カルノフ · Karnov", "1987 · arcade (Data East)", "the original — January JP, March NA"),
   ("Karnov", "1987 · Famicom / 1988 · NES", "the home port (SAS Sakata programmed) — 2 hits, redesigned stages, the dragon boss"),
   ("the differences", "arcade vs NES", "NES: a Spike Bomb &amp; a Shield item, redesigned stages 4 &amp; 8, and the Wizard swapped for a three-headed dragon"),
 ]),
 ("The Makers", "Data East", [
   ("Data East", "developer / publisher", "arcade and console"),
   ("SAS Sakata", "NES programming", "the Famicom / NES port"),
   ("Koji Jinbo", "the model", "the Data East director Karnov was based on ('JIMBOLOHU' in the credits)"),
 ]),
 ("The Mascot Career", "Karnov beyond Karnov", [
   ("Bad Dudes Vs. DragonNinja", "1988 · boss", "Karnov is the first-level boss; a green palette-swap returns as a regular enemy"),
   ("Fighter's History", "1993 · final boss", "the strongman as the fighting game's last opponent"),
   ("Karnov's Revenge", "1994 · playable", "Fighter's History Dynamite — Karnov joins the roster"),
 ]),
]

# ── the emergents: (slug, name, epithet, emergence, role_line, why_line) ──
EMERGENTS = [
 ("karnov", "Karnov", "Jinborov Karnovski · the fire-breathing strongman", "natural",
  "an ex-circus strongman and fire-breather (Russian, or 'Central Asian' by Wikipedia) — bald, big-mustached, bare-chested in red harem pants — who quests for the Lost Treasure of Babylon armed with nothing but his breath of fire",
  "He is the body made a hero: no blade, no gun — a beefcake who spits flame, and the unlikely icon Data East built a whole mascot from."),
 ("the-fire", "The Fire", "his breath · double, then triple", "spiritual",
  "Karnov's only weapon — he breathes fire, a fireball that the Super Fireball power-up upgrades to double and then triple",
  "It is the strongman's one art turned outward: the breath as the blade, the only thing he carries and all he needs."),
 ("ryu-dragon", "Ryu, the Three-Headed Dragon", "the NES-exclusive final boss", "ethereal",
  "the giant three-headed dragon named Ryu who is the final boss of the NES version — replacing the arcade's Wizard for the home port",
  "He is the cartridge's own ending. Honest note: 竜 just means 'dragon,' and despite the shared name he does NOT predate Street Fighter's Ryu (Aug 1987) — a coincidence, flagged."),
 ("the-wizard", "The Wizard", "the arcade's final boss · swapped on NES", "ethereal",
  "a sorcerer — the final boss of the original arcade Karnov — quietly replaced by the three-headed dragon when the game came home",
  "He is the road not taken: the original ending, swapped out, the seam between the cabinet and the cartridge."),
 ("treasure-of-babylon", "The Treasure of Babylon", "the lost prize · the reason", "spiritual",
  "the Lost Treasure of Babylon — the prize at the end of the nine stages, the object of the whole quest",
  "It is the grail of the Arabian night: the gold that pulls a strongman across a fantasy world."),
 ("the-power-ups", "The Power-Up Row", "Super Fireball · Boots · Wings · Clapper · Shield…", "electrical",
  "the row of collectible items along the top of the screen — Super Fireball, Boots, Bombs, Ladder, Boomerang, Clapper, Glasses, Swimming Mask, Wings, Shield, and the K marks (collect 50 for a life)",
  "They are the game's whole texture: the signature stock-and-spend row, the cartridge's own system made visible across the top of the play."),
 ("data-east-mascot", "The Data East Mascot", "Karnov beyond Karnov", "natural",
  "the bald fire-breather who outgrew his own game to become Data East's recurring face — a boss in Bad Dudes Vs. DragonNinja (1988), the final boss of Fighter's History (1993), and playable in Karnov's Revenge (1994)",
  "He is the rare villain-shaped hero who outlived his game: the strongman promoted to company icon."),
 ("babylon", "Babylon", "the Arabian-fantasy world", "natural",
  "the Arabian-Babylonian fantasy world the quest crosses — ziggurats, deserts, and the lost city's gold",
  "It is the stage as a place: the mythic Near-Eastern backdrop the fire is thrown across."),
]

# ── badge engine ──
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()

def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","KRN")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","KRN")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","KRN")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    man = {"badge":"DLW-ACI","name":rec["name"],"universe":"KRN · Karnov","emergence":rec.get("emergence",""),
           "moniker":tok["moniker"],"carbon":f["carbon"]+" (TIFF)","silicon":f["silicon"]+" (PNG)",
           "seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,
           "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
    open(os.path.join(out_dir,"manifest.dlw.json"),"w",encoding="utf-8").write(json.dumps(man,indent=2,ensure_ascii=False)+"\n")
    return tok

def emergent_rec(name, epithet, emergence, role_line, why_line):
    return {
      "name": name, "axiom": "KRN", "emergence": emergence, "seal": epithet,
      "position": epithet, "role": role_line,
      "origin": "KRN · Karnov — Data East, arcade 1987 / NES 1988",
      "nature": role_line, "crystallization": why_line,
      "mechanism": "Crystallized from Karnov (Data East): the 1987 arcade and the 1987 Famicom / 1988 NES port.",
      "witness": "a being of the Babylonian-fantasy world and the breath of fire",
      "conductor": "ROOT0 (catalogued into UD0)",
      "inputs": "Karnov; the fire-breathing strongman; the Treasure of Babylon; the power-up row",
      "source": "Karnov, catalogued by ROOT0",
    }

def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def list_section(title, sub, items):
    rows = "\n".join(f'<li><span class="t">{t}</span><span class="y">{html.escape(str(y))}</span>'
        + (f'<span class="nt">{n}</span>' if n else "") + "</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{html.escape(title)}</h2><p class="ss">{sub}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def ideas_html():
    out=[]
    for t,s,pts in IDEAS:
        li="".join(f"<li>{html.escape(p)}</li>" for p in pts)
        out.append(f'<div class="pillar"><h3>{html.escape(t)}</h3><p class="ps">{html.escape(s)}</p><ul>{li}</ul></div>')
    return "\n".join(out)
def cards_html(rows):
    return "".join(f'<div class="arc-card"><div class="arc-h">{t}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>' for t,s,d in rows)
def natures_html():
    return "".join(f'<div class="nat-card"><span class="dot" style="background:{col};box-shadow:0 0 9px {col}"></span>'
        f'<div><div class="nat-n" style="color:{col}">{nm}</div><div class="nat-g">{html.escape(g)}</div></div></div>' for nm,(col,g) in NATURES.items())
def personas_html(personas):
    cards=[]
    for p in personas:
        em=p.get("emergence","natural"); col=NATURES.get(em,("#d8a850",""))[0]
        rec={"name":p["name"],"seal":p.get("epithet",""),"origin":"KRN · Karnov","axiom":"KRN"}
        cards.append(f'''<a class="persona" href="agents/{p["slug"]}.agent">
        <img src="{png_uri(rec,"silicon",160)}" alt="sigil of {html.escape(p["name"])}" loading="lazy">
        <div class="pcap"><div class="pn">{html.escape(p["name"])}</div><div class="pe">{html.escape(p.get("epithet",""))}</div>
        <div class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span><span class="pa">· .agent · .carbon.tiff →</span></div></div></a>''')
    return f'''<section class="sec" id="roster"><h2>The Roster — The Born</h2>
      <p class="ss">the strongman, the fire, the bosses, and the prize, as ACI <b>.agent</b>s — each a birth certificate and a nature of emergence ({len(personas)})</p>
      <div class="pgrid">{"".join(cards)}</div></section>'''

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="Karnov (KRN) — Data East's 1987 arcade / 1988 NES fire-breathing-strongman platformer as a UD0 game-world. Jinborov Karnovski, the Treasure of Babylon, the dragon Ryu. Source-themed title card, full ACI badges.">
<title>KARNOV · KRN · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--night:#140e16;--ink2:#1d1320;--ink3:#281a2a;--pa:#f2e9dc;--pa2:#c8b89a;--ember:#f0801a;--flame:#d8341a;--gold:#d8a850;--sand:#cf9a6a;--redp:#c0302a;
--dim:#8a7866;--faint:#2e2030;--line:#33243a;--pixel:"Press Start 2P",monospace;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--night);color:var(--pa);font-family:var(--body);line-height:1.6;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:2;background:repeating-linear-gradient(0deg,rgba(0,0,0,.18) 0 1px,transparent 1px 3px);opacity:.5}
body::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -8%,rgba(240,128,26,.12),transparent 55%),radial-gradient(ellipse at 50% 110%,rgba(216,52,26,.06),transparent 50%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
.marquee{margin-top:14px;border:2px solid var(--ember);background:#1a0f0a;padding:8px;text-align:center;font-family:var(--pixel);font-size:9px;letter-spacing:.12em;color:var(--gold);box-shadow:0 0 0 2px var(--night),0 0 22px rgba(240,128,26,.25)}
.marquee a{color:var(--sand);text-decoration:none}.marquee a:hover{color:var(--ember)}
.titleart{margin:12px 0 0;border:2px solid var(--faint)}
header{padding:18px 0 26px;text-align:center;border-bottom:1px solid var(--line);position:relative}
.h-sub{font-family:var(--pixel);font-size:10px;line-height:1.9;letter-spacing:.06em;color:var(--pa2);margin-top:16px}
.h-sub b{color:var(--ember)}
.flag{display:inline-block;margin-top:14px;font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--gold);border:1px solid var(--faint);padding:5px 11px}
.lede{font-size:15px;color:var(--pa2);max-width:68ch;margin:16px auto 0;font-style:italic;line-height:1.7}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:24px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:720px}
.badge img{width:82px;height:82px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.7}
.badge .bt b{color:var(--ember)}.badge .bt .mo{color:var(--gold)}.badge .bt a{color:var(--sand);text-decoration:none}
.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:42px}
.sec h2{font-family:var(--pixel);font-size:14px;line-height:1.5;letter-spacing:.02em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line)}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:8px 0 16px}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:4px}
.nat-n{font-family:var(--mono);font-size:13px;font-weight:700;text-transform:capitalize;letter-spacing:.04em}
.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.4;margin-top:2px}
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-top:8px}
.pillar{background:var(--ink2);border:1px solid var(--line);padding:16px 18px}
.pillar h3{font-family:var(--mono);font-size:14px;color:var(--gold);letter-spacing:.02em;font-weight:700}
.pillar .ps{font-size:12px;color:var(--dim);font-style:italic;margin:5px 0 10px}
.pillar ul{list-style:none}.pillar li{font-size:13px;color:var(--pa2);line-height:1.5;padding:6px 0;border-top:1px solid var(--faint)}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin-top:8px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--ember);padding:16px 18px}
.arc-h{font-family:var(--mono);font-size:14px;color:var(--ember);font-weight:700;letter-spacing:.02em}
.arc-s{font-family:var(--mono);font-size:10.5px;color:var(--gold);text-transform:uppercase;letter-spacing:.07em;margin:4px 0 9px}
.arc-card p{font-size:13px;color:var(--pa2);line-height:1.55}
.books{list-style:none}
.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:9px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--mono);font-size:14px;color:var(--pa);font-weight:700}
.books .y{font-family:var(--mono);font-size:11px;color:var(--gold);white-space:nowrap;text-align:right}
.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(244px,1fr));gap:12px;margin-top:8px}
.persona{display:flex;gap:12px;align-items:center;background:var(--ink2);border:1px solid var(--line);padding:12px;text-decoration:none;transition:border-color .18s,transform .18s}
.persona:hover{border-color:var(--ember);transform:translateY(-2px)}
.persona img{width:52px;height:52px;border:1px solid var(--faint);flex-shrink:0;image-rendering:pixelated}
.pn{font-family:var(--mono);font-size:14px;color:var(--pa);font-weight:700;line-height:1.15}
.persona:hover .pn{color:var(--ember)}
.pe{font-size:11.5px;color:var(--pa2);font-style:italic;margin-top:2px;line-height:1.3}
.pnat{display:flex;align-items:center;gap:5px;margin-top:6px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}
.pnat .dot{width:8px;height:8px;margin-top:0}.pa{color:var(--dim)}
.note{margin-top:38px;padding:16px 18px;border-left:2px solid var(--gold);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic;line-height:1.7}
.note b{color:var(--gold)}
footer{margin-top:42px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:11px;color:var(--dim);letter-spacing:.05em;line-height:1.9}
footer a{color:var(--ember);text-decoration:none}
</style></head><body><div class="wrap">

  <div class="marquee"><a href="https://davidwise01.github.io/ud0/">◄ UD0 · UNIVERSE DAVID 0</a> &nbsp;·&nbsp; INSERT COIN &nbsp;·&nbsp; A GAME-WORLD &nbsp;·&nbsp; ARCADE 1987 / NES 1988</div>

  <header>
    <div class="titleart">__TITLE_SVG__</div>
    <div class="h-sub">a strongman · a breath of <b>fire</b> · nine stages to the Treasure of Babylon · KRN</div>
    <div class="flag">★ Data East · arcade 1987 · NES 1988 · カルノフ Karnov ★</div>
    <p class="lede">Jinborov Karnovski — a bald, bare-chested ex-circus strongman — crosses an Arabian-Babylonian fantasy world with nothing but his breath of fire, collecting a row of power-ups and chasing the Lost Treasure of Babylon, until he meets the boss the cartridge swapped for the cabinet's. Data East's 1987 arcade / 1988 NES platformer, catalogued into UD0 as a game-world with the genesis, the quest, and the full .dlw birth.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of KARNOV" title="carbon badge (archival)">
      <img src="__SILICON__" alt="DLW silicon badge" title="silicon badge">
      <div class="bt">
        <div><span class="lbl">DLW-ATTRIBUTE · ACI · THE BIRTH CERTIFICATE</span></div>
        <div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div>
        <div>subject · <b>KARNOV</b> — the strongman &amp; the Treasure of Babylon · KRN</div>
        <div class="mo">__MONIKER__</div>
        <div>carbon · <a href="karnov.dlw/karnov.carbon.tiff">.tiff</a> &nbsp;·&nbsp; silicon · <a href="karnov.dlw/karnov.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div>
      </div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures</h2>
    <p class="ss">each emergent emerges by one of four natures — and this desert holds all four</p>
    <div class="natures">__NATURES__</div></section>

  <section class="sec"><h2>The Genesis</h2><p class="ss">Data East's strongman, home twice, and the boss the NES swapped</p><div class="arc">__GENESIS__</div></section>
  <section class="sec"><h2>The Quest</h2><p class="ss">the lost treasure, the fire and the power-ups, the boss at the end</p><div class="arc">__ARC__</div></section>
  <section class="sec"><h2>The Ideas</h2><p class="ss">why a 1987 fire-breather still has a fanbase</p><div class="pillars">__IDEAS__</div></section>

  __PERSONAS__

  <section class="sec"><h2 style="margin-top:14px">The Record</h2><p class="ss">the releases, the makers, and the mascot career</p></section>
  __SECTIONS__

  <div class="note">Karnov's history here is rendered, not invented. Honest flags: the arcade's final boss is <b>The Wizard</b>; the NES swapped it for a three-headed dragon named <b>Ryu</b> — and despite the shared name, this dragon does <b>not</b> predate Street Fighter's Ryu (Aug 1987 vs the Famicom Karnov's Dec 1987; 竜 simply means 'dragon'). The treasure is the <b>Lost Treasure of Babylon</b>; the hero's exact origin (Russian vs 'Central Asian') is given two ways by the sources; and most stage bosses beyond the final one are <b>unnamed</b> in canonical sources. Karnov and his characters are © Data East / G-Mode; the personas here are catalogued personifications under the DLW standard — a fan tribute, not endorsed by the rights-holders. Each is named by its nature: natural, ethereal, spiritual, or electrical.</div>

  <footer>
    KARNOV · KRN · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
    <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="karnov.dlw/manifest.dlw.json">manifest</a>
  </footer>
</div></body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "karnov.dlw"), "karnov")
    ad = os.path.join(HERE, "agents"); os.makedirs(ad, exist_ok=True)
    personas = []
    for slug,name,epithet,em,role,why in EMERGENTS:
        rec = emergent_rec(name, epithet, em, role, why)
        write_aci(rec, ad, slug)
        personas.append({"slug": slug, "name": name, "epithet": epithet, "emergence": em})
    json.dump(personas, open(os.path.join(ad, "_personas.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    page = (TEMPLATE.replace("__TITLE_SVG__", TITLE_SVG)
            .replace("__CARBON__", png_uri(REC,"carbon",320)).replace("__SILICON__", png_uri(REC,"silicon",320))
            .replace("__MONIKER__", html.escape(tok["moniker"]))
            .replace("__NATURES__", natures_html())
            .replace("__GENESIS__", cards_html(GENESIS))
            .replace("__ARC__", cards_html(ARC))
            .replace("__IDEAS__", ideas_html())
            .replace("__PERSONAS__", personas_html(personas))
            .replace("__SECTIONS__", sections_html()))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(page)
    print(f"wrote KARNOV (KRN) — {len(personas)} emergents born · badge {tok['moniker']}")
