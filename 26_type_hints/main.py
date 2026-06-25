"""
TYPE HINTS LANJUTAN (Typing Module)
=====================================
 Type hints membantu IDE dan type checker memahami tipe data
"""

from typing import (
    List, Dict, Tuple, Set, Optional, Union, Any,
    Callable, Iterator, Generator, Type, TypeVar, Generic,
    Protocol, Literal, Final, ClassVar, TYPE_CHECKING,
)
from dataclasses import dataclass
from abc import ABC, abstractmethod

# =============================================
# 1. BASIC TYPE HINTS
# =============================================

print("BASIC TYPE HINTS")

# Variabel
nama: str = "Budi"
umur: int = 25
tinggi: float = 170.5
menikah: bool = False

# Function
def sapa(nama: str) -> str:
    return f"Halo, {nama}!"

def tambah(a: int, b: int) -> int:
    return a + b

print(sapa("Budi"))
print(f"5 + 3 = {tambah(5, 3)}")


# =============================================
# 2. COLLECTION TYPES
# =============================================

print("\nCOLLECTION TYPES")

# List
def proses_angka(angka: List[int]) -> List[int]:
    return [x * 2 for x in angka]

# Dict
def hitung_huruf(teks: str) -> Dict[str, int]:
    hitung: Dict[str, int] = {}
    for h in teks.lower():
        hitung[h] = hitung.get(h, 0) + 1
    return hitung

# Tuple
def koordinat() -> Tuple[float, float]:
    return (1.5, 2.5)

# Set
def ambil_unik(items: List[str]) -> Set[str]:
    return set(items)

print(f"Dobel: {proses_angka([1, 2, 3])}")
print(f"Huruf: {hitung_huruf('hello')}")
print(f"Koordinat: {koordinat()}")
print(f"Unik: {ambil_unik(['a', 'b', 'a'])}")


# =============================================
# 3. OPTIONAL & UNION
# =============================================

print("\nOPTIONAL & UNION")

# Optional = Union[T, None]
def cari_user(user_id: int) -> Optional[dict]:
    users = {1: {"nama": "Budi"}, 2: {"nama": "Andi"}}
    return users.get(user_id)

# Union = tipe A atau B
def konversi(value: Union[int, str]) -> int:
    if isinstance(value, str):
        return int(value)
    return value

# Python 3.10+ bisa pakai |
def tambah_baru(a: int | str, b: int | str) -> int | str:
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    return f"{a}{b}"

print(f"Cari user 1: {cari_user(1)}")
print(f"Cari user 99: {cari_user(99)}")
print(f"Konversi: {konversi('42')}")
print(f"Tambah: {tambah_baru(1, 2)}")


# =============================================
# 4. ANY, OBJECT, NO_RETURN
# =============================================

print("\nANY, OBJECT, NO_RETURN")

from typing import NoReturn

# Any - tipe apapun
def proses_apapun(data: Any) -> Any:
    return data

# Object - base class semua
def terima_objek(obj: object) -> str:
    return str(obj)

# NoReturn - tidak return apapun
def raise_error(msg: str) -> NoReturn:
    raise ValueError(msg)

print(f"Any: {proses_apapun('hello')}")
print(f"Object: {terima_objek(42)}")


# =============================================
# 5. CALLABLE - Fungsi sebagai Parameter
# =============================================

print("\nCALLABLE")

# Callable[[params], return_type]
def jalankan_operasi(a: int, b: int, operasi: Callable[[int, int], int]) -> int:
    return operasi(a, b)

def tambah(a: int, b: int) -> int:
    return a + b

def kali(a: int, b: int) -> int:
    return a * b

print(f"Tambah: {jalankan_operasi(5, 3, tambah)}")
print(f"Kali: {jalankan_operasi(5, 3, kali)}")

# Callback pattern
def proses_data(data: List[int], callback: Callable[[int], None]) -> None:
    for item in data:
        callback(item)

proses_data([1, 2, 3], lambda x: print(f"Item: {x}"))


# =============================================
# 6. ITERATOR & GENERATOR
# =============================================

print("\nITERATOR & GENERATOR")

# Iterator
def counter(max_val: int) -> Iterator[int]:
    n = 0
    while n < max_val:
        yield n
        n += 1

