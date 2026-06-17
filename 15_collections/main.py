from collections import namedtuple, defaultdict, Counter, deque

# 1. namedtuple — tuple dengan nama field

Mahasiswa = namedtuple("Mahasiswa", ["nama", "umur", "jurusan"])
mhs = Mahasiswa("Budi", 20, "Informatika")

print("NAMEDTUPLE")
print(f"pake index: {mhs[0]}")
print(f"pake nama: {mhs.nama}")
print(f"semua: {mhs}")

# unpacking
nama, umur, jurusan = mhs
print(f"unpack: {nama} - {umur} - {jurusan}")

# 2. defaultdict — dict dengan default value

print("\nDEFAULTDICT")

# biasa -> KeyError kalo key ga ada
# defaultdict -> otomatis bikin default

# list default
kelompok = defaultdict(list)
kelompok["A"].append("Budi")
kelompok["A"].append("Andi")
kelompok["B"].append("Siti")

print(f"kelompok A: {kelompok['A']}")
print(f"kelompok B: {kelompok['B']}")
print(f"kelompok C (otomatis): {kelompok['C']}")

# int default (buat counter manual)
hitung = defaultdict(int)
for huruf in "python programming":
    hitung[huruf] += 1
print(f"hitung huruf: {dict(hitung)}")

# 3. Counter — hitung frekuensi otomatis

print("\nCOUNTER")

warna = ["merah", "biru", "merah", "hijau", "biru", "merah"]
cnt = Counter(warna)
print(f"counter: {cnt}")
print(f"paling umum: {cnt.most_common(2)}")

# counter dari string
cnt2 = Counter("aabbcccddddeeeee")
print(f"counter string: {cnt2}")
print(f"3 most common: {cnt2.most_common(3)}")

# operasi counter
a = Counter(["a", "b", "c", "a"])
b = Counter(["a", "b", "b", "d"])
print(f"a + b: {a + b}")
print(f"a - b: {a - b}")

# 4. deque — antrian double-ended

print("\nDEQUE")

q = deque(["a", "b", "c"])
print(f"deque: {q}")

q.append("d")
q.appendleft("z")
print(f"append & appendleft: {q}")

q.pop()
q.popleft()
print(f"pop & popleft: {q}")

# rotate — putar isi
q2 = deque(range(5))
print(f"\nsebelum rotate: {list(q2)}")
q2.rotate(2)
print(f"rotate 2: {list(q2)}")
q2.rotate(-1)
print(f"rotate -1: {list(q2)}")

# maxlen — batas maksimum
q3 = deque(maxlen=3)
for i in range(5):
    q3.append(i)
    print(f"append {i}: {list(q3)}")
