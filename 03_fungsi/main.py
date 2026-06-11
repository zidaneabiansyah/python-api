# 1. FUNGSI SEDERHANA

def sapa():
    print("Halo, selamat belajar Python!")


def sapa_orang(nama: str):
    print(f"Halo {nama}, selamat belajar Python!")


def tambah(a: int, b: int) -> int:
    return a + b


def kurang(a: int, b: int) -> int:
    return a - b


# 2. MULTIPLE RETURN VALUE

def bagi(a: int, b: int):
    if b == 0:
        return 0, "tidak bisa membagi dengan nol"
    return a // b, None


# 3. DEFAULT PARAMETER

def pangkat(angka: int, eksponen: int = 2) -> int:
    return angka**eksponen


# 4. NAMED ARGUMENT / KEYWORD ARGUMENT

def perkenalan(nama: str, umur: int, kota: str = "Jakarta"):
    print(f"Halo, nama saya {nama}, {umur} tahun, dari {kota}")


# 5. VARIADIC FUNCTION (*args)

def jumlah_angka(*angka: int) -> int:
    return sum(angka)


# 6. KEYWORD VARIADIC (**kwargs)

def tampilkan_data(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


# 7. FUNGSI SEBAGAI VALUE

def operasi_matematika(a: int, b: int, op):
    return op(a, b)


# 8. LAMBDA / ANONYMOUS FUNCTION

kali = lambda a, b: a * b


# 9. TYPE HINT DENGAN OPTIONAL

from typing import Optional


def cari_siswa(nama: str) -> Optional[dict]:
    data = {"Budi": {"umur": 25}, "Andi": {"umur": 30}}
    return data.get(nama)


# MAIN
def main():
    print("FUNGSI SEDERHANA")
    sapa()
    sapa_orang("Budi")

    hasil_tambah = tambah(10, 5)
    print(f"10 + 5 = {hasil_tambah}")

    hasil_kurang = kurang(10, 5)
    print(f"10 - 5 = {hasil_kurang}")

    print("\nMULTIPLE RETURN VALUE")
    hasil_1, err = bagi(10, 2)
    if err:
        print(f"Error: {err}")
    else:
        print(f"10 / 2 = {hasil_1}")

    _, err = bagi(10, 0)
    if err:
        print(f"Error: {err}")

    print("\nDEFAULT PARAMETER")
    print(f"3^2 = {pangkat(3)}")
    print(f"3^4 = {pangkat(3, 4)}")

    print("\nNAMED ARGUMENT")
    perkenalan("Budi", 25)
    perkenalan("Andi", 22, "Bandung")
    perkenalan(umur=30, nama="Siti", kota="Surabaya")

    print("\nVARIADIC FUNCTION (*args)")
    print(f"Jumlah: {jumlah_angka(1, 2, 3, 4, 5)}")
    print(f"Jumlah (kosong): {jumlah_angka()}")

    print("\nKEYWORD VARIADIC (**kwargs)")
    tampilkan_data(nama="Budi", umur=25, kota="Jakarta")

    print("\nFUNGSI SEBAGAI VALUE")
    hasil = operasi_matematika(6, 7, lambda a, b: a * b)
    print(f"6 * 7 = {hasil}")
    print(f"10 / 5 = {operasi_matematika(10, 5, lambda a, b: a // b)}")

    print("\nLAMBDA")
    print(f"4 * 5 = {kali(4, 5)}")

    print("\nTYPE HINT")
    siswa = cari_siswa("Budi")
    if siswa:
        print(f"Budi: {siswa}")
    siswa = cari_siswa("Eko")
    if siswa is None:
        print("Eko tidak ditemukan")


if __name__ == "__main__":
    main()
