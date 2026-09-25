"""
Artikel edukasi evergreen untuk IDX Cuan — konten SEO jangka panjang.
Target keyword: 'apa itu RSI saham', 'cara baca moving average', dll.
Setiap artikel = 1 halaman ter-index. Ditulis netral + edukatif, ada CTA affiliate + disclaimer.
"""

ARTICLES = [
    {
        "slug": "apa-itu-rsi",
        "title": "Apa Itu RSI dalam Analisa Saham? Cara Baca & Contoh",
        "kw": "apa itu RSI, RSI saham, indikator RSI, overbought oversold",
        "desc": "RSI (Relative Strength Index) adalah indikator momentum untuk mengukur apakah saham overbought atau oversold. Pelajari cara baca RSI 14, level 70/30, dan contoh penerapannya di saham IDX.",
        "body": """
<h2>Apa Itu RSI?</h2>
<p><b>RSI (Relative Strength Index)</b> adalah indikator momentum yang mengukur kecepatan dan besarnya perubahan harga. Nilainya bergerak dari <b>0 sampai 100</b>. RSI diperkenalkan J. Welles Wilder tahun 1978 dan sampai sekarang jadi salah satu indikator paling populer di kalangan trader.</p>

<h2>Cara Baca RSI</h2>
<ul>
<li><b>RSI di atas 70</b> — kondisi <i>overbought</i> (jenuh beli). Harga sudah naik banyak, berpotensi koreksi. Bukan berarti wajib jual, tapi sinyal waspada.</li>
<li><b>RSI di bawah 30</b> — kondisi <i>oversold</i> (jenuh jual). Harga sudah turun dalam, berpotensi rebound.</li>
<li><b>RSI 30–70</b> — zona netral. Momentum belum ekstrem ke arah manapun.</li>
</ul>

<h2>RSI Periode Berapa yang Dipakai?</h2>
<p>Standar paling umum adalah <b>RSI 14</b> (14 periode/hari). Trader jangka pendek kadang pakai RSI 7 (lebih sensitif), sedangkan investor jangka panjang bisa pakai RSI 21 (lebih halus).</p>

<h2>Kelemahan RSI yang Harus Dipahami</h2>
<p>RSI bisa "menipu" di pasar yang sedang <i>trending</i> kuat — saham bisa tetap overbought (RSI &gt; 70) sambil terus naik berhari-hari. Karena itu, <b>jangan pakai RSI sendirian</b>. Kombinasikan dengan analisa trend (Moving Average) dan volume. Di sistem <a href="/">IDX Cuan</a>, RSI hanyalah 1 dari 5 indikator yang digabung jadi skor komposit.</p>

<h2>Contoh Praktis</h2>
<p>Misal saham X punya RSI 14 = 25. Ini menandakan oversold — banyak yang sudah jual, harga tertekan. Kalau ditemani sinyal lain (misal volume naik + harga menyentuh support), ini bisa jadi peluang rebound. Tapi tetap: konfirmasi dulu, jangan asal "tangkap pisau jatuh".</p>
""",
    },
    {
        "slug": "apa-itu-moving-average",
        "title": "Moving Average (MA) Saham: MA20, MA50 & Golden Cross",
        "kw": "moving average saham, MA20 MA50, golden cross, death cross, cara baca MA",
        "desc": "Moving Average (MA) meratakan harga untuk memperjelas arah trend. Pelajari beda MA20 vs MA50, sinyal Golden Cross & Death Cross, dan cara memakainya di saham IDX.",
        "body": """
<h2>Apa Itu Moving Average?</h2>
<p><b>Moving Average (MA)</b> atau rata-rata bergerak adalah indikator yang meratakan data harga selama periode tertentu untuk memperjelas arah <i>trend</i>. MA20 = rata-rata harga 20 hari terakhir; MA50 = 50 hari terakhir.</p>

<h2>MA20 vs MA50</h2>
<ul>
<li><b>MA20 (jangka pendek)</b> — lebih responsif, cepat bereaksi terhadap perubahan harga. Cocok untuk trader.</li>
<li><b>MA50 (jangka menengah)</b> — lebih halus, menggambarkan trend yang lebih besar. Cocok untuk swing/investor.</li>
</ul>

<h2>Golden Cross & Death Cross</h2>
<p>Ini dua sinyal klasik dari perpotongan MA:</p>
<ul>
<li>🟢 <b>Golden Cross</b> — MA pendek (MA20) memotong ke ATAS MA panjang (MA50). Sinyal bullish, momentum naik.</li>
<li>🔴 <b>Death Cross</b> — MA pendek memotong ke BAWAH MA panjang. Sinyal bearish, momentum turun.</li>
</ul>

<h2>Cara Baca Posisi Harga vs MA</h2>
<p>Susunan yang ideal untuk uptrend: <b>Harga &gt; MA20 &gt; MA50</b> (semua sejajar naik / <i>aligned</i>). Sebaliknya, Harga &lt; MA20 &lt; MA50 menandakan downtrend. Di <a href="/">IDX Cuan</a>, alignment ini jadi komponen "Trend" dalam skor tiap saham.</p>

<h2>Kelemahan MA</h2>
<p>MA adalah indikator <i>lagging</i> (tertinggal) — dia mengonfirmasi trend yang sudah terjadi, bukan memprediksi. Di pasar <i>sideways</i> (mendatar), MA sering kasih sinyal palsu. Karena itu selalu kombinasikan dengan volume & momentum.</p>
""",
    },
    {
        "slug": "apa-itu-donchian-channel",
        "title": "Donchian Channel: Strategi Breakout Saham yang Simpel",
        "kw": "donchian channel, strategi breakout saham, trading breakout, channel breakout",
        "desc": "Donchian Channel adalah indikator breakout yang menandai harga tertinggi & terendah dalam N hari. Pelajari cara pakai strategi breakout Donchian untuk trading saham IDX.",
        "body": """
<h2>Apa Itu Donchian Channel?</h2>
<p><b>Donchian Channel</b> adalah indikator yang dibuat Richard Donchian. Cara kerjanya sederhana: garis atas = harga <b>tertinggi</b> dalam N hari terakhir, garis bawah = harga <b>terendah</b> dalam N hari terakhir. Umum dipakai periode 10 atau 20 hari.</p>

<h2>Strategi Breakout</h2>
<p>Logikanya: kalau harga <b>menembus ke atas garis atas</b> Donchian, artinya harga membuat titik tertinggi baru — sinyal <i>breakout</i> bullish, momentum kuat. Sebaliknya, tembus ke bawah garis bawah = <i>breakdown</i>, sinyal keluar/hindari.</p>

<h2>Kenapa Donchian Efektif?</h2>
<p>Strategi breakout menangkap awal dari trend besar. Dalam backtest sistem IDX Cuan selama 5 tahun, <b>Donchian 10-hari terbukti paling robust</b> dibanding indikator lain untuk saham volatil — karena dia objektif (tidak ada tebakan) dan menangkap momentum nyata, bukan noise.</p>

<h2>Kombinasi dengan ATR untuk Stop Loss</h2>
<p>Breakout harus dilindungi <i>stop loss</i>. IDX Cuan menghitung level SL/TP pakai <b>ATR (Average True Range)</b> — ukuran volatilitas. SL ditaruh 1.5x ATR di bawah entry, TP 3x ATR di atas (risk:reward 1:2). Ini jauh lebih akurat daripada persentase tetap, karena menyesuaikan volatilitas tiap saham.</p>

<h2>Peringatan</h2>
<p>Breakout bisa gagal (<i>false breakout</i>) — harga tembus lalu balik lagi. Konfirmasi dengan <b>volume</b>: breakout yang sehat disertai lonjakan volume. Tanpa volume, breakout patut dicurigai.</p>
""",
    },
    {
        "slug": "cara-baca-sinyal-idx-cuan",
        "title": "Cara Baca Sinyal & Skor di IDX Cuan",
        "kw": "cara baca sinyal saham, skor teknikal, analisa saham otomatis, sinyal bullish bearish",
        "desc": "Panduan membaca skor komposit, verdict bullish/bearish/netral, dan level entry/SL/TP di IDX Cuan. Pahami cara sistem menggabungkan 5 indikator teknikal.",
        "body": """
<h2>Bagaimana Skor Dihitung?</h2>
<p>IDX Cuan menggabungkan <b>5 indikator teknikal</b> menjadi satu skor komposit dari <b>-100 (sangat bearish) sampai +100 (sangat bullish)</b>:</p>
<ul>
<li><b>Trend (MA20/MA50)</b> — bobot ±20. Cek alignment harga vs moving average.</li>
<li><b>Momentum (RSI14)</b> — bobot ±10. Overbought/oversold.</li>
<li><b>Breakout (Donchian 10)</b> — bobot ±35. Komponen terbesar; menangkap breakout nyata.</li>
<li><b>Volume</b> — bobot ±15. Konfirmasi partisipasi pasar.</li>
</ul>

<h2>Arti Verdict</h2>
<ul>
<li>🟢 <b>BULLISH</b> (skor ≥ +30) — mayoritas indikator selaras positif. Layak dipertimbangkan untuk entry.</li>
<li>🔴 <b>BEARISH</b> (skor ≤ -30) — sinyal negatif dominan. Sebaiknya hindari atau keluar.</li>
<li>🟡 <b>NETRAL</b> (di antaranya) — sinyal campur. Tunggu konfirmasi lebih jelas.</li>
</ul>

<h2>Level Entry, Stop Loss, Take Profit</h2>
<p>Setiap saham punya 3 level yang dihitung dari <b>Donchian breakout + ATR</b>, bukan angka tebakan:</p>
<ul>
<li><b>Entry</b> — level breakout di atas resistance 10-hari.</li>
<li><b>Stop Loss</b> — 1.5x ATR di bawah entry (batas rugi).</li>
<li><b>Take Profit</b> — 3x ATR di atas entry (target untung). Risk:reward 1:2.</li>
</ul>

<h2>Penting: Ini Alat Bantu, Bukan Perintah</h2>
<p>Skor IDX Cuan adalah <b>alat bantu analisa</b>, bukan ajakan beli/jual. Sistem hanya membaca data teknikal harga & volume — tidak tahu berita, laporan keuangan, atau aksi korporasi. Selalu gabungkan dengan riset Anda sendiri (DYOR) dan pertimbangan risiko pribadi.</p>
""",
    },
]
