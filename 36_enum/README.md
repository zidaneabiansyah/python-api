# Enum Module dalam Python

## Daftar Isi
1. [Apa itu Enum](#1-apa-itu-enum)
2. [Basic Enum](#2-basic-enum)
3. [Enum dengan Value](#3-enum-dengan-value)
4. [Auto](#4-auto)
5. [Method di Enum](#5-method-di-enum)
6. [Iterasi Enum](#6-iterasi-enum)
7. [Enum sebagai Dict Key](#7-enum-sebagai-dict-key)
8. [StrEnum (Python 3.11+)](#8-strenum-python-311)

---

## 1. Apa itu Enum

**Enum** (Enumeration) adalah kelas untuk membuat **konstanta terbatas** yang memiliki nama. Berguna untuk mengganti magic values dengan nilai yang bermakna.

```python
from enum import Enum

class Status(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"

# Akses
print(Status.PENDING)           # Status.PENDING
print(Status.PENDING.value)     # "pending"
print(Status.PENDING.name)      # "PENDING"
```

---

## 2. Basic Enum

```python
from enum import Enum

class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4

# Akses
dir = Direction.NORTH
print(dir)           # Direction.NORTH
print(dir.value)     # 1
print(dir.name)      # "NORTH"
```

---

## 3. Enum dengan Value

```python
from enum import Enum

class Color(Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

# Akses tuple value
print(Color.RED.value)  # (255, 0, 0)
r, g, b = Color.RED.value
print(f"R={r}, G={g}, B={b}")
```

---

## 4. Auto

```python
from enum import Enum, auto

class Status(Enum):
    PENDING = auto()    # 1
    APPROVED = auto()   # 2
    REJECTED = auto()   # 3

print(Status.PENDING.value)  # 1
```

---

## 5. Method di Enum

```python
from enum import Enum

class Status(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"

    def is_terminal(self):
        return self in (Status.APPROVED, Status.REJECTED)

    @classmethod
    def from_string(cls, s):
        for status in cls:
            if status.value == s:
                return status
        raise ValueError(f"Unknown status: {s}")
```

---

## 6. Iterasi Enum

```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Iterasi
for color in Color:
    print(f"{color.name} = {color.value}")

# Cari berdasarkan value
print(Color(1))  # Color.RED
print(Color["RED"])  # Color.RED
```

---

## 7. Enum sebagai Dict Key

```python
from enum import Enum

class Status(Enum):
    PENDING = 1
    DONE = 2

# Enum hashable, bisa jadi dict key
counts = {Status.PENDING: 5, Status.DONE: 10}
print(counts[Status.PENDING])  # 5
```

---

## 8. StrEnum (Python 3.11+)

```python
from enum import StrEnum

class Color(StrEnum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

# StrEnum bisa dibandingkan dengan string
print(Color.RED == "red")  # True
print(f"Color: {Color.RED}")  # "Color: red"
```
