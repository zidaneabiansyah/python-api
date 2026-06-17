from itertools import chain, cycle, product, permutations, combinations, count, repeat, groupby

# 1. chain — gabung multiple iterable

print("CHAIN")
a = [1, 2, 3]
b = [4, 5, 6]
c = "abc"

gabung = list(chain(a, b, c))
print(f"chain: {gabung}")

# 2. cycle — loop terus menerus

print("\nCYCLE")
warna = cycle(["merah", "kuning", "hijau"])
for i, w in enumerate(warna):
    if i >= 5:
        break
    print(f"  {i}: {w}")

# 3. product — semua kombinasi (cartesian product)

print("\nPRODUCT")
buah = ["apel", "mangga"]
ukuran = ["kecil", "besar"]
hasil = list(product(buah, ukuran))
print(f"product: {hasil}")

# dengan repeat
print(f"product repeat 2: {list(product([1, 2], repeat=2))}")

# 4. permutations — semua urutan yang mungkin

print("\nPERMUTATIONS")
for p in permutations("ABC", 2):
    print(f"  {p}")

# 5. combinations — semua kombinasi (tanpa urutan)

print("\nCOMBINATIONS")
for c in combinations("ABC", 2):
    print(f"  {c}")

# 6. count — counter tak terbatas

print("\nCOUNT")
for i in count(5, 3):
    if i > 15:
        break
    print(f"  {i}")

# 7. repeat — ulang value

print(f"\nREPEAT: {list(repeat('halo', 3))}")

# 8. groupby — kelompokkan data berurutan

print("\nGROUPBY")
data = [("A", 1), ("A", 2), ("B", 3), ("B", 4)]
for key, group in groupby(data, key=lambda x: x[0]):
    print(f"  {key}: {list(group)}")

# CONTOH NYATA — generate semua kombinasi password

print("\nCONTOH NYATA")
angka = [0, 1, 2]
pin_3_digit = list(product(angka, repeat=3))
print(f"kemungkinan PIN 3 digit: {len(pin_3_digit)}")
print(f"5 pertama: {pin_3_digit[:5]}")

# jadwal turnamen
tim = ["MU", "ARS", "CHE"]
jadwal = list(combinations(tim, 2))
print(f"\njadwal pertandingan: {jadwal}")
