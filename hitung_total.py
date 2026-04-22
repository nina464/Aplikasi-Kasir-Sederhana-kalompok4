def hitung_total_belanja(daftar_barang):
    total = 0
    for barang in daftar_barang:
        total += barang['harga']
    return total

def cari_terbanyak(daftar_barang):
    tertinggi = daftar_barang[0]
    
    for barang in daftar_barang:
        if barang["harga"] > tertinggi["harga"]:
            tertinggi = barang
            
    return tertinggi

def hitung_rata_rata(daftar_barang):
    total = hitung_total_belanja(daftar_barang)
    rata = total / len(daftar_barang)
    return rata