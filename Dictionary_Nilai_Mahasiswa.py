def hitung_nilai_akhir(tugas, uts, uas):
    return (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)

def tampilkan_data():
    if not data_mahasiswa:
        print("\nDaftar Nilai Mahasiswa Kosong")
        return
    print("\nDaftar Nilai Mahasiswa:")
    print("="*77)
    print(f"| {'NIM':^10} | {'Nama':^15} | {'Tugas':^5} | {'UTS':^5} | {'UAS':^5} | {'Akhir':^7} |")
    print("="*77)
    for mahasiswa in data_mahasiswa:
        print(f"| {mahasiswa['NIM']:^10} | {mahasiswa['Nama']:^15} | {mahasiswa['Tugas']:^5} | {mahasiswa['UTS']:^5} | {mahasiswa['UAS']:^5} | {mahasiswa['Nilai Akhir']:^7.2f} |")
    print("="*77)

data_mahasiswa = []

while True:
    print("\nMenu:")
    print("[L]ihat, [T]ambah, [U]bah, [H]apus, [C]ari, [K]eluar")
    pilihan = input("Pilih menu: ").lower()

    if pilihan == "t": 
        print("\nTambah Data Mahasiswa")
        nim = input("Masukkan NIM Mahasiswa: ")
        nama = input("Masukkan Nama Mahasiswa: ")
        tugas = float(input("Masukkan Nilai Tugas: "))
        uts = float(input("Masukkan Nilai UTS: "))
        uas = float(input("Masukkan Nilai UAS: "))
        nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
        data_mahasiswa.append({
            "NIM": nim,
            "Nama": nama,
            "Tugas": tugas,
            "UTS": uts,
            "UAS": uas,
            "Nilai Akhir": nilai_akhir
        })
        print("Data berhasil ditambahkan!")

    elif pilihan == "u":
        nim = input("\nMasukkan NIM Mahasiswa yang ingin diubah: ")
        for mahasiswa in data_mahasiswa:
            if mahasiswa["NIM"] == nim:
                print("Data ditemukan. Silakan perbarui.")
                mahasiswa["Nama"] = input("Masukkan Nama Baru: ")
                mahasiswa["Tugas"] = float(input("Masukkan Nilai Tugas Baru: "))
                mahasiswa["UTS"] = float(input("Masukkan Nilai UTS Baru: "))
                mahasiswa["UAS"] = float(input("Masukkan Nilai UAS Baru: "))
                mahasiswa["Nilai Akhir"] = hitung_nilai_akhir(mahasiswa["Tugas"], mahasiswa["UTS"], mahasiswa["UAS"])
                print("Data berhasil diperbarui!")
                break
        else:
            print("Data dengan NIM tersebut tidak ditemukan.")

    elif pilihan == "h":
        nim = input("\nMasukkan NIM Mahasiswa yang ingin dihapus: ")
        for mahasiswa in data_mahasiswa:
            if mahasiswa["NIM"] == nim:
                data_mahasiswa.remove(mahasiswa)
                print("Data berhasil dihapus!")
                break
        else:
            print("Data dengan NIM tersebut tidak ditemukan.")

    elif pilihan == "l":
        tampilkan_data()

    elif pilihan == "c": 
        nim = input("\nMasukkan NIM Mahasiswa yang ingin dicari: ")
        for mahasiswa in data_mahasiswa:
            if mahasiswa["NIM"] == nim:
                print("\nData Mahasiswa:")
                print("="*77)
                print(f"| {'NIM':^10} | {'Nama':^15} | {'Tugas':^5} | {'UTS':^5} | {'UAS':^5} | {'Akhir':^7} |")
                print("="*77)
                print(f"| {mahasiswa['NIM']:^10} | {mahasiswa['Nama']:^15} | {mahasiswa['Tugas']:^5} | {mahasiswa['UTS']:^5} | {mahasiswa['UAS']:^5} | {mahasiswa['Nilai Akhir']:^7.2f} |")
                print("="*77)
                break
        else:
            print("Data dengan NIM tersebut tidak ditemukan.")

    elif pilihan == "k":
        print("Terima kasih telah menggunakan program ini!")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
