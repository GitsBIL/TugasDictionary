# Inisialisasi dictionary untuk daftar kontak
kontak = {}

def tampilkan_menu():
    print("\n" + "=" * 40)
    print("         MENU UTAMA - DAFTAR KONTAK         ")
    print("=" * 40)
    print("[1] Tambah kontak")
    print("[2] Ubah kontak")
    print("[3] Hapus kontak")
    print("[4] Tampilkan kontak tertentu")
    print("[5] Tampilkan semua nama")
    print("[6] Tampilkan semua nomor")
    print("[7] Tampilkan semua nama dan nomor")
    print("[8] Keluar")
    print("=" * 40)

def tambah_kontak():
    nama = input("Masukkan nama kontak: ").strip()
    nomor = input("Masukkan nomor telepon: ").strip()
    if nama in kontak:
        print(f"Kontak '{nama}' sudah ada.")
    else:
        kontak[nama] = nomor
        print(f"Kontak '{nama}' berhasil ditambahkan.")

def ubah_kontak():
    nama = input("Masukkan nama kontak yang ingin diubah: ").strip()
    if nama in kontak:
        nomor = input("Masukkan nomor telepon baru: ").strip()
        kontak[nama] = nomor
        print(f"Kontak '{nama}' berhasil diubah.")
    else:
        print(f"Kontak '{nama}' tidak ditemukan.")

def hapus_kontak():
    nama = input("Masukkan nama kontak yang ingin dihapus: ").strip()
    if nama in kontak:
        del kontak[nama]
        print(f"Kontak '{nama}' berhasil dihapus.")
    else:
        print(f"Kontak '{nama}' tidak ditemukan.")

def tampilkan_kontak_tertentu():
    nama = input("Masukkan nama kontak yang ingin ditampilkan: ").strip()
    if nama in kontak:
        print(f"Nama: {nama}\nNomor: {kontak[nama]}")
    else:
        print(f"Kontak '{nama}' tidak ditemukan.")

def tampilkan_semua_nama():
    if kontak:
        print("Daftar Nama Kontak:")
        for nama in kontak:
            print(f"- {nama}")
    else:
        print("Tidak ada kontak tersimpan.")

def tampilkan_semua_nomor():
    if kontak:
        print("Daftar Nomor Telepon:")
        for nomor in kontak.values():
            print(f"- {nomor}")
    else:
        print("Tidak ada kontak tersimpan.")

def tampilkan_semua_kontak():
    if kontak:
        print("\n" + "=" * 40)
        print("         DAFTAR KONTAK TERSIMPAN         ")
        print("=" * 40)
        print("{:<15} | {:<15}".format("Nama", "Nomor Telepon"))
        print("-" * 40)
        for nama, nomor in kontak.items():
            print("{:<15} | {:<15}".format(nama, nomor))
        print("=" * 40)
    else:
        print("\nTidak ada kontak tersimpan.")

# Program Utama
while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-8): ").strip()

    if pilihan == "1":
        tambah_kontak()
    elif pilihan == "2":
        ubah_kontak()
    elif pilihan == "3":
        hapus_kontak()
    elif pilihan == "4":
        tampilkan_kontak_tertentu()
    elif pilihan == "5":
        tampilkan_semua_nama()
    elif pilihan == "6":
        tampilkan_semua_nomor()
    elif pilihan == "7":
        tampilkan_semua_kontak()
    elif pilihan == "8":
        print("\nTerima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
