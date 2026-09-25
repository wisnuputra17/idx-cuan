"""
IDX-CUAN — Static site generator untuk analisa saham IDX otomatis.
Sumber data: signal_engine.py (armada bot Wisnu) via Yahoo Finance.
Output: public/ (siap deploy ke Vercel / GitHub Pages / Netlify).

Monetisasi:
- Slot affiliate Ajaib (30% net revenue) — placeholder AJAIB_REF
- Slot AdSense (RPM finance tertinggi) — placeholder ADSENSE_SLOT
- Nanti: CTA langganan bot Telegram premium

Jalankan: ~/.hermes/venv/bin/python3 build_site.py
"""
import sys, os, json, datetime

sys.path.insert(0, '/Users/wisnuputra/trading-tools')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import signal_engine as se
from articles import ARTICLES

BASE = os.path.dirname(os.path.abspath(__file__))
PUBLIC = os.path.join(BASE, 'docs')
SITE_NAME = "IDX Cuan"
SITE_TAGLINE = "Analisa Teknikal Saham IDX Otomatis — Update Harian"
SITE_URL = "https://wisnuputra17.github.io/idx-cuan"  # GitHub Pages project URL

# --- Placeholder monetisasi (isi setelah daftar) ---
AJAIB_REF = "PLACEHOLDER_AJAIB"          # kode referral Ajaib
ADSENSE_CLIENT = "ca-pub-PLACEHOLDER"    # AdSense publisher id
GSC_VERIFY = "qX8QbC6aHiIWixybPmi6ww2zW680CIaWAuDP0l3FWJs"  # token Google Search Console

WATCHLIST = ["BBCA.JK","BBRI.JK","BMRI.JK","BBNI.JK","TLKM.JK","ASII.JK",
             "GOTO.JK","BUMI.JK","ANTM.JK","MDKA.JK","ADRO.JK","PGAS.JK",
             "UNVR.JK","ICBP.JK","CUAN.JK"]  # (di-override oleh NAMES.keys() di bawah)

NAMES = {
 "BBCA.JK":"Bank Central Asia","BBRI.JK":"Bank Rakyat Indonesia","BMRI.JK":"Bank Mandiri",
 "BBNI.JK":"Bank Negara Indonesia","BRIS.JK":"Bank Syariah Indonesia","ARTO.JK":"Bank Jago",
 "TLKM.JK":"Telkom Indonesia","ASII.JK":"Astra International","GOTO.JK":"GoTo Gojek Tokopedia",
 "BUMI.JK":"Bumi Resources","ANTM.JK":"Aneka Tambang","MDKA.JK":"Merdeka Copper Gold",
 "ADRO.JK":"Adaro Energy","PGAS.JK":"Perusahaan Gas Negara","UNVR.JK":"Unilever Indonesia",
 "ICBP.JK":"Indofood CBP","INDF.JK":"Indofood Sukses Makmur","CUAN.JK":"Petrindo Jaya Kreasi",
 "PTBA.JK":"Bukit Asam","ITMG.JK":"Indo Tambangraya","INCO.JK":"Vale Indonesia",
 "TINS.JK":"Timah","AMMN.JK":"Amman Mineral","MBMA.JK":"Merdeka Battery",
 "KLBF.JK":"Kalbe Farma","GGRM.JK":"Gudang Garam","HMSP.JK":"HM Sampoerna",
 "AKRA.JK":"AKR Corporindo","SMGR.JK":"Semen Indonesia","INTP.JK":"Indocement",
 "CPIN.JK":"Charoen Pokphand","JPFA.JK":"Japfa Comfeed","MAPI.JK":"Mitra Adiperkasa",
 "ACES.JK":"Aspirasi Hidup Indonesia","MNCN.JK":"Media Nusantara Citra","EMTK.JK":"Elang Mahkota",
 "BUKA.JK":"Bukalapak","EXCL.JK":"XL Axiata","ISAT.JK":"Indosat","TOWR.JK":"Sarana Menara",
 "BRPT.JK":"Barito Pacific","TPIA.JK":"Chandra Asri","ESSA.JK":"ESSA Industries",
 "PGEO.JK":"Pertamina Geothermal","RAJA.JK":"Rukun Raharja",
}
WATCHLIST = list(NAMES.keys())

