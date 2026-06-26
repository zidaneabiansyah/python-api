"""
__slots__ (MEMORY OPTIMIZATION)
================================
 __slots__ membatasi attribute instance dan menghemat memori
 Tanpa __slots__: setiap instance punya __dict__ (~64 bytes)
 Dengan __slots__: attribute disimpan di fixed-size array
"""

import sys
from dataclasses import dataclass


# =============================================
# 1. DEFAULT vs __slots__
# =============================================

print("=== DEFAULT vs __slots__ ===")


class PointDefault:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointSlots:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = PointDefault(1, 2)
p2 = PointSlots(1, 2)

print(f"Default punya __dict__: {hasattr(p1, '__dict__')}")
print(f"Slots punya __dict__:   {hasattr(p2, '__dict__')}")
print(f"Default __dict__: {p1.__dict__}")
print(f"Slots __dict__:   TIDAK ADA ( AttributeError)")

# Akses attribute normal
print(f"\nDefault.x = {p1.x}, Default.y = {p1.y}")
print(f"Slots.x = {p2.x}, Slots.y = {p2.y}")


# =============================================
# 2. PERBANDINGAN MEMORY
# =============================================

print("\n=== PERBANDINGAN MEMORY ===")

N = 100000

# Tanpa __slots__
default_points = [PointDefault(i, i) for i in range(N)]

# Dengan __slots__
slots_points = [PointSlots(i, i) for i in range(N)]

# Hitung total memory
default_memory = sum(sys.getsizeof(p) + sys.getsizeof(p.__dict__) for p in default_points)
slots_memory = sum(sys.getsizeof(p) for p in slots_points)

print(f"{N:,} instance PointDefault: {default_memory:,} bytes ({default_memory/1024/1024:.1f} MB)")
print(f"{N:,} instance PointSlots:   {slots_memory:,} bytes ({slots_memory/1024/1024:.1f} MB)")
print(f"Selisih: {default_memory - slots_memory:,} bytes ({(default_memory - slots_memory)/1024/1024:.1f} MB)")
print(f"Hemat: {(1 - slots_memory/default_memory)*100:.1f}%")


# =============================================
# 3. __slots__ DENGAN PROPERTY
# =============================================

print("\n=== __slots__ DENGAN PROPERTY ===")


class User:
    __slots__ = ('_name', '_email', '_age')

    def __init__(self, name, email, age):
        self._name = name
        self._email = email
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age tidak boleh negatif")
        self._age = value


user = User("Budi", "budi@email.com", 25)
print(f"Nama: {user.name}")
print(f"Email: {user.email}")
print(f"Age: {user.age}")

user.age = 30
print(f"Age baru: {user.age}")

try:
    user.age = -5
except ValueError as e:
    print(f"Error: {e}")

# Tidak bisa tambah attribute sembarang
try:
    user.username = "budi123"
except AttributeError as e:
    print(f"Error tambah attribute: {e}")


# =============================================
# 4. __slots__ DENGAN INHERITANCE
# =============================================

print("\n=== __slots__ DENGAN INHERITANCE ===")


class Animal:
    __slots__ = ('name', 'species')

    def __init__(self, name, species):
        self.name = name
        self.species = species


class Dog(Animal):
    __slots__ = ('breed', 'is_trained')

    def __init__(self, name, breed, is_trained=False):
        super().__init__(name, "Canine")
        self.breed = breed
        self.is_trained = is_trained


class Puppy(Dog):
    # Puppy otomatis mewarisi __slots__ dari Dog dan Animal
    __slots__ = ('vaccinated',)

    def __init__(self, name, breed, vaccinated=False):
        super().__init__(name, breed)
        self.vaccinated = vaccinated


dog = Dog("Buddy", "Golden Retriever", True)
puppy = Puppy("Max", "Labrador", False)

print(f"Dog: {dog.name}, {dog.species}, {dog.breed}, trained={dog.is_trained}")
print(f"Puppy: {puppy.name}, {puppy.species}, {puppy.breed}, vaccinated={puppy.vaccinated}")

# Cek slots
print(f"\nAnimal slots: {Animal.__slots__}")
print(f"Dog slots: {Dog.__slots__}")
print(f"Puppy slots: {Puppy.__slots__}")
print(f"Puppy punya __dict__: {hasattr(puppy, '__dict__')}")


# =============================================
# 5. __slots__ DENGAN CLASS TANPA __dict__
# =============================================

print("\n=== __slots__ TANPA __dict__ ===")


class StrictClass:
    __slots__ = ('x', 'y')
    # Tidak ada __dict__ sama sekali

    def __init__(self, x, y):
        self.x = x
        self.y = y


obj = StrictClass(1, 2)

# Semua cara akses attribute yang dilarang
print(f"punya __dict__: {hasattr(obj, '__dict__')}")
print(f"punya __slots__: {hasattr(obj, '__slots__')}")

# Test dynamic attribute
try:
    obj.z = 3
except AttributeError as e:
    print(f"Tidak bisa tambah attribute: {e}")

# Test akses dict
try:
    _ = obj.__dict__
except AttributeError as e:
    print(f"Tidak ada __dict__: {e}")


# =============================================
# 6. __slots__ DENGAN DATACLASS
# =============================================

print("\n=== __slots__ DENGAN DATACLASS ===")


@dataclass(slots=True)  # Python 3.10+
class Vector:
    x: float
    y: float

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


v = Vector(3, 4)
print(f"Vector: {v}")
print(f"Magnitude: {v.magnitude()}")
print(f"Punya __dict__: {hasattr(v, '__dict__')}")


# =============================================
# 7. REAL-WORLD: BANYAK INSTANCE
# =============================================

print("\n=== REAL-WORLD: BANYAK INSTANCE ===")


class Point3D:
    __slots__ = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Point3DDict:
    """Versi tanpa __slots__"""
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


# Simulasi: 3D point cloud (LiDAR data)
N = 50000

points_slots = [Point3D(i, i, i) for i in range(N)]
points_dict = [Point3DDict(i, i, i) for i in range(N)]

mem_slots = sum(sys.getsizeof(p) for p in points_slots)
mem_dict = sum(sys.getsizeof(p) + sys.getsizeof(p.__dict__) for p in points_dict)

print(f"3D Point Cloud ({N:,} points):")
print(f"  Dengan __slots__: {mem_slots:,} bytes ({mem_slots/1024/1024:.2f} MB)")
print(f"  Tanpa __slots__:  {mem_dict:,} bytes ({mem_dict/1024/1024:.2f} MB)")
print(f"  Hemat: {(1 - mem_slots/mem_dict)*100:.1f}%")
