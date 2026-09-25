#!/usr/bin/env python3
"""
IDX Cuan — daily auto-update runner.
Dijalankan cron tiap sore setelah market close.

Alur:
1. Gate hari bursa (skip weekend/libur via idx_calendar dari trading-tools).
2. Rebuild website (build_site.py).
3. Commit + push HANYA kalau sinyal berubah (bandingkan hash data signal,
   bukan timestamp) — biar nggak spam commit kosong.

Output: print ringkas (dipakai cron untuk notifikasi; kosong = no-op senyap).
"""
import sys, os, subprocess, hashlib, json, datetime

REPO = "/Users/wisnuputra/idx-cuan"
VENV_PY = "/Users/wisnuputra/.hermes/venv/bin/python3"
sys.path.insert(0, "/Users/wisnuputra/trading-tools")

import idx_calendar

def run(cmd, cwd=REPO):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, shell=isinstance(cmd, str))
    return r.returncode, r.stdout.strip(), r.stderr.strip()

def signal_fingerprint():
    """Hash dari verdict+score tiap saham (abaikan timestamp) untuk deteksi perubahan riil."""
    import build_site  # noqa
    # Re-import signal_engine hasil analisa lewat build output data
    # build_site.build() menulis docs/; kita baca ulang skor dari hasil terbaru.
    # Lebih simpel: panggil analyze langsung.
    import signal_engine as se
    sigs = []
    for sym in build_site.WATCHLIST:
        try:
            r = se.analyze(sym, verbose=False)
            sigs.append((sym, r['score'], r['verdict'], round(r['price'], 1)))
        except Exception:
            sigs.append((sym, None, "ERR", None))
    blob = json.dumps(sigs, sort_keys=True)
    return hashlib.sha256(blob.encode()).hexdigest(), sigs

def main():
    ok, reason = idx_calendar.should_run_today()
    if not ok:
        # Hari libur/weekend — no-op senyap (cron no_agent: stdout kosong = tak ada notifikasi)
        return

    os.chdir(REPO)
    sys.path.insert(0, REPO)

    fp_path = os.path.join(REPO, ".last_fingerprint")
    new_fp, sigs = signal_fingerprint()
    old_fp = ""
    if os.path.exists(fp_path):
        old_fp = open(fp_path).read().strip()

    # Rebuild selalu (biar timestamp fresh), tapi push hanya kalau fingerprint beda
    rc, out, err = run([VENV_PY, "build_site.py"])
    if rc != 0:
        print(f"❌ IDX Cuan build GAGAL: {err[:300]}")
        return

    if new_fp == old_fp:
        # Data sinyal sama — skip push biar nggak spam commit
        return

    open(fp_path, "w").write(new_fp)
    run("git add -A")
    today = datetime.date.today().isoformat()
    run(["git", "-c", "user.email=wisnuputra1.wp@gmail.com",
         "-c", "user.name=Wisnu Putra", "commit", "-q", "-m",
         f"auto-update sinyal {today}"])
    rc, out, err = run("git push -q origin main")
    if rc != 0:
        print(f"⚠️ IDX Cuan: build OK tapi push gagal: {err[:200]}")
        return

    # Ringkasan perubahan untuk notifikasi
    bull = [s for s in sigs if s[1] is not None and s[1] >= 30]
    bear = [s for s in sigs if s[1] is not None and s[1] <= -30]
    top = sorted([s for s in sigs if s[1] is not None], key=lambda x: -x[1])[:3]
    top_str = ", ".join(f"{s[0].replace('.JK','')}({s[1]:+d})" for s in top)
    print(f"✅ IDX Cuan updated {today} — {len(bull)} bullish, {len(bear)} bearish. "
          f"Top: {top_str}. Live: https://wisnuputra17.github.io/idx-cuan/")

if __name__ == "__main__":
    main()