CSS = """
:root{--bg:#0b0e14;--card:#151a23;--border:#232a36;--fg:#e6e9ef;--muted:#8b95a7;
--green:#22c55e;--red:#ef4444;--amber:#f59e0b;--accent:#3b82f6}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--fg);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;line-height:1.6}
a{color:var(--accent);text-decoration:none}
.wrap{max-width:960px;margin:0 auto;padding:20px}
header{border-bottom:1px solid var(--border);padding:24px 0;margin-bottom:24px}
header h1{font-size:1.6rem;font-weight:800}
header .tag{color:var(--muted);font-size:.9rem;margin-top:4px}
header .upd{color:var(--muted);font-size:.8rem;margin-top:8px}
.hero{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:20px;margin-bottom:20px}
.hero h2{font-size:1.15rem;margin-bottom:8px}
.hero p{color:var(--muted);font-size:.92rem}
table{width:100%;border-collapse:collapse;background:var(--card);border-radius:12px;overflow:hidden;border:1px solid var(--border)}
th,td{padding:12px 14px;text-align:left;font-size:.9rem;border-bottom:1px solid var(--border)}
th{background:#1a212c;color:var(--muted);font-weight:600;text-transform:uppercase;font-size:.72rem;letter-spacing:.04em}
tr:last-child td{border-bottom:none}
tr:hover td{background:#1a212c}
.badge{display:inline-block;padding:3px 10px;border-radius:20px;font-size:.75rem;font-weight:700}
.b-bull{background:rgba(34,197,94,.15);color:var(--green)}
.b-bear{background:rgba(239,68,68,.15);color:var(--red)}
.b-neu{background:rgba(245,158,11,.15);color:var(--amber)}
.score{font-weight:800;font-variant-numeric:tabular-nums}
.sc-p{color:var(--green)}.sc-n{color:var(--red)}.sc-0{color:var(--muted)}
.card{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:22px;margin-bottom:18px}
.card h2{font-size:1.3rem;margin-bottom:4px}
.card .sub{color:var(--muted);font-size:.88rem;margin-bottom:16px}
.sig{padding:10px 0;border-bottom:1px solid var(--border);font-size:.92rem}
.sig:last-child{border:none}
.sig .n{font-weight:700;font-size:.75rem;letter-spacing:.04em;color:var(--muted);display:inline-block;width:90px}
.levels{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:16px 0}
.lv{background:#1a212c;border-radius:10px;padding:14px;text-align:center}
.lv .l{font-size:.72rem;color:var(--muted);text-transform:uppercase}
.lv .v{font-size:1.25rem;font-weight:800;margin-top:4px}
.aff{background:linear-gradient(135deg,#1e3a5f,#152a45);border:1px solid #2d4a6f;border-radius:14px;padding:20px;margin:20px 0;text-align:center}
.aff h3{font-size:1.05rem;margin-bottom:6px}
.aff p{color:#a8c0dd;font-size:.88rem;margin-bottom:12px}
.btn{display:inline-block;background:var(--accent);color:#fff;padding:11px 26px;border-radius:10px;font-weight:700;font-size:.92rem}
.ad{background:var(--card);border:1px dashed var(--border);border-radius:10px;padding:24px;text-align:center;color:var(--muted);font-size:.8rem;margin:18px 0}
.disc{color:var(--muted);font-size:.78rem;margin-top:20px;padding:14px;background:var(--card);border-radius:10px;border:1px solid var(--border)}
footer{border-top:1px solid var(--border);margin-top:40px;padding:24px 0;color:var(--muted);font-size:.82rem;text-align:center}
.back{display:inline-block;margin-bottom:16px;font-size:.88rem}
.grid-links{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:10px;margin-top:16px}
.gl{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:12px;text-align:center;font-size:.85rem}
"""

def badge(verdict):
    if verdict.startswith("BULLISH"): return '<span class="badge b-bull">BULLISH</span>'
    if verdict.startswith("BEARISH"): return '<span class="badge b-bear">BEARISH</span>'
    return '<span class="badge b-neu">NETRAL</span>'

def score_cls(s):
    return "sc-p" if s>0 else "sc-n" if s<0 else "sc-0"

def head(title, desc, canonical):
    gsc = f'\n<meta name="google-site-verification" content="{GSC_VERIFY}">' if GSC_VERIFY else ''
    return f"""<!DOCTYPE html><html lang="id"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">{gsc}
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:type" content="website"><meta name="robots" content="index,follow">
<!-- AdSense: <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_CLIENT}" crossorigin="anonymous"></script> -->
<style>{CSS}</style></head><body><div class="wrap">"""

