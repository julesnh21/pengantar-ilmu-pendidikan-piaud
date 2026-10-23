# Publikasi GitHub Pages

Repositori publik, cabang `main`, dan izin penulisan telah diverifikasi. Halaman pengaturan Pages belum dapat diperiksa karena peramban sesi tidak masuk ke GitHub; koneksi API yang tersedia tidak menyediakan perubahan Pages. Karena itu, status situs publik **belum diklaim aktif** pada serah terima awal.

## Aktivasi oleh pemilik

1. Buka repositori → **Settings → Pages**.
2. Pada **Build and deployment**, pilih **Deploy from a branch**.
3. Pilih cabang **main**, folder **/docs**, lalu **Save**.
4. Tunggu proses Pages selesai. Gunakan URL yang ditampilkan GitHub setelah berhasil.

Folder `docs/` sudah berisi HTML, aset, dan `.nojekyll`. Tidak membutuhkan workflow khusus atau instalasi paket. Jika telah terpasang dari `/ (root)`, halaman akar mengalihkan ke `docs/index.html`; pilihan `/docs` tetap lebih langsung.

## Pemeriksaan setelah publikasi

Buka beranda, satu materi, pencarian, ilustrasi, dan referensi. Uji pada ponsel. Periksa tab Actions/riwayat Pages jika penerbitan gagal. Jangan menganggap commit berhasil sebagai bukti deploy berhasil.

## Memperbarui

Edit sumber → jalankan `python3 scripts/build.py` dan `python3 scripts/validate.py` → commit ke `main`. Pada Pages berbasis cabang, perubahan di direktori sumber akan diproses oleh GitHub. Periksa hasil deploy sesudahnya.
