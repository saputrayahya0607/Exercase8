import modul_manajemen_stok

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("\nPilih menu:")
    print("1. Tambah Data Barang")
    print("2. Hapus Data Barang")
    print("3. Tampilkan Data Barang")
    print("4. Keluar")

# Program utama
def main():
    while True:
        tampilkan_menu()
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            nama_barang = input("Masukkan nama barang: ")
            stok_barang = int(input("Masukkan stok barang: "))
            modul_manajemen_stok.tambah_data_barang(nama_barang, stok_barang)
        elif pilihan == "2":
            nama_barang = input("Masukkan nama barang yang ingin dihapus: ")
            modul_manajemen_stok.hapus_data_barang(nama_barang)
        elif pilihan == "3":
            modul_manajemen_stok.tampilkan_data_barang()
        elif pilihan == "4":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()