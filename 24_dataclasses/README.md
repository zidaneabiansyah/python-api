# Dataclasses dalam Python

## Daftar Isi
1. [Apa itu Dataclass](#1-apa-itu-dataclass)
2. [Field Options](#2-field-options)
3. [Frozen Dataclass](#3-frozen-dataclass)
4. [Post Init](#4-post-init)
5. [Convert](#5-convert)
6. [Attrs](#6-attrs)

---

## 1. Apa itu Dataclass

`@dataclass` decorator (Python 3.7+) yang membuat class untuk data storage lebih mudah.

### Tanpa Dataclass
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
```

### Dengan Dataclass
```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
```

Otomatis dapat:
- `__init__()`
- `__repr__()`
- `__eq__()`

---

## 2. Field Options

```python
@dataclass
class Config:
    host: str = "localhost"           # Default value
    port: int = field(default=8080)   # Field() untuk opsi
    _secret: str = field(repr=False)  # Sembunyi dari repr
    tags: List[str] = field(default_factory=list)  # Mutable default
```

| Parameter | Keterangan |
|-----------|------------|
| `default` | Nilai default |
| `default_factory` | Fungsi untuk generate default |
| `repr` | Tampilkan di `__repr__` |
| `compare` | Ikut di `__eq__` |
| `hash` | Ikut di hash |
| `init` | Ikut di `__init__` |

---

## 3. Frozen Dataclass

```python
@dataclass(frozen=True)
class Color:
    r: int
    g: int
    b: int
```

- Immutable (tidak bisa diubah)
- Hashable (bisa jadi dict key)
- Error jika coba ubah value

---

## 4. Post Init

```python
@dataclass
class Suhu:
    celsius: float

    def __post_init__(self):
        if self.celsius < -273.15:
            raise ValueError("Invalid!")
```

Jalankan setelah `__init__()` untuk validasi/custom logic.

---

## 5. Convert

```python
from dataclasses import asdict, astuple

p = Point(5, 10)
asdict(p)   # {'x': 5, 'y': 10}
astuple(p)  # (5, 10)
```

---

## 6. Attrs

Third-party library dengan fitur lebih banyak:

```python
import attr

@attr.define
class Point:
    x: int
    y: int

    @attr.validators.example
    def _(self, attribute, value):
        if value < 0:
            raise ValueError("Must be positive")
```

### Install
```bash
pip install attrs
```

---

## Perbandingan

| Fitur | Dataclass | Attrs | NamedTuple |
|-------|-----------|-------|------------|
| Mutable | Ya | Ya | Tidak |
| Validasi | Manual | Built-in | Tidak |
| Frozen | Ya | Ya | Selalu |
| Type Hints | Ya | Ya | Ya |
| Speed | Cepat | Cepat | Paling cepat |
