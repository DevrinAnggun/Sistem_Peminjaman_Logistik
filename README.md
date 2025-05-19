# 📦 Sistem Peminjaman Logistik
Sistem ini digunakan untuk memudahkan pengelolaan peminjaman barang dan ruangan di sebuah organisasi atau instansi. Sistem ini berbasis CLI (Command Line Interface) yang memanfaatkan Python dan menyimpan data peminjaman secara digital menggunakan file JSON.

# ✨ Fitur-Fitur Sistem Peminjaman Logistik
📋 Lihat Daftar Ruangan dan Barang

Menampilkan daftar ruangan yang tersedia serta daftar barang yang bisa dipinjam.

➕ Peminjaman Logistik

Memungkinkan peminjam untuk memilih jenis logistik yang akan dipinjam, baik barang maupun ruangan. Peminjam harus mengisi nama, organisasi asal, serta jaminan KTM. Data peminjaman akan otomatis tercatat dengan tanggal pinjam dan tanggal kembali (3 hari dari tanggal pinjam).

🔍 Cek Status Peminjaman

Menampilkan status terkini dari semua peminjaman yang tercatat, apakah sudah dikembalikan atau belum, lengkap dengan detail tanggal pinjam dan tanggal kembali.

🔄 Pengembalian Logistik

Mencatat pengembalian logistik berdasarkan nama peminjam. Jika data peminjaman ditemukan dan masih aktif, statusnya akan diubah menjadi "Sudah Dikembalikan".

📜 Riwayat Peminjaman

Menampilkan seluruh riwayat peminjaman, baik yang sudah dikembalikan maupun yang masih aktif, untuk keperluan monitoring dan pelaporan.

🚪 Keluar dari Program

Menutup aplikasi CLI dengan aman.

# 🛠️ Tools dan Teknologi yang Digunakan
- Python
- Modul json untuk menyimpan dan memuat data peminjaman
- Modul os untuk pengecekan file
- Modul datetime untuk mengatur tanggal peminjaman dan pengembalian
- Library tabulate untuk menampilkan tabel data secara rapi di CLI
- Data disimpan dalam format JSON di file data_peminjaman.json
