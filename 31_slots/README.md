# `__slots__` dalam Python

## Daftar Isi
1. [Apa itu `__slots__`](#1-apa-itu-__slots__)
2. [Perbandingan Memory](#2-perbandingan-memory)
3. [Cara Menggunakan](#3-cara-menggunakan)
4. [Limitasi `__slots__`](#4-limitasi-__slots__)
5. [`__slots__` dengan Inheritance](#5-__slots__-dengan-inheritance)
6. [Kapan Menggunakan `__slots__`](#6-kapan-menggunakan-__slots__)

---

## 1. Apa itu `__slots__`

`__slots__` adalah special attribute untuk membatasi attribute instance dan **menghemat memori**. Tanpa `__slots__`, Python menggunakan `__dict__` untuk setiap instance.

```python
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

print(hasattr(p1, '__dict__'))  # True
print(hasattr(p2, '__dict__'))  # False
print(hasattr(p2, '__slots__'))  # True
```

---

## 2. Perbandingan Memory

```python
import sys

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

print(f"Default: {sys.getsizeof(p1)} bytes + {sys.getsizeof(p1.__dict__)} bytes dict")
print(f"Slots:   {sys.getsizeof(p2)} bytes")
# Default: ~48 bytes + ~64 bytes dict = ~112 bytes
# Slots:   ~56 bytes
```

---

## 3. Cara Menggunakan

```python
class User:
    __slots__ = ('name', 'email', '_age')

    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self._age = age

    @property
    def age(self):
        return self._age

user = User("Budi", "budi@email.com", 25)
print(user.name)  # OK

# user.username = "test"  # ERROR! AttributeError
```

---

## 4. Limitasi `__slots__`

```python
class Point:
    __slots__ = ('x', 'y')

p = Point()
p.x = 1
p.y = 2

# p.z = 3  # ERROR! Tidak ada attribute 'z'

# Tidak bisa pakai **kwargs untuk attribute baru
# p.__dict__  # ERROR! Tidak ada __dict__
```

---

## 5. `__slots__` dengan Inheritance

```python
class Base:
    __slots__ = ('a',)

class Child(Base):
    __slots__ = ('b',)

c = Child()
c.a = 1  # Dari Base
c.b = 2  # Dari Child

# Child juga mewarisi __slots__ dari Base
# Tapi Child tetap punya __dict__ kecuali juga didefinisikan __slots__
```

---

## 6. Kapan Menggunakan `__slots__`

```python
# GUNAKAN __slots__ ketika:
# 1. Banyak instance dari class yang sama
# 2. Ingin menghemat memori
# 3. Ingin mencegah attribute typo

# JANGAN gunakan __slots__ ketika:
# 1. Perlu dynamic attributes (p.__dict__['baru'] = 1)
# 2. Inherit dari class tanpa __slots__
# 3. Butuh flexibility
```
