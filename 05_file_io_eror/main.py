# 1. FILE I/O — MENULIS FILE

print("MENULIS FILE")
with open("contoh.txt", "w") as f:
    f.write("Baris pertama\n")
    f.write("Baris kedua\n")

print("File contoh.txt berhasil dibuat")

# 2. FILE I/O — MEMBACA FILE

print("\nMEMBACA FILE")
with open("contoh.txt", "r") as f:
    isi = f.read()
print(f"Isi file:\n{isi}")

# 3. FILE I/O — READLINE & READLINES

print("READLINE & READLINES")
with open("contoh.txt", "r") as f:
    baris = f.readline()
    print(f"Readline: {baris.strip()}")

with open("contoh.txt", "r") as f:
    semua_baris = f.readlines()
    print(f"Readlines: {semua_baris}")

# 4. FILE I/O — APPEND

print("\nAPPEND KE FILE")
with open("contoh.txt", "a") as f:
    f.write("Baris ketiga (append)\n")

with open("contoh.txt", "r") as f:
    print(f.read())

# 5. FILE I/O — ITERASI FILE

print("ITERASI FILE")
with open("contoh.txt", "r") as f:
    for baris in f:
        print(f"  > {baris.strip()}")

# 6. ERROR HANDLING — TRY EXCEPT

print("\nTRY EXCEPT")
try:
    hasil = 10 / 0
    print(hasil)
except ZeroDivisionError:
    print("Error: tidak bisa membagi dengan nol")

# 7. MULTIPLE EXCEPT

print("\nMULTIPLE EXCEPT")
try:
    angka = int("bukan_angka")
except ValueError:
    print("Error: value tidak valid")
except ZeroDivisionError:
    print("Error: pembagian nol")

# 8. TRY EXCEPT ELSE FINALLY

print("\nTRY EXCEPT ELSE FINALLY")
try:
    angka = int("123")
except ValueError:
    print("Terjadi error")
else:
    print(f"Berhasil: {angka}")
finally:
    print("Blok finally selalu dijalankan")

# 9. RAISE EXCEPTION

print("\nRAISE EXCEPTION")


def cek_umur(umur):
    if umur < 0:
        raise ValueError("Umur tidak boleh negatif")
    if umur < 17:
        print("Belum dewasa")
    else:
        print("Sudah dewasa")


try:
    cek_umur(-5)
except ValueError as e:
    print(f"Error: {e}")

# 10. MENANGANI ERROR FILE

print("\nMENANGANI ERROR FILE")
try:
    with open("file_tidak_ada.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File tidak ditemukan")

# cleanup
import os
os.remove("contoh.txt")
print("\nFile contoh.txt dihapus")
