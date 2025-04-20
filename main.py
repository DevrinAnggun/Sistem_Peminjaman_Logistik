import json
import os
from datetime import datetime, timedelta
from tabulate import tabulate

DATA_FILE = 'data_peminjaman.json'

ruangan = [
    "REK-201", "REK-202", "REK-203",
    "IOT-201", "IOT-202", "IOT-204",
    "DSP-201", "DSP-202", "DSP-203",
    "DC-201", "DC-202", "DC-203",
    "AULA REKTORAT"
]

barang = ["microphone", "bendera", "kursi dan meja", "kabel"]

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def view_ruangan_barang():
    print("\n[Daftar Ruangan]")
    for i in range(0, len(ruangan), 4):
        print(" | ".join(f"{r:<13}" for r in ruangan[i:i+4]))

    print("\n[Daftar Barang]")
    for i in range(0, len(barang), 2):
        print(" | ".join(f"{b:<15}" for b in barang[i:i+2]))

def pilih_jenis():
    print("\n1. Pinjam Barang")
    print("2. Pinjam Ruangan")
    while True:
        try:
            pilihan = int(input("Pilih jenis logistik (1/2): "))
            if pilihan == 1:
                return 'barang'
            elif pilihan == 2:
                return 'ruangan'
            else:
                print("[!] Pilihan tidak valid.")
        except ValueError:
            print("[!] Masukkan angka 1 atau 2.")

def borrow_logistik():
    jenis = pilih_jenis()
    if jenis == 'barang':
        print("\n[Daftar Barang]")
        for i, b in enumerate(barang, 1):
            print(f"{i}. {b}")
        pilihan = int(input("Pilih barang: "))
        item = barang[pilihan-1]
    else:
        print("\n[Daftar Ruangan]")
        for i, r in enumerate(ruangan, 1):
            print(f"{i}. {r}")
        pilihan = int(input("Pilih ruangan: "))
        item = ruangan[pilihan-1]

    jaminan = input("Jaminan KTM (Y/N): ").strip().upper()
    nama = input("Masukkan nama peminjam: ").strip()
    organisasi = input("Masukkan asal organisasi: ").strip()

    sekarang = datetime.now()
    kembali = sekarang + timedelta(days=3)

    data = load_data()
    data.append({
        'nama': nama,
        'organisasi': organisasi,
        'item': item,
        'jenis': jenis,
        'jaminan': jaminan,
        'tanggal_pinjam': sekarang.strftime('%Y-%m-%d %H:%M:%S'),
        'tanggal_kembali': kembali.strftime('%Y-%m-%d %H:%M:%S'),
        'status': 'Belum Dikembalikan'
    })
    save_data(data)
    print("[✔] Peminjaman berhasil dicatat!\n")

def cek_status():
    data = load_data()
    if not data:
        print("[!] Tidak ada data peminjaman.")
        return

    headers = ["Nama", "Item", "Jenis", "Tanggal Pinjam", "Tanggal Kembali", "Status"]
    tabel = [[
        d['nama'],
        d['item'],
        d['jenis'],
        d['tanggal_pinjam'],
        d['tanggal_kembali'],
        d['status']
    ] for d in data]
    print(tabulate(tabel, headers=headers, tablefmt="grid"))

def return_logistik():
    nama = input("Masukkan nama peminjam untuk pengembalian: ").strip()
    data = load_data()
    ditemukan = False
    for entry in data:
        if entry['nama'].lower() == nama.lower() and entry['status'] == 'Belum Dikembalikan':
            entry['status'] = 'Sudah Dikembalikan'
            ditemukan = True
            print(f"[✔] Pengembalian dicatat: {entry['item']} ({entry['jenis']})")
    if not ditemukan:
        print("[!] Tidak ditemukan peminjaman aktif atas nama tersebut.")
    save_data(data)

def view_riwayat():
    data = load_data()
    if not data:
        print("[!] Belum ada riwayat peminjaman.")
        return

    headers = ["Nama", "Item", "Jenis", "Tanggal Pinjam", "Tanggal Kembali", "Status"]
    tabel = [[
        d['nama'],
        d['item'],
        d['jenis'],
        d['tanggal_pinjam'],
        d['tanggal_kembali'],
        d['status']
    ] for d in data]
    print(tabulate(tabel, headers=headers, tablefmt="grid"))

def main():
    while True:
        print("\n--- Sistem Peminjaman Logistik ---")
        print("1. Lihat Ruangan dan Barang")
        print("2. Peminjaman Logistik")
        print("3. Cek Status Peminjaman")
        print("4. Pengembalian Logistik")
        print("5. Riwayat Peminjaman")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")

        menu = {
            '1': view_ruangan_barang,
            '2': borrow_logistik,
            '3': cek_status,
            '4': return_logistik,
            '5': view_riwayat,
            '0': exit
        }
        menu.get(pilihan, lambda: print("[!] Pilihan tidak valid."))()

if __name__ == '__main__':
    main()