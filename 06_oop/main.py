# 1. CLASS SEDERHANA

class Mobil:
    def __init__(self, merek, tahun):
        self.merek = merek
        self.tahun = tahun

    def info(self):
        print(f"Mobil {self.merek}, tahun {self.tahun}")


print("CLASS SEDERHANA")
mobil1 = Mobil("Toyota", 2020)
mobil1.info()

# 2. CLASS VARIABLE vs INSTANCE VARIABLE

class Siswa:
    sekolah = "SMA Negeri 1"

    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas


print("\nCLASS VARIABLE")
siswa1 = Siswa("Budi", "XII-A")
siswa2 = Siswa("Andi", "XII-B")
print(f"{siswa1.nama} - {siswa1.kelas} - {siswa1.sekolah}")
print(f"{siswa2.nama} - {siswa2.kelas} - {siswa2.sekolah}")

# 3. INHERITANCE

class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def bersuara(self):
        print("...")


class Kucing(Hewan):
    def bersuara(self):
        print("Meow!")


class Anjing(Hewan):
    def bersuara(self):
        print("Guk guk!")


print("\nINHERITANCE")
kucing = Kucing("Kitty")
anjing = Anjing("Doggy")
kucing.bersuara()
anjing.bersuara()

# 4. SUPER()

class Kendaraan:
    def __init__(self, merk, roda):
        self.merk = merk
        self.roda = roda

    def info(self):
        print(f"Merk: {self.merk}, Roda: {self.roda}")


class Motor(Kendaraan):
    def __init__(self, merk):
        super().__init__(merk, 2)

    def info(self):
        super().info()
        print("Ini adalah sepeda motor")


print("\nSUPER()")
motor = Motor("Honda")
motor.info()

# 5. DUNDER METHOD (__str__, __repr__, __len__)

class Buku:
    def __init__(self, judul, penulis, halaman):
        self.judul = judul
        self.penulis = penulis
        self.halaman = halaman

    def __str__(self):
        return f"{self.judul} oleh {self.penulis}"

    def __repr__(self):
        return f"Buku('{self.judul}', '{self.penulis}', {self.halaman})"

    def __len__(self):
        return self.halaman


print("\nDUNDER METHOD")
buku = Buku("Python 101", "Budi", 200)
print(str(buku))
print(repr(buku))
print(f"Jumlah halaman: {len(buku)}")

# 6. CLASSMETHOD & STATICMETHOD

class Kalkulator:
    counter = 0

    @classmethod
    def tambah_counter(cls):
        cls.counter += 1
        return cls.counter

    @staticmethod
    def tambah(a, b):
        return a + b


print("\nCLASSMETHOD & STATICMETHOD")
print(f"Static: 5 + 3 = {Kalkulator.tambah(5, 3)}")
print(f"Counter: {Kalkulator.tambah_counter()}")
print(f"Counter: {Kalkulator.tambah_counter()}")

# 7. PROPERTY DECORATOR

class Lingkaran:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, nilai):
        if nilai < 0:
            raise ValueError("Radius tidak boleh negatif")
        self._radius = nilai

    @property
    def luas(self):
        return 3.14 * self._radius**2


print("\nPROPERTY")
l = Lingkaran(7)
print(f"Radius: {l.radius}")
print(f"Luas: {l.luas}")
l.radius = 10
print(f"Radius baru: {l.radius}")
print(f"Luas baru: {l.luas}")
