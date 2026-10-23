# Ruang PIAUD — Pengantar Ilmu Pendidikan

Portal materi kuliah S1 Pendidikan Islam Anak Usia Dini, UNISMAM Jambi. Pengampu: **Jules Nurhatmi, M.Pd.**

**Edisi 1.0 · 24 Oktober 2026.** 14 unit materi, UTS/UAS, peta belajar, bank kasus, glosarium, dan referensi. Semua halaman dapat dibaca tanpa JavaScript. Fitur tambahan: pencarian isi, cek pemahaman, refleksi lokal, ekspor catatan, progres pribadi, dan tampilan cetak.

## Mulai dari sini

- [Daftar seluruh materi dalam satu dokumen](docs/MATERI-KOMPILASI.md)
- [Peta kurikulum dan keputusan editorial](handbook/KALIBRASI.md)
- [Petunjuk publikasi GitHub Pages](handbook/PUBLIKASI.md)
- [Laporan pemeriksaan](handbook/QA.md)
- [Riwayat perubahan](CHANGELOG.md)

## Struktur repositori

| Lokasi | Fungsi |
|---|---|
| `content/course.json` | Sumber tunggal teks 14 unit, tujuan, latihan, kunci, refleksi, intisari |
| `content/references.json` | Bibliografi, jenis sumber, URL, dan batas penggunaan |
| `assets/` | CSS, JavaScript, ilustrasi beranda, dan diagram SVG |
| `scripts/build.py` | Menghasilkan HTML dan kompilasi Markdown dari sumber |
| `scripts/diagrams.py` | Menghasilkan diagram dari data unit |
| `scripts/validate.py` | Memeriksa struktur, sumber, tautan, dan jangkar lokal |
| `docs/` | Hasil siap GitHub Pages; tidak diedit langsung |
| `handbook/` | Dokumentasi editorial, publikasi, dan verifikasi |

## Menyunting dan membangun

Memerlukan Python 3. Tidak perlu npm, framework, akun mahasiswa, atau layanan basis data.

```bash
python3 scripts/diagrams.py
python3 scripts/build.py
python3 scripts/validate.py
```

Buka `docs/index.html` langsung untuk penggunaan lokal. Bila menggunakan server statis, arahkan document root ke `docs/`. Seluruh tautan dan aset relatif sehingga kompatibel dengan subpath GitHub Pages. `index.html` di akar menyediakan pengalihan jika Pages dipasang dari akar.

Edit `content/course.json`, jalankan build dan pemeriksaan, lalu commit sumber **dan** hasil `docs/`. Jangan mengedit HTML hasil secara manual karena perubahan akan tertimpa build berikutnya. Tambahkan alasan revisi akademik pada `CHANGELOG.md`.

## Batas penggunaan

Kompendium baru berdasarkan kerangka mata kuliah yang disepakati; bukan reproduksi naskah lama yang belum tersedia. Kalibrasi internal tidak sama dengan validasi ahli eksternal atau pengesahan RPS. Panduan UTS/UAS dan rubrik adalah usulan pembelajaran, bukan penetapan bobot resmi.

Catatan/progres hanya berada di peramban mahasiswa, tidak dikirim ke dosen. Jangan memasukkan identitas, diagnosis, atau data pribadi anak. Tugas resmi tetap dikelola dosen/LMS.

## Atribusi

Seluruh ilustrasi SVG dibuat khusus untuk portal; diagram merupakan sintesis pedagogis, bukan salinan diagram buku. Sumber berhak cipta ditautkan, tidak diunggah ulang. Tidak ada lisensi distribusi umum yang ditetapkan atas nama pemilik repositori; keputusan lisensi berada pada pemilik. Aset pihak ketiga tetap mengikuti hak masing-masing.
