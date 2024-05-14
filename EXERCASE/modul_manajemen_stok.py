# Variabel global untuk menyimpan data barang
data_barang = {}

# Fungsi untuk menambahkan data barang
def tambah_data_barang(nama_barang, stok_barang):
    data_barang[nama_barang] = stok_barang
    print("Data barang berhasil ditambahkan.")

# Fungsi untuk menghapus data barang
def hapus_data_barang(nama_barang):
    if nama_barang in data_barang:
        del data_barang[nama_barang]
        print("Data barang berhasil dihapus.")
    else:
        print("Data barang tidak ditemukan.")

# Fungsi untuk menampilkan data barang
def tampilkan_data_barang():
    if data_barang:
        print("Data barang:")
        for nama_barang, stok_barang in data_barang.items():
            print(f"{nama_barang}: {stok_barang}")
    else:
        print("Tidak ada data barang yang tersimpan.")

# Jika file ini dijalankan langsung
if __name__ == "__main__":
    print("Ini adalah modul untuk manajemen stok barang.")
