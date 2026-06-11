# 1. VARIABEL DAN TIPE DATA

nama: str = "Budi"
umur: int = 25
tinggi: float = 170.5
menikah: bool = False

print("VARIABEL DAN TIPE DATA")
print(f"Nama: {nama} | Umur: {umur} | Tinggi: {tinggi} | Menikah: {menikah}")

# type inference — Python otomatis nebak tipe
pekerjaan = "Programmer"
kota = "Jakarta"
print(f"Pekerjaan: {pekerjaan} | Kota: {kota}")

# tipe data lain
inisial: str = "B"
angka_besar: int = 1_000_000
print(f"Inisial: {inisial} | Angka besar: {angka_besar}")

# konversi tipe
umur_str = str(umur)
tinggi_int = int(tinggi)
print(f"Umur (str): {umur_str} | Tinggi (int): {tinggi_int}")

# None / null
alamat: None = None
print(f"Alamat: {alamat}")

# 2. PERCABANGAN (if-elif-else)

print("\nPERCABANGAN")

nilai = 85

if nilai >= 90:
    print("Grade: A")
elif nilai >= 75:
    print("Grade: B")
elif nilai >= 60:
    print("Grade: C")
else:
    print("Grade: D")

# ternary / conditional expression
status = "Dewasa" if umur >= 17 else "Anak-anak"
print(f"Status: {status}")

# match-case (switch versi Python 3.10+)
print("\nMatch-case:")
match nilai:
    case n if 90 <= n <= 100:
        print("A")
    case n if 75 <= n <= 89:
        print("B")
    case n if 60 <= n <= 74:
        print("C")
    case _:
        print("D")

# 3. PERULANGAN (for, while)

print("\nPERULANGAN")

# for range
print("For range:")
for i in range(5):
    print(f"Iterasi ke-{i}")

# for range dengan start, stop, step
print("\nFor range (1-10, step 2):")
for i in range(1, 10, 2):
    print(i)

# for iterasi list
print("\nFor iterasi list:")
buah = ["Apel", "Mangga", "Jeruk"]
for item in buah:
    print(f"Buah: {item}")

# for dengan index (enumerate)
print("\nFor dengan index:")
for index, value in enumerate(buah):
    print(f"Index {index}: {value}")

# while
print("\nWhile:")
hitungan = 0
while hitungan < 3:
    print(f"Hitungan: {hitungan}")
    hitungan += 1

# break & continue
print("\nBreak & Continue:")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    if i > 7:
        break
    print(f"Bilangan ganjil: {i}")
