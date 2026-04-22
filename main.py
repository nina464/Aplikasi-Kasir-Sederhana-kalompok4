import input_barang
import hitung_total

def main():
    print("=== APLIKASI KASIR SEDERHANA ===\n")

    nama = input_barang.input_nama_pembeli()
    list_belanja = input_barang.input_nama_barang_dan_harga()

    total_bayar = hitung_total.hitung_total_belanja(list_belanja)
    barang_tertinggi = hitung_total.cari_terbanyak(list_belanja)
    print(f"BARANG TERMAHAL : {barang_tertinggi['nama']} (Rp {barang_tertinggi['harga']})")

    print("\n" + "="*30)
    print("       STRUK PEMBAYARAN")
    print("="*30)
    print(f"Nama Pembeli : {nama}")
    print("-" * 30)
    
    for barang in list_belanja:
        print(f"{barang['nama']:<15} : Rp {barang['harga']:>10}")
    
    print("-" * 30)
    print(f"TOTAL BELANJA   : Rp {total_bayar:>10}")
    print("="*30)
    print("      Terima Kasih!")

if __name__ == "__main__":
    main()