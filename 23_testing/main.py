# 1. FUNGSI YANG AKAN DITEST

def tambah(a: int, b: int) -> int:
    return a + b

def kurang(a: int, b: int) -> int:
    return a - b

def kali(a: int, b: int) -> int:
    return a * b

def bagi(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Tidak bisa membagi dengan nol")
    return a / b

def cek_genap(angka: int) -> bool:
    return angka % 2 == 0

def sapa(nama: str) -> str:
    if not nama:
        raise ValueError("Nama tidak boleh kosong")
    return f"Halo, {nama}!"

class Kalkulator:
    def __init__(self):
        self.riwayat = []

    def tambah(self, a: int, b: int) -> int:
        hasil = a + b
        self.riwayat.append(f"{a} + {b} = {hasil}")
        return hasil

    def reset(self):
        self.riwayat = []
        return True

# 2. CONTOH UNTESTED CODE

if __name__ == "__main__":
    print("Fungsi siap untuk ditest!")
    print(f"5 + 3 = {tambah(5, 3)}")
    print(f"10 - 4 = {kurang(10, 4)}")
