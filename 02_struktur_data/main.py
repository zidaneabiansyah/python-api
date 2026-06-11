# 1. LIST — mutable, ordered

print("LIST")

buah = ["Apel", "Mangga", "Jeruk"]
print(f"List: {buah}")
print(f"Panjang: {len(buah)}")
print(f"Index 0: {buah[0]}")
print(f"Index -1: {buah[-1]}")

# slicing
print(f"Slicing [1:]: {buah[1:]}")
print(f"Slicing [0:2]: {buah[0:2]}")

# modify
buah[1] = "Anggur"
print(f"Setelah diubah: {buah}")

# method
buah.append("Pisang")
print(f"Setelah append: {buah}")
buah.insert(1, "Melon")
print(f"Setelah insert: {buah}")
buah.remove("Apel")
print(f"Setelah remove 'Apel': {buah}")
pop = buah.pop()
print(f"Pop: {pop} | Sisa: {buah}")

# sorting
angka = [5, 2, 8, 1, 9]
angka.sort()
print(f"Sort: {angka}")
angka.sort(reverse=True)
print(f"Reverse sort: {angka}")

# nested list
matrix = [[1, 2], [3, 4], [5, 6]]
print(f"Matrix: {matrix}")
print(f"Matrix[1][0]: {matrix[1][0]}")

# list comprehension
kuadrat = [x**2 for x in range(5)]
print(f"List comprehension: {kuadrat}")

# 2. TUPLE — immutable, ordered

print("\nTUPLE")

orang = ("Budi", 25, 170.5)
print(f"Tuple: {orang}")
print(f"Nama: {orang[0]}, Umur: {orang[1]}, Tinggi: {orang[2]}")

# unpacking
nama, umur, tinggi = orang
print(f"Destructure: {nama} {umur} {tinggi}")

# tuple tidak bisa diubah
# orang[0] = "Andi"  # ERROR

# single element tuple
satu = (5,)
print(f"Single tuple: {satu}")

# 3. DICT — key-value, mutable

print("\nDICT")

siswa = {
    "nama": "Budi",
    "umur": 25,
    "kelas": "A",
}
print(f"Dict: {siswa}")
print(f"Nama: {siswa['nama']}")
print(f"Umur: {siswa.get('umur')}")

# modify
siswa["umur"] = 26
siswa["alamat"] = "Jakarta"
print(f"Setelah diubah: {siswa}")

# keys, values, items
print(f"Keys: {list(siswa.keys())}")
print(f"Values: {list(siswa.values())}")
print(f"Items: {list(siswa.items())}")

# iterasi
for key, value in siswa.items():
    print(f"  {key}: {value}")

# dict comprehension
kuadrat_dict = {x: x**2 for x in range(5)}
print(f"Dict comprehension: {kuadrat_dict}")

# nested dict
kelas = {
    "siswa1": {"nama": "Budi", "nilai": 85},
    "siswa2": {"nama": "Andi", "nilai": 90},
}
print(f"Nested dict: {kelas}")
print(f"Siswa1 nama: {kelas['siswa1']['nama']}")

# 4. SET — unique, unordered

print("\nSET")

angka_set = {1, 2, 3, 4, 5, 2, 3}
print(f"Set: {angka_set}")

# operasi set
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(f"Union: {a | b}")
print(f"Intersection: {a & b}")
print(f"Difference: {a - b}")
print(f"Symmetric diff: {a ^ b}")

# method
a.add(9)
print(f"Setelah add 9: {a}")
a.remove(9)
print(f"Setelah remove 9: {a}")
