<div align="center">
  <img src="v2/logo.png" alt="NEXPHYRIX Logo" width="120" />
  <h1>NEXPHYRIX — PS4 Exploit Host</h1>
  <p><strong>Advanced Offline Exploit Host for PlayStation 4 WebKit</strong></p>
</div>

---

NEXPHYRIX adalah host jailbreak PS4 modern yang dioptimalkan untuk performa tinggi, stabilitas, dan mendukung penyimpanan offline penuh melalui HTML5 `applicationCache`. Setelah melakukan proses caching satu kali, Anda dapat menjalankan exploit PS4 selamanya tanpa membutuhkan koneksi internet.

## ✨ Fitur Utama
- **Fully Offline Ready**: Mendukung *offline caching* otomatis. Tidak perlu DNS palsu (Fake DNS) atau ESP8266.
- **Auto-Detection**: Secara otomatis mendeteksi status cache dan jaringan PS4.
- **Modern UI**: Desain antarmuka *cyberpunk-style* yang futuristik dan responsif.
- **Dua Mode Eksploit**: Mendukung metode exploit lawas hingga yang terbaru (Lapse & Poops).

---

## 🎮 Kompatibilitas Firmware

NEXPHYRIX menyediakan dua engine exploit yang bisa dipilih sesuai versi Firmware PS4 Anda:

| Mode | Engine / Method | Kompatibilitas Firmware | Status |
|:----:|:---:|:---:|:---:|
| **Mode 01** | Standard PS4 HEN | `6.20` – `11.02` | ✅ Stabil |
| **Mode 02** | Lapse & Poops Chain | `11.00` – `13.00` | ⚠️ Eksperimental |

---

## 🚀 Panduan Penggunaan (Instalasi Offline Cache)

Lakukan langkah ini hanya **Satu Kali Saja**. Setelah berhasil, Anda tidak perlu lagi menghubungkan PS4 ke internet.

1. **Hubungkan PS4 ke Internet**  
   Buka menu `Settings` > `Network` dan pastikan PS4 Anda terhubung ke koneksi internet normal.
2. **Buka Browser PS4**  
   Akses URL Host NEXPHYRIX Anda (contoh: `https://username.github.io/nexphyrix/`).
3. **Mulai Proses Caching**  
   Di halaman utama, biarkan sistem memproses secara otomatis atau tekan tombol **CACHE WEBSITE**.
   - Sistem akan mengunduh payload (sekitar 20MB - 30MB).
   - Tunggu hingga *progress bar* mencapai 100% dan status berubah menjadi **CACHED ✓ — OFFLINE READY**.
4. **Matikan Internet (Sangat Disarankan)**  
   Kembali ke `Settings` > `Network` dan **matikan koneksi internet (hilangkan centang Connect to the Internet)** untuk mencegah pembaruan firmware PS4 secara diam-diam oleh Sony.
5. **Jalankan Exploit**  
   Buka kembali browser (halaman akan dimuat secara instan tanpa internet). Pilih **Mode 01** atau **Mode 02**, lalu tekan **Launch Lapse** atau metode pilihan Anda.

---

## 🔄 Pembaruan Cache (Update)

Jika Anda melihat pengumuman ada versi terbaru dari NEXPHYRIX, Anda dapat memperbarui cache yang tersimpan di PS4 Anda dengan cara:

1. Nyalakan kembali internet di PS4 Anda.
2. Buka halaman utama NEXPHYRIX.
3. Tekan tombol **RESTART CACHE** (berlogo panah melingkar ↻).
4. Browser akan otomatis mendeteksi pembaruan dan mengunduh ulang versi terbarunya.
5. Setelah selesai, matikan kembali internet Anda.

---

## 🛠️ Informasi Deployment / Hosting

Jika Anda ingin meng-host NEXPHYRIX di server Anda sendiri (Apache / Nginx) atau GitHub Pages:

- **GitHub Pages**: Sangat direkomendasikan. GitHub Pages secara otomatis mengatur ekstensi `.appcache` dengan MIME Type yang benar (`text/cache-manifest`).
- **Apache Web Server**: Pastikan `mod_headers` dan `mod_deflate` aktif. Secara default, pengaturan MIME Type sudah ada di dalam file `.htaccess`.

> **Catatan untuk Developer**: Jika Anda memodifikasi file JavaScript atau HTML, Anda **wajib** memperbarui nomor build (misal: `# build v1.2`) di dalam file `cache.appcache`. Jika tidak, PS4 pengguna tidak akan menyadari adanya pembaruan dan akan terus memuat file cache yang lama.

---

<div align="center">
  <p>© 2026 NEXPHYRIX | DAENG 17PlayBox</p>
</div>
