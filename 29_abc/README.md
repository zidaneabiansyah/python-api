# Abstract Base Classes (ABC) dalam Python

## Daftar Isi
1. [Apa itu ABC](#1-apa-itu-abc)
2. [`@abstractmethod`](#2-abstractmethod)
3. [`@abstractproperty` (deprecated)](#3-abstractproperty-deprecated)
4. [`@property` + `@abstractmethod`](#4-property--abstractmethod)
5. [ABC dengan `register()`](#5-abc-dengan-register)
6. [Built-in ABC dari `collections.abc`](#6-built-in-abc-dari-collectionsabc)
7. [Stacked Decorators](#7-stacked-decorators)

---

## 1. Apa itu ABC

**Abstract Base Class** adalah class yang tidak bisa diinstansiasi langsung. Berguna untuk mendefinisikan **kontrak** — class turunan **wajib** mengimplementasi method tertentu.

```python
from abc import ABC, abstractmethod

class Hewan(ABC):
    @abstractmethod
    def bersuara(self):
        pass

# Hewan()  # ERROR! Tidak bisa diinstansiasi

class Kucing(Hewan):
    def bersuara(self):
        return "Meow!"

kucing = Kucing()  # OK
print(kucing.bersuara())  # "Meow!"
```

---

## 2. `@abstractmethod`

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius
```

---

## 3. `@abstractproperty` (deprecated)

```python
# JANGAN PAKAI ini (deprecated sejak Python 3.3)
from abc import ABC, abstractmethod

class Player(ABC):
    @property
    @abstractmethod
    def score(self):
        pass
```

---

## 4. `@property` + `@abstractmethod`

```python
from abc import ABC, abstractmethod

class Player(ABC):
    @property
    @abstractmethod
    def score(self):
        """Score harus diimplementasi oleh subclass"""
        pass

class Gamer(Player):
    def __init__(self, name, points):
        self.name = name
        self._score = points

    @property
    def score(self):
        return self._score

gamer = Gamer("Budi", 100)
print(f"Score: {gamer.score}")
```

---

## 5. ABC dengan `register()`

```python
from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

# Class tanpa inheritance, tapi didaftarkan sebagai subclass
class Line:
    def draw(self):
        print("Menggambar garis")

Drawable.register(Line)

# Bisa dicek
print(issubclass(Line, Drawable))  # True

# Tapi tetap tidak bisa instansiasi Drawable
```

---

## 6. Built-in ABC dari `collections.abc`

```python
from collections.abc import Sequence, Mapping, Set

# Sequence: mendukung __getitem__ dan __len__
class MyList(Sequence):
    def __init__(self, data):
        self._data = list(data)

    def __getitem__(self, index):
        return self._data[index]

    def __len__(self):
        return len(self._data)

my_list = MyList([1, 2, 3])
print(len(my_list))    # 3
print(my_list[0])      # 1
print(1 in my_list)    # True (otomatis dari Sequence)
print(list(my_list))   # [1, 2, 3]
```

---

## 7. Stacked Decorators

```python
from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def method(self):
        """Method abstract"""
        pass

    @abstractmethod
    def other(self):
        """Method abstract lain"""
        pass

# Urutan dekorator: dari dalam ke luar
# @property
# @abstractmethod
# def prop(self): ...
```