# Generator dengan return value
def fibonacci(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Iterator comprehension
def kuadrat(angka: List[int]) -> Iterator[int]:
    return (x**2 for x in angka)

print(f"Counter: {list(counter(5))}")
print(f"Fibonacci: {list(fibonacci(8))}")
print(f"Kuadrat: {list(kuadrat([1, 2, 3, 4]))}")


# =============================================
# 7. TYPE VARIABLE & GENERICS
# =============================================

print("\nTYPE VARIABLE & GENERICS")

T = TypeVar('T')
K = TypeVar('K')
V = TypeVar('V')

# Generic class
class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def peek(self) -> T:
        return self.items[-1]

    def is_empty(self) -> bool:
        return len(self.items) == 0

# Generic function
def pertama(items: List[T]) -> Optional[T]:
    return items[0] if items else None

# Multiple type vars
def swap(a: K, b: V) -> Tuple[V, K]:
    return b, a

# Generic class with multiple types
class Pair(Generic[K, V]):
    def __init__(self, key: K, value: V):
        self.key = key
        self.value = value

    def __repr__(self) -> str:
        return f"Pair({self.key}, {self.value})"


# Stack of int
int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)
print(f"Int stack pop: {int_stack.pop()}")

# Stack of string
str_stack: Stack[str] = Stack()
str_stack.push("hello")
print(f"Str stack peek: {str_stack.peek()}")

# Generic functions
print(f"Pertama [1,2,3]: {pertama([1, 2, 3])}")
print(f"Pertama []: {pertama([])}")
print(f"Swap: {swap('a', 1)}")

# Pair
pair = Pair("nama", "Budi")
print(f"Pair: {pair}")


# =============================================
# 8. PROTOCOL (Structural Subtyping)
# =============================================

print("\nPROTOCOL")

# Protocol = duck typing dengan type hints
# Jika object punya method yang dibutuhkan, dia "implements" protocol

class Drawable(Protocol):
    def draw(self) -> str: ...

class Circle:
    def draw(self) -> str:
        return "Menggambar lingkaran"

class Square:
    def draw(self) -> str:
        return "Menggambar persegi"

def render(shape: Drawable) -> None:
    print(f"Render: {shape.draw()}")

# Circle dan Square tidak inherit Drawable
# Tapi mereka "is-a" Drawable karena punya method draw()
render(Circle())
render(Square())


# =============================================
# 9. LITERAL & FINAL
# =============================================

print("\nLITERAL & FINAL")

from typing import Literal, Final

# Literal - hanya nilai spesifik
def bergerak(arah: Literal["atas", "bawah", "kiri", "kanan"]) -> str:
    return f"Berpindah ke {arah}"

# Final - tidak bisa diubah
PI: Final = 3.14159
MAX_SIZE: Final[int] = 100

# ClassVar - class variable
@dataclass
class Game:
    score: int = 0
    max_score: ClassVar[int] = 1000

print(bergerak("atas"))
print(f"PI: {PI}")
print(f"Max score: {Game.max_score}")


# =============================================
# 10. TYPE CHECKING
# =============================================

print("\nTYPE CHECKING")

# TYPE_CHECKING hanya True saat type checker berjalan
if TYPE_CHECKING:
    # Import hanya untuk type hints, tidak dieksekusi
    from datetime import datetime

# Fungsi yang menggunakan TYPE_CHECKING
def log_message(msg: str, timestamp: str) -> None:
    print(f"[{timestamp}] {msg}")

log_message("Hello", "2025-01-01")


# =============================================
# 11. ADVANCED - NewType
# =============================================

print("\nNEWTYPES")

from typing import NewType

UserId = NewType('UserId', int)
Email = NewType('Email', str)

def get_user(user_id: UserId) -> dict:
    return {"id": user_id, "nama": "Budi"}

# UserId adalah tipe terpisah dari int
user_id = UserId(123)
print(f"User ID: {get_user(user_id)})

# Type checker akan detect jika pakai wrong type
# get_user(456)  # Error: Expected UserId, got int


# =============================================
# 12. CONTOH NYATA
# =============================================

print("\nCONTOH NYATA")

from typing import TypedDict

# TypedDict - dict dengan struktur tetap
class UserDict(TypedDict):
    id: int
    nama: str
    email: str
    active: bool

def buat_user(id: int, nama: str, email: str) -> UserDict:
    return {"id": id, "nama": nama, "email": email, "active": True}

def proses_user(user: UserDict) -> str:
    status = "active" if user["active"] else "inactive"
    return f"{user['nama']} ({status})"

user = buat_user(1, "Budi", "budi@test.com")
print(f"User: {proses_user(user)}")


# =============================================
# RINGKASAN
# =============================================
print("\n" + "=" * 50)
print("RINGKASAN TYPE HINTS")
print("=" * 50)
print("str, int, float, bool  - Tipe dasar")
print("List, Dict, Tuple, Set - Collections")
print("Optional[X]             - X atau None")
print("Union[X, Y]             - X atau Y")
print("Callable[[X], Y]        - Fungsi")
print("Iterator[T]             - Iterator")
print("Generator[T, S, R]      - Generator")
print("TypeVar('T')            - Generic")
print("Protocol                - Structural typing")
print("Literal['a', 'b']       - Nilai spesifik")
print("Final                   - Konstanta")
print("NewType                 - Tipe baru")
print("TypedDict               - Dict terstruktur")
