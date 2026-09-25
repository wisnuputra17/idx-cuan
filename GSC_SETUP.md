# 🔍 Setup Google Search Console — IDX Cuan

**Tujuan:** Daftarkan website ke Google biar cepat ke-index (dari mingguan → harian) + bisa pantau performa (keyword apa yang bikin orang datang, posisi ranking, dll).

**Yang kamu lakukan:** ~5 menit, sekali doang. Sisanya aku.

---

## Langkah 1 — Buka Google Search Console
1. Ke https://search.google.com/search-console
2. Login pakai akun Google-mu (wisnuputra1.wp@gmail.com)

## Langkah 2 — Add Property
1. Klik **"Add Property"** (atau dropdown properti kiri atas → Add property)
2. Pilih tipe **"URL prefix"** (yang KANAN, bukan Domain)
3. Masukkan: `https://wisnuputra17.github.io/idx-cuan/`
4. Klik **Continue**

## Langkah 3 — Verifikasi pakai HTML tag
1. Di halaman verifikasi, pilih metode **"HTML tag"**
2. Google kasih kode kayak gini:
   ```html
   <meta name="google-site-verification" content="ABC123xyz...." />
   ```
3. **COPY bagian `content="..."` nya aja** — yaitu token `ABC123xyz....`
4. **JANGAN klik Verify dulu!** Kasih token itu ke aku dulu.

## Langkah 4 — Kasih token ke Mr. Rich
Cukup paste token-nya di chat, contoh:
> "token GSC: ABC123xyz...."

Lalu **aku otomatis**:
- Pasang meta tag ke semua 50 halaman
- Rebuild + push ke GitHub Pages
- Konfirmasi ke kamu kalau udah live

## Langkah 5 — Klik Verify (balik ke GSC)
Setelah aku bilang "udah live", balik ke tab GSC → klik **Verify**. Beres! ✅

## Langkah 6 (aku yang lakukan setelah verified)
- Submit sitemap: `https://wisnuputra17.github.io/idx-cuan/sitemap.xml`
- Google mulai crawl 50 halaman kita

---

## ❓ FAQ
**Q: Kenapa nggak pakai akun aku aja langsung?**
A: GSC butuh login Google interaktif + verifikasi kepemilikan — itu yang cuma bisa kamu lakukan (fasilitator). Setelah verified, semua pemantauan & optimasi aku yang urus.

**Q: Aman nggak?**
A: Aman. Token verifikasi cuma nunjukin ke Google "aku pemilik situs ini" — nggak ngasih akses apa-apa ke akun Google-mu.

**Q: Berapa lama sampai muncul di Google?**
A: Setelah submit sitemap, indexing mulai dalam beberapa hari. Ranking naik seiring waktu (SEO tetap butuh 2-4 bulan buat trafik signifikan).
