# Multiple Inheritance & MRO dalam Python

## Daftar Isi
1. [Multiple Inheritance Dasar](#1-multiple-inheritance-dasar)
2. [Diamond Problem](#2-diamond-problem)
3. [MRO (Method Resolution Order)](#3-mro-method-resolution-order)
4. [`super()` dengan Multiple Inheritance](#4-super-dengan-multiple-inheritance)
5. [Mixin Pattern](#5-mixin-pattern)
6. [`isinstance()` dan `issubclass()`](#6-isinstance-dan-issubclass)

---

## 1. Multiple Inheritance Dasar

```python
class A:
    def method(self):
        return "A"

class B:
    def method(self):
        return "B"

class C(A, B):
    pass

c = C()
print(c.method())  # "A" (dari A, karena A lebih dulu)
print(C.__mro__)
# (<class 'C'>, <class 'A'>, <class 'B'>, <class 'object'>)
```

---

## 2. Diamond Problem

```python
#      A
#     / \
#    B   C
#     \ /
#      D

class A:
    def greet(self):
        return "Hello from A"

class B(A):
    def greet(self):
        return "Hello from B"

class C(A):
    def greet(self):
        return "Hello from C"

class D(B, C):
    pass

d = D()
print(d.greet())  # "Hello from B" (B lebih dulu dari C)
print(D.__mro__)
# D -> B -> C -> A -> object
```

---

## 3. MRO (Method Resolution Order)

```python
# Cek urutan resolusi method
print(D.__mro__)
# Atau:
print(D.mro())

# MRO menggunakan C3 Linearization
# Aturan: D -> B -> C -> A -> object
# 1. Anak sebelum parent
# 2. Kiri sebelum kanan
# 3. Tidak mengulang
```

---

## 4. `super()` dengan Multiple Inheritance

```python
class Base:
    def __init__(self):
        print("Base init")

class Left(Base):
    def __init__(self):
        super().__init__()
        print("Left init")

class Right(Base):
    def __init__(self):
        super().__init__()
        print("Right init")

class Diamond(Left, Right):
    def __init__(self):
        super().__init__()  # Hanya panggil sekali!
        print("Diamond init")

Diamond()
# Base init
# Left init
# Right init  <-- super() mengikuti MRO, bukan urutan definisi
# Diamond init
```

---

## 5. Mixin Pattern

```python
class JsonMixin:
    """Mixin untuk menambahkan serialisasi JSON"""
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class LogMixin:
    """Mixin untuk menambahkan logging"""
    def log(self, msg):
        print(f"[{self.__class__.__name__}] {msg}")

class User(JsonMixin, LogMixin):
    def __init__(self, name):
        self.name = name

user = User("Budi")
print(user.to_json())  # '{"name": "Budi"}'
user.log("Logged in")   # "[User] Logged in"
```

---

## 6. `isinstance()` dan `issubclass()`

```python
class A: pass
class B(A): pass
class C(B): pass

c = C()

# isinstance: objek adalah instance dari class
print(isinstance(c, C))      # True
print(isinstance(c, B))      # True
print(isinstance(c, A))      # True
print(isinstance(c, object)) # True

# issubclass: class adalah subclass dari class lain
print(issubclass(C, B))      # True
print(issubclass(C, A))      # True
print(issubclass(A, C))      # False

# Cek multiple parent
print(isinstance(c, (A, B)))  # True
```
