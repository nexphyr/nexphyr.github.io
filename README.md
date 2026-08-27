# NEXPHYRIX — PS4 Jailbreak Host

PS4 HEN exploit host dengan AppCache untuk offline caching.

## Cara pakai AppCache di PS4

1. Buka URL host via browser PS4 saat ada internet
2. Tunggu semua file selesai di-cache (biasanya 1–2 menit karena payload besar)
3. Setelah itu, exploit bisa dijalankan **tanpa internet**

## Hosting

Deploy ke GitHub Pages atau server Apache. Pastikan `.htaccess` aktif (Apache perlu `mod_headers` dan `mod_deflate`).

Jika pakai **GitHub Pages**, MIME type `.appcache` sudah otomatis benar.

## Versi

| Mode | Firmware |
|------|----------|
| v1 (PS4 HEN) | FW 6.20 – 11.02 |
| v2 (Lapse Chain) | FW 11.00 – 13.00 |
