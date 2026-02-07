from abc import ABC, abstractmethod

# =========================
# ABSTRACT CLASS (Blueprint)
# =========================
class BarangElektronik(ABC):
    def __init__(self, nama, harga_dasar):
        self.nama = nama
        self.__stok = 0                # private
        self.__harga_dasar = harga_dasar  # private

    # Getter stok
    def get_stok(self):
        return self.__stok

    # Method untuk menambah stok (Setter dengan validasi)
    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
        else:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.nama}: {jumlah} unit.")

    # Getter harga dasar (dipakai anak class)
    def _get_harga_dasar(self):
        return self.__harga_dasar

    # Abstract methods (KONTRAK)
    @abstractmethod
    def tampilkan_detail(self, jumlah):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass


# =========================
# CHILD CLASS: LAPTOP
# =========================
class Laptop(BarangElektronik):
    def __init__(self, nama, harga_dasar, processor):
        super().__init__(nama, harga_dasar)
        self.processor = processor

    def hitung_harga_total(self, jumlah):
        pajak = 0.10 * self._get_harga_dasar()
        return (self._get_harga_dasar() + pajak) * jumlah

    def tampilkan_detail(self, jumlah):
        pajak = 0.10 * self._get_harga_dasar()
        print(f"[LAPTOP] {self.nama} | Proc: {self.processor}")
        print(f"Harga Dasar: Rp {self._get_harga_dasar():,} | Pajak(10%): Rp {int(pajak):,}")
        print(f"Beli: {jumlah} unit | Subtotal: Rp {int(self.hitung_harga_total(jumlah)):,}\n")


# =========================
# CHILD CLASS: SMARTPHONE
# =========================
class Smartphone(BarangElektronik):
    def __init__(self, nama, harga_dasar, kamera):
        super().__init__(nama, harga_dasar)
        self.kamera = kamera

    def hitung_harga_total(self, jumlah):
        pajak = 0.05 * self._get_harga_dasar()
        return (self._get_harga_dasar() + pajak) * jumlah

    def tampilkan_detail(self, jumlah):
        pajak = 0.05 * self._get_harga_dasar()
        print(f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}")
        print(f"Harga Dasar: Rp {self._get_harga_dasar():,} | Pajak(5%): Rp {int(pajak):,}")
        print(f"Beli: {jumlah} unit | Subtotal: Rp {int(self.hitung_harga_total(jumlah)):,}\n")


# =========================
# POLYMORPHISM: TRANSAKSI
# =========================
def proses_transaksi(daftar_barang):
    print("\n--- STRUK TRANSAKSI ---")
    total = 0
    nomor = 1
    for barang, jumlah in daftar_barang:
        print(f"{nomor}. ", end="")
        barang.tampilkan_detail(jumlah)
        total += barang.hitung_harga_total(jumlah)
        nomor += 1

    print("----------------------------------------")
    print(f"TOTAL TAGIHAN: Rp {int(total):,}")
    print("----------------------------------------")


# =========================
# MAIN PROGRAM (USER STORY)
# =========================
print("--- SETUP DATA ---")

laptop1 = Laptop("ROG Zephyrus", 20_000_000, "Ryzen 9")
hp1 = Smartphone("iPhone 13", 15_000_000, "12MP")

laptop1.tambah_stok(10)
hp1.tambah_stok(-5)
hp1.tambah_stok(20)

keranjang = [
    (laptop1, 2),
    (hp1, 1)
]

proses_transaksi(keranjang)
