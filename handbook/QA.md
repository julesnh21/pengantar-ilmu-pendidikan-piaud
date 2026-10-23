# Pemeriksaan edisi 1.0

Tanggal: 24 Oktober 2026. Pemeriksaan internal, bukan validasi ahli eksternal.

## Pemeriksaan otomatis

`python3 scripts/validate.py` lulus:

- 14 unit dengan pemetaan P1–7 dan P9–15; UTS P8 dan UAS P16.
- 23 halaman HTML; satu H1 dan bahasa Indonesia per halaman.
- 25 entri sumber; seluruh ID rujukan unit terhubung ke bibliografi.
- Semua tautan file dan jangkar HTML internal ditemukan.
- Ilustrasi memiliki teks alternatif, tautan tab baru diberi perlindungan.
- Tidak ditemukan placeholder atau catatan uji dalam hasil HTML.
- Materi inti sekitar 4.976 kata, di luar kasus, aktivitas, refleksi, glosarium, dan referensi. Ini kompendium pengantar, bukan buku teks panjang.
- `node --check assets/app.js` lulus pemeriksaan sintaks.

## Pemeriksaan peramban

- Beranda desktop diperiksa secara visual: hierarki, kartu materi, ilustrasi, dan navigasi terbaca.
- Tata letak 390 piksel diperiksa dalam iframe ukuran tetap; menu buka/tutup berfungsi. Ini pemeriksaan breakpoint, bukan pengujian perangkat ponsel fisik.
- Pencarian “scaffolding” menampilkan dua unit yang relevan pada isi.
- Kuis diuji dengan jawaban keliru dan tepat; pembahasan tampil sesuai.
- Refleksi dan penanda selesai bertahan setelah pemuatan ulang.
- Data uji kemudian dikosongkan dan progres kembali 0/14.
- Halaman materi dan bibliografi diperiksa secara visual.

## Batas pemeriksaan

- Belum ada audit aksesibilitas eksternal, pengujian pembaca layar, atau pencetakan fisik; CSS cetak tersedia.
- Pengunduhan ekspor dan dialog hapus belum diuji end-to-end; implementasinya ditinjau, tetapi jangan menyebut seluruh fitur telah diuji dinamis.
- URL sumber eksternal ditelusuri untuk bibliografi, namun seluruh endpoint tidak dijamin selalu tersedia. Beberapa PDF resmi gagal diambil; klaim dibatasi pada informasi yang terkonfirmasi.
- Peramban menampilkan pesan ekstensi internal; tidak dijadikan bukti adanya kesalahan aplikasi portal.
- Halaman pengaturan GitHub Pages membutuhkan sesi masuk yang tidak tersedia. Aktivasi publikasi belum diverifikasi.

## Edisi 1.1 — pemeriksaan visual

- 14 ilustrasi kasus diperiksa satu per satu dan dihubungkan dengan deskripsi alternatif, dua pertanyaan pengamatan, serta latihan visual.
- 14 diagram diganti dengan hubungan konsep yang relevan. Diagram PAUD memuat pendidikan, kesehatan/gizi, pengasuhan, perlindungan, dan kesejahteraan. Diagram ekologi diberi batas sebagai penyederhanaan, bukan representasi lengkap teori.
- Semua WebP dapat didekode (1536 × 1024); ukuran sekitar 124–224 KiB per gambar. Ilustrasi menggunakan berkas lokal, tanpa ketergantungan hotlink.
- 23 halaman, 14 unit, 25 entri referensi: pemeriksaan struktur, tautan, jangkar, teks alternatif, dan cakupan visual lulus tanpa kesalahan.
- Pratinjau desktop: kasus bergambar, diagram PAUD, kartu pertemuan, serta pembahasan latihan visual diperiksa di peramban.
- Pratinjau iframe lebar 390 piksel: diagram scaffolding dan penjelasan terbaca; lebar konten sama dengan viewport (375 piksel setelah scrollbar), tanpa luapan horizontal.
- Pembahasan latihan visual dapat dibuka melalui kontrol `details`; konten inti tetap tersedia tanpa JavaScript.
- Pemeriksaan ini merupakan QA editorial/teknis internal, bukan pengukuran hasil belajar atau validasi ahli eksternal.
