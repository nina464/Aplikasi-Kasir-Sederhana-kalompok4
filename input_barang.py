def input_nama_pembeli():
    return input("Masukkan nama pembeli: ")

def input_nama_barang_dan_harga():
    daftar_barang = []
    # Loop untuk 3 barang sesuai ketentuan
    for i in range(1, 4):
        nama = input(f"Masukkan nama barang ke-{i}: ")
        harga = int(input(f"Masukkan harga {nama}: "))
        daftar_barang.append({"nama": nama, "harga": harga})
    return daftar_barang