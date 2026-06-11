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


# 8. CLOSURE

def buat_counter():
    counter = 0

    def increment():
        nonlocal counter
        counter += 1
        return counter

    return increment


# 9. LAMBDA / ANONYMOUS FUNCTION

kali = lambda a, b: a + b  # ga usah dipake, cuma contoh
kali = lambda a, b: a * b


# 10. DECORATOR — fungsi yang membungkus fungsi lain

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Memanggil {func.__name__} dengan {args} {kwargs}")
        hasil = func(*args, **kwargs)
        print(f"Hasil: {hasil}")
        return hasil

    return wrapper


@logger
def luas_lingkaran(r: float) -> float:
    return 3.14 * r * r


# 11. GENERATOR — fungsi yang yield

def counter_atas(maks: int):
    n = 0
    while n <= maks:
        yield n
        n += 1


# 12. TYPE HINT DENGAN UNION

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

    print("\nCLOSURE")
    counter1 = buat_counter()
    print(f"Counter 1: {counter1()}")
    print(f"Counter 1: {counter1()}")
    counter2 = buat_counter()
    print(f"Counter 2: {counter2()}")
    print(f"Counter 1 lagi: {counter1()}")

    print("\nDECORATOR")
    print(f"Luas lingkaran r=7: {luas_lingkaran(7)}")

    print("\nGENERATOR")
    for val in counter_atas(3):
        print(f"Counter: {val}")

    print("\nTYPE HINT")
    siswa = cari_siswa("Budi")
    if siswa:
        print(f"Budi: {siswa}")
    siswa = cari_siswa("Eko")
    if siswa is None:
        print("Eko tidak ditemukan")


if __name__ == "__main__":
    main()