def header_html():
    upd = datetime.datetime.now().strftime("%d %B %Y, %H:%M WIB")
    return f"""<header><h1><a href="/" style="color:var(--fg)">📈 {SITE_NAME}</a></h1>
<div class="tag">{SITE_TAGLINE}</div><div class="upd">🔄 Terakhir update: {upd}</div></header>"""

def aff_box():
    return f"""<div class="aff"><h3>💡 Mau mulai investasi saham?</h3>
<p>Buka rekening saham gratis di Ajaib — beli saham IDX mulai dari receh. Pakai kode <b>{AJAIB_REF}</b> untuk bonus saham gratis.</p>
<a class="btn" href="https://ajaib.co.id/?ref={AJAIB_REF}" rel="sponsored nofollow" target="_blank">Buka Rekening Gratis →</a></div>"""

def ad_box(label="Iklan"):
    return f'<div class="ad">— slot {label} —</div>'

def disclaimer():
    return """<div class="disc">⚠️ <b>Disclaimer:</b> Seluruh analisa di situs ini dihasilkan otomatis oleh sistem berbasis indikator teknikal (MA, RSI, Donchian, Volume, ATR) dari data publik Yahoo Finance. Ini <b>BUKAN ajakan jual/beli</b> dan bukan nasihat keuangan. Pasar saham berisiko — Anda bisa rugi. Selalu <b>DYOR (Do Your Own Research)</b> dan konsultasi dengan penasihat keuangan berizin sebelum mengambil keputusan investasi.</div>"""

def footer():
    y = datetime.datetime.now().year
    return f"""<footer>© {y} {SITE_NAME} · Analisa otomatis berbasis data · Bukan nasihat keuangan<br>
Data: Yahoo Finance · Dibuat dengan sistem sinyal multi-indikator</footer></div></body></html>"""

def slug(sym): return sym.replace(".JK","").lower()

