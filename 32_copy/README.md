# `copy.copy()` / `copy.deepcopy()` dalam Python

## Daftar Isi
1. [Assignment vs Copy](#1-assignment-vs-copy)
2. [`copy.copy()` — Shallow Copy](#2-copycopy--shallow-copy)
3. [`copy.deepcopy()` — Deep Copy](#3-copydeepcopy--deep-copy)
4. [Perbandingan Shallow vs Deep](#4-perbandingan-shallow-vs-deep)
5. [Custom Copy Behavior](#5-custom-copy-behavior)
6. [Copy untuk Collection Types](#6-copy-untuk-collection-types)

---

## 1. Assignment vs Copy

```python
# Assignment: hanya membuat alias (satu objek, dua nama)
a = [1, 2, [3, 4]]
b = a
b.append(5)
print(a)  # [1, 2, [3, 4], 5] — ikut berubah!

# Copy: membuat objek baru
import copy
c = copy.copy(a)
```

---

## 2. `copy.copy()` — Shallow Copy

```python
import copy

a = [1, 2, [3, 4]]
b = copy.copy(a)

b[0] = 99       # Tidak mempengaruhi a
b[2][0] = 99    # MEMPERNGARUHI a! (karena masih share reference)

print(a)  # [1, 2, [99, 4]]
print(b)  # [99, 2, [99, 4]]
```

---

## 3. `copy.deepcopy()` — Deep Copy

```python
import copy

a = [1, 2, [3, 4]]
b = copy.deepcopy(a)

b[2][0] = 99    # Tidak mempengaruhi a

print(a)  # [1, 2, [3, 4]]
print(b)  # [1, 2, [99, 4]]
```

---

## 4. Perbandingan Shallow vs Deep

| Aspek | Shallow (`copy()`) | Deep (`deepcopy()`) |
|-------|-------------------|---------------------|
| Nested objects | Share reference | Copy sepenuhnya |
| Kecepatan | Lebih cepat | Lebih lambat |
| Memory | Lebih hemat | Lebih banyak |
| Cocok untuk | Flat objects | Nested/complex objects |

---

## 5. Custom Copy Behavior

```python
import copy

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __copy__(self):
        print("Custom __copy__ called")
        return Point(self.x, self.y)

    def __deepcopy__(self, memo):
        print("Custom __deepcopy__ called")
        return Point(copy.deepcopy(self.x, memo), copy.deepcopy(self.y, memo))

p1 = Point(1, 2)
p2 = copy.copy(p1)
p3 = copy.deepcopy(p1)
```

---

## 6. Copy untuk Collection Types

```python
import copy

# List
a = [[1, 2], [3, 4]]
b = copy.copy(a)       # Shallow: list baru, tapi sublists share
c = copy.deepcopy(a)   # Deep: semua dibuat baru

# Dict
d1 = {"a": [1, 2], "b": [3, 4]}
d2 = copy.copy(d1)       # Shallow
d3 = copy.deepcopy(d1)   # Deep
```
