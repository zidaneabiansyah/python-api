# 1. map — apply function ke setiap item

angka = [1, 2, 3, 4, 5]
kuadrat = list(map(lambda x: x**2, angka))
print(f"map kuadrat: {kuadrat}")

def kali_dua(x):
    return x * 2

hasil = list(map(kali_dua, angka))
print(f"map kali_dua: {hasil}")

# map dengan multiple iterable
a = [1, 2, 3]
b = [4, 5, 6]
jumlah = list(map(lambda x, y: x + y, a, b))
print(f"map dua list: {jumlah}")

# 2. filter — ambil item yang memenuhi kondisi

genap = list(filter(lambda x: x % 2 == 0, angka))
print(f"filter genap: {genap}")

panjang = ["a", "ab", "abc", "abcd", "abcde"]
lebih_dari_2 = list(filter(lambda x: len(x) > 2, panjang))
print(f"filter len>2: {lebih_dari_2}")

# 3. zip — menggabungkan multiple iterable

nama = ["Budi", "Andi", "Siti"]
umur = [25, 30, 22]
gabung = list(zip(nama, umur))
print(f"zip: {gabung}")

for n, u in gabung:
    print(f"  {n} berumur {u}")

# zip dengan panjang berbeda (kelebihan diabaikan)
nilai = [85, 90]
gabung2 = list(zip(nama, umur, nilai))
print(f"zip 3 list: {gabung2}")

# unzip
data = [("Budi", 25), ("Andi", 30)]
nama2, umur2 = zip(*data)
print(f"unzip nama: {nama2}, umur: {umur2}")

# 4. any & all

nilai_bool = [True, False, True]
print(f"any: {any(nilai_bool)}")
print(f"all: {all(nilai_bool)}")

# contoh praktis
angka2 = [1, 3, 5, 7]
print(f"ada genap? {any(x % 2 == 0 for x in angka2)}")
print(f"semua ganjil? {all(x % 2 == 1 for x in angka2)}")

# 5. sorted — sorting tanpa modify original

murid = [
    {"nama": "Budi", "nilai": 85},
    {"nama": "Andi", "nilai": 90},
    {"nama": "Siti", "nilai": 75},
]

by_nilai = sorted(murid, key=lambda x: x["nilai"])
print(f"sorted by nilai: {by_nilai}")

by_nilai_desc = sorted(murid, key=lambda x: x["nilai"], reverse=True)
print(f"sorted desc: {by_nilai_desc}")

# sorted pada string
print(f"sorted string: {sorted('python')}")

# 6. enumerate (sudah di 01_dasar, tapi sekedar pengingat)

buah = ["apel", "mangga", "jeruk"]
for i, b in enumerate(buah, start=1):
    print(f"  {i}. {b}")
