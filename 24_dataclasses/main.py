"""
DATACLASSES & ATTRS
===================
 Python 3.7+ dataclasses mempermembuat class untuk data
 attrs adalah alternatif pihak ketiga dengan fitur lebih banyak
"""

from dataclasses import dataclass, field, asdict, astuple
from typing import List, Optional


# =============================================
# 1. DATACLASSES DASAR
# =============================================

# Tanpa dataclass (verbose)
class PointManual:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"PointManual(x={self.x}, y={self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


# Dengan dataclass (simpel!)
@dataclass
class Point:
    x: int
    y: int


print("DATACLASSES DASAR")
p1 = Point(5, 10)
p2 = Point(5, 10)
p3 = Point(3, 7)

print(f"p1: {p1}")  # Otomatis punya __repr__
print(f"p2: {p2}")
print(f"p1 == p2: {p1 == p2}")  # Otomatis punya __eq__
print(f"p1 == p3: {p1 == p3}")


# =============================================
# 2. FIELD OPTIONS
# =============================================

@dataclass
class Mahasiswa:
    nama: str
    umur: int
    jurusan: str = "Umum"  # Default value
    ipk: float = field(default=0.0)  # Dengan field()
    aktivitas: List[str] = field(default_factory=list)  # Mutable default


print("\nFIELD OPTIONS")
mhs = Mahasiswa("Budi", 20, "Informatika")
print(f"Nama: {mhs.nama}")
print(f"Jurusan: {mhs.jurusan}")
print(f"Aktivitas: {mhs.aktivitas}")

# Mutable default aman
mhs2 = Mahasiswa("Andi", 22)
mhs.aktivitas.append("Coding")
print(f"mhs aktivitas: {mhs.aktivitas}")
print(f"mhs2 aktivitas: {mhs2.aktivitas}")  # Tidak ikut terubah!


# =============================================
# 3. FIELD YANG TIDAK DI-REPR/COMPARE
# =============================================

@dataclass
class Config:
    host: str = "localhost"
    port: int = 8080
    _password: str = field(default="secret", repr=False, compare=False)


print("\nFIELD HIDDEN")
config = Config("example.com", 443, "mypassword")
print(f"Config: {config}")  # _password tidak muncul


# =============================================
# 4. FROZEN DATACLASS (Immutable)
# =============================================

@dataclass(frozen=True)
class Color:
    r: int
    g: int
    b: int


print("\nFROZEN DATACLASS")
merah = Color(255, 0, 0)
print(f"Color: {merah}")

# merah.r = 100  # Error! Tidak bisa diubah

# Bisa dijadikan dict key (hashable)
warna = {
    Color(255, 0, 0): "Merah",
    Color(0, 255, 0): "Hijau",
}
print(f"Dict lookup: {warna[Color(255, 0, 0)]}")


# =============================================
# 5. POST-INIT
# =============================================

@dataclass
class Suhu:
    celsius: float

    def __post_init__(self):
        if self.celsius < -273.15:
            raise ValueError("Suhu di bawah 0 absolut!")

    @property
    def fahrenheit(self) -> float:
        return self.celsius * 9/5 + 32


print("\nPOST-INIT")
s = Suhu(100)
print(f"Celsius: {s.celsius}")
print(f"Fahrenheit: {s.fahrenheit}")


# =============================================
# 6. DATACLASS DENGAN INHERITANCE
# =============================================

@dataclass
class Hewan:
    nama: str
    suara: str

@dataclass
class Kucing(Hewan):
    warna: str = "Orange"
    indoor: bool = True


print("\nINHERITANCE")
kucing = Kucing("Kitty", "Meong", "Calico")
print(f"Kucing: {kucing}")


# =============================================
# 7. CONVERT KE DICT/TUPLE
# =============================================

@dataclass
class Produk:
    nama: str
    harga: int
    stok: int


print("\nCONVERT")
laptop = Produk("Laptop", 10000000, 5)
print(f"Dict: {asdict(laptop)}")
print(f"Tuple: {astuple(laptop)}")


# =============================================
# 8. DATACLASS SEBAGAI NAMED TUPLE ALTERNATIVE
# =============================================

from typing import NamedTuple

# NamedTuple (immutable)
class PointNT(NamedTuple):
    x: int
    y: int

# Dataclass (mutable by default)
@dataclass
class PointDC:
    x: int
    y: int


print("\nDATACLASS vs NAMEDTUPLE")
pnt = PointNT(1, 2)
pdc = PointDC(1, 2)

print(f"NamedTuple: {pnt}")
print(f"Dataclass: {pdc}")

# NamedTuple lebih ringan tapi tidak bisa diubah
# PointNT(1, 2) -> object ringan, immutable
# PointDC(1, 2) -> object dengan fitur lebih banyak


# =============================================
# 9. CONTOH NYATA - User Profile
# =============================================

@dataclass
class UserProfile:
    username: str
    email: str
    full_name: Optional[str] = None
    is_active: bool = True
    tags: List[str] = field(default_factory=list)

    def __post_init__(self):
        self.email = self.email.lower()

    @property
    def display_name(self) -> str:
        return self.full_name or self.username

    def deactivate(self):
        self.is_active = False

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)


print("\nCONTOH NYATA - User Profile")
user = UserProfile("budi123", "BUDI@Email.Com", "Budi Prasetio")
user.add_tag("admin")
user.add_tag("developer")
print(f"User: {user}")
print(f"Display Name: {user.display_name}")
print(f"Tags: {user.tags}")

user.deactivate()
print(f"Active: {user.is_active}")


# =============================================
# 10. ATTRS (Third-party)
# =============================================
# Install: pip install attrs
#
# import attr
#
# @attr.s
# class PointAttrs:
#     x = attr.ib()
#     y = attr.ib()
#
# # atau decorator style
# @attr.define
# class PointAttrs:
#     x: int
#     y: int
#
# Kelebihan attrs:
# - Validasi lebih mudah
# - Converter bawaan
# - Slot support
# - Lebih banyak fitur

print("\nSelesai! Lihat komentar untuk contoh attrs")