def build():
    os.makedirs(PUBLIC, exist_ok=True)
    results = []
    for sym in WATCHLIST:
        try:
            r = se.analyze(sym, verbose=False); results.append(r)
        except Exception as e:
            print(f"skip {sym}: {e}")
    results.sort(key=lambda x:-x['score'])

    # --- Homepage ---
    rows = ""
    for r in results:
        s = r['score']; nm = NAMES.get(r['symbol'], r['symbol'])
        rows += f"""<tr><td><a href="/{slug(r['symbol'])}.html"><b>{slug(r['symbol']).upper()}</b></a><br><span style="color:var(--muted);font-size:.78rem">{nm}</span></td>
<td>{r['price']:.0f}</td>
<td class="score {score_cls(s)}">{s:+d}</td>
<td>{badge(r['verdict'])}</td>
<td style="font-size:.82rem;color:var(--muted)">{r['date']}</td></tr>"""

    bull = sum(1 for r in results if r['score']>=30)
    bear = sum(1 for r in results if r['score']<=-30)
    home = head(f"{SITE_NAME} — {SITE_TAGLINE}",
        f"Analisa teknikal {len(results)} saham IDX paling likuid, update harian otomatis. Sinyal bullish/bearish, level entry, stop loss, take profit berbasis MA, RSI, Donchian & volume.",
        SITE_URL)
    home += header_html()
    home += f"""<div class="hero"><h2>Ranking Sinyal Saham IDX Hari Ini</h2>
<p>{len(results)} saham dianalisa otomatis pakai 5 indikator teknikal. <b style="color:var(--green)">{bull} bullish</b> · <b style="color:var(--red)">{bear} bearish</b> · sisanya netral. Klik ticker untuk analisa lengkap + level trading.</p></div>"""
    home += ad_box("Iklan (AdSense)")
    home += f"""<table><thead><tr><th>Saham</th><th>Harga</th><th>Skor</th><th>Sinyal</th><th>Update</th></tr></thead><tbody>{rows}</tbody></table>"""
    home += aff_box()
    # Section Belajar (link ke artikel edukasi)
    art_links = "".join(
        f'<a class="gl" href="/belajar/{a["slug"]}.html">📚 {a["title"]}</a>'
        for a in ARTICLES)
    home += f"""<div style="margin-top:28px"><h2 style="font-size:1.15rem;margin-bottom:6px">📚 Belajar Analisa Teknikal</h2>
<p style="color:var(--muted);font-size:.9rem">Panduan singkat memahami indikator yang dipakai IDX Cuan.</p>
<div class="grid-links">{art_links}</div></div>"""
    home += disclaimer() + footer()
    with open(os.path.join(PUBLIC,'index.html'),'w') as f: f.write(home)

    # --- Per-stock pages ---
    for r in results:
        sym = r['symbol']; nm = NAMES.get(sym, sym); sl = slug(sym)
        sigs = ""
        for name, dir_, desc in r['signals']:
            mk = "🟢" if dir_=="+" else "🔴" if dir_=="-" else "⚪"
            sigs += f'<div class="sig"><span class="n">{mk} {name}</span> {desc}</div>'
        page = head(f"Analisa Saham {sl.upper()} ({nm}) Hari Ini — Sinyal Teknikal | {SITE_NAME}",
            f"Analisa teknikal saham {sl.upper()} {nm} hari ini: skor {r['score']:+d}, {r['verdict']}. Level entry {r['entry_level']:.0f}, SL {r['sl_level']:.0f}, TP {r['tp_level']:.0f}. Update otomatis harian.",
            f"{SITE_URL}/{sl}.html")
        page += header_html()
        page += '<a class="back" href="/">← Kembali ke ranking</a>'
        page += f"""<div class="card"><h2>{sl.upper()} — {nm}</h2>
<div class="sub">Harga: <b>Rp {r['price']:.0f}</b> · {r['date']} · {badge(r['verdict'])} <span class="score {score_cls(r['score'])}">skor {r['score']:+d}</span></div>
<h3 style="font-size:.95rem;margin-bottom:8px">📊 Detail Indikator Teknikal</h3>{sigs}
<div class="levels">
<div class="lv"><div class="l">Entry (breakout)</div><div class="v">{r['entry_level']:.0f}</div></div>
<div class="lv"><div class="l">Stop Loss</div><div class="v" style="color:var(--red)">{r['sl_level']:.0f}</div></div>
<div class="lv"><div class="l">Take Profit</div><div class="v" style="color:var(--green)">{r['tp_level']:.0f}</div></div></div>
<p style="color:var(--muted);font-size:.85rem">Risk:Reward ≈ 1:{r['risk_reward']} · Level dihitung dari Donchian 10-hari breakout + ATR14 (volatilitas), bukan angka tebakan.</p></div>"""
        page += ad_box("Iklan (AdSense)")
        page += aff_box()
        page += disclaimer() + footer()
        with open(os.path.join(PUBLIC,f'{sl}.html'),'w') as f: f.write(page)

    # --- Artikel edukasi (SEO evergreen) ---
    os.makedirs(os.path.join(PUBLIC,'belajar'), exist_ok=True)
    for a in ARTICLES:
        ap = head(f"{a['title']} | {SITE_NAME}", a['desc'],
                  f"{SITE_URL}/belajar/{a['slug']}.html")
        ap += f'<meta name="keywords" content="{a["kw"]}">'
        ap += header_html()
        ap += '<a class="back" href="/">← Kembali ke ranking saham</a>'
        ap += f'<article class="card"><h1 style="font-size:1.5rem;margin-bottom:16px">{a["title"]}</h1>{a["body"]}</article>'
        ap += ad_box("Iklan (AdSense)")
        ap += aff_box()
        ap += disclaimer() + footer()
        with open(os.path.join(PUBLIC,'belajar',f'{a["slug"]}.html'),'w') as f: f.write(ap)

    # sitemap + robots
    urls = [f"{SITE_URL}/"] + [f"{SITE_URL}/{slug(r['symbol'])}.html" for r in results]
    urls += [f"{SITE_URL}/belajar/{a['slug']}.html" for a in ARTICLES]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    today = datetime.date.today().isoformat()
    for u in urls: sm += f"<url><loc>{u}</loc><lastmod>{today}</lastmod></url>\n"
    sm += "</urlset>"
    with open(os.path.join(PUBLIC,'sitemap.xml'),'w') as f: f.write(sm)
    with open(os.path.join(PUBLIC,'robots.txt'),'w') as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
    open(os.path.join(PUBLIC,'.nojekyll'),'w').close()

    print(f"Built {len(results)+1} pages -> {PUBLIC}")
    return results

if __name__ == '__main__':
    build()
