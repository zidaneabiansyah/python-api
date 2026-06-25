# Type Hints Lanjutan dalam Python

## Daftar Isi
1. [Basic Types](#1-basic-types)
2. [Collection Types](#2-collection-types)
3. [Optional & Union](#3-optional--union)
4. [Callable](#4-callable)
5. [Generics](#5-generics)
6. [Protocol](#6-protocol)
7. [Advanced Types](#7-advanced-types)

---

## 1. Basic Types

```python
# Variabel
nama: str = "Budi"
umur: int = 25
tinggi: float = 170.5
menikah: bool = False

# Function
def sapa(nama: str) -> str:
    return f"Halo, {nama}!"
```

---

## 2. Collection Types

```python
from typing import List, Dict, Tuple, Set

# List
def proses(angka: List[int]) -> List[int]:
    return [x * 2 for x in angka]

# Dict
def hitung(teks: str) -> Dict[str, int]:
    return {"h": 1}  # Simplified

# Tuple (fixed length)
def koordinat() -> Tuple[float, float]:
    return (1.0, 2.0)

# Tuple (variable length)
def angka(n: int) -> Tuple[int, ...]:
    return tuple(range(n))

# Set
def unik(items: List[str]) -> Set[str]:
    return set(items)

# Python 3.9+ bisa pakai list, dict, dll tanpa import
def proses_v2(angka: list[int]) -> list[int]:
    return [x * 2 for x in angka]
```

---

## 3. Optional & Union

```python
from typing import Optional, Union

# Optional = Union[X, None]
def cari(id: int) -> Optional[dict]:
    return None  # Bisa dict atau None

# Union = tipe A atau B
def konversi(val: Union[int, str]) -> int:
    return int(val)

# Python 3.10+ pakai |
def tambah(a: int | str, b: int | str) -> int | str:
    return a + b
```

---

## 4. Callable

```python
from typing import Callable

# Callable[[param_types], return_type]
def jalankan(a: int, b: int, op: Callable[[int, int], int]) -> int:
    return op(a, b)

def tambah(x: int, y: int) -> int:
    return x + y

jalankan(5, 3, tambah)

# Callback pattern
def proses_data(data: list[int], cb: Callable[[int], None]) -> None:
    for item in data:
        cb(item)
```

---

## 5. Generics

```python
from typing import TypeVar, Generic, List

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

# Specific types
int_stack: Stack[int] = Stack()
str_stack: Stack[str] = Stack()
```

---

## 6. Protocol

```python
from typing import Protocol

# Structural typing - tidak perlu inherit
class Drawable(Protocol):
    def draw(self) -> str: ...

class Circle:
    def draw(self) -> str:  # Punya method draw
        return "Circle"

def render(shape: Drawable) -> None:  # Terima apapun yang punya draw()
    print(shape.draw())

render(Circle())  # OK!
```

---

## 7. Advanced Types

### Literal
```python
from typing import Literal

def bergerak(arah: Literal["atas", "bawah", "kiri", "kanan"]) -> str:
    return f"Berpindah ke {arah}"
```

### Final
```python
from typing import Final

PI: Final = 3.14159
MAX_SIZE: Final[int] = 100
```

### NewType
```python
from typing import NewType

UserId = NewType('UserId', int)
user_id = UserId(123)  # Tipe terpisah dari int
```

### TypedDict
```python
from typing import TypedDict

class UserDict(TypedDict):
    id: int
    nama: str
    email: str

user: UserDict = {"id": 1, "nama": "Budi", "email": "budi@test.com"}
```

---

## Type Checking Tools

| Tool | Keterangan |
|------|------------|
| `mypy` | Static type checker |
| `pyright` | Type checker dari Microsoft |
| `pytype` | Type checker dari Google |

```bash
# Install mypy
pip install mypy

# Jalankan type check
mypy your_code.py
```

---

## Best Practices

1. **Annotate fungsi publik** - Selalu tambahkan type hints
2. **Gunakan Optional** - Untuk nilai yang bisa None
3. **Spesifik** - Hindari `Any` jika bisa
4. **Gunakan TypeVar** - Untuk generic functions/classes
5. **Protocol untuk duck typing** - Lebih fleksibel dari ABC
