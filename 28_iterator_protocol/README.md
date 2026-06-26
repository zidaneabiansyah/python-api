# Iterator Protocol dalam Python

## Daftar Isi
1. [Apa itu Iterator](#1-apa-itu-iterator)
2. [Iterator Protocol: `__iter__` dan `__next__`](#2-iterator-protocol-__iter__-dan-__next__)
3. [Custom Iterator](#3-custom-iterator)
4. [Iterator vs Generator](#4-iterator-vs-generator)
5. [`iter()` dan `next()` Built-in](#5-iter-dan-next-built-in)
6. [Infinite Iterator](#6-infinite-iterator)
7. [StopIteration](#7-stopiteration)
8. [`iter()` dengan Sentinel](#8-iter-dengan-sentinel)

---

## 1. Apa itu Iterator

**Iterator** adalah objek yang bisa diiterasi (dilalui satu per satu). Setiap objek Python yang memiliki `__iter__` method adalah **iterable**.

```python
# Iterable: punya __iter__
# Iterator: punya __iter__ DAN __next__

my_list = [1, 2, 3]  # Iterable (punya __iter__)
my_iter = iter(my_list)  # Iterator (punya __iter__ + __next__)

print(next(my_iter))  # 1
print(next(my_iter))  # 2
print(next(my_iter))  # 3
```

---

## 2. Iterator Protocol: `__iter__` dan `__next__`

```python
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self  # Iterator mengembalikan dirinya sendiri

    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1

for num in Countdown(5):
    print(num)  # 5, 4, 3, 2, 1
```

---

## 3. Custom Iterator

```python
class FibIterator:
    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        self.count += 1
        self.a, self.b = self.b, self.a + self.b
        return self.a

fib = list(FibIterator(10))
print(fib)  # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

---

## 4. Iterator vs Generator

| Aspek | Iterator | Generator |
|-------|----------|-----------|
| Implementasi | Class dengan `__iter__` + `__next__` | Function dengan `yield` |
| Kode | Lebih verbose | Lebih singkat |
| State | Manual (`self.x`) | Otomatis |
| Stop | `raise StopIteration` | `return` / selesai |

```python
# Iterator style
class Squares:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.n:
            raise StopIteration
        result = self.current ** 2
        self.current += 1
        return result

# Generator style (lebih simpel)
def squares_gen(n):
    for i in range(n):
        yield i ** 2

# Hasil sama
print(list(Squares(5)))       # [0, 1, 4, 9, 16]
print(list(squares_gen(5)))   # [0, 1, 4, 9, 16]
```

---

## 5. `iter()` dan `next()` Built-in

```python
# iter() membuat iterator dari iterable
nums = [10, 20, 30]
it = iter(nums)

print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30

# next() dengan default value (tidak error jika habis)
print(next(it, "Habis"))  # "Habis"

# for loop menggunakan iterator di balik layar
for x in [1, 2, 3]:
    print(x)
# Sama dengan:
it = iter([1, 2, 3])
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break
```

---

## 6. Infinite Iterator

```python
class InfiniteCounter:
    def __init__(self, start=0, step=1):
        self.current = start
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        value = self.current
        self.current += self.step
        return value

# Gunakan islice untuk membatasi
from itertools import islice

counter = InfiniteCounter(start=1, step=2)  # Ganjil tak hingga
odd_numbers = list(islice(counter, 5))
print(odd_numbers)  # [1, 3, 5, 7, 9]
```

---

## 7. StopIteration

```python
# StopIteration adalah sinyal bahwa iterasi selesai
it = iter([1, 2, 3])
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3

try:
    next(it)  # Error! Tidak ada elemen lagi
except StopIteration:
    print("Iterasi selesai!")

# Di dalam generator, return dengan value jadi pesan StopIteration
def gen():
    yield 1
    yield 2
    return "Selesai"  # Menjadi pesan di StopIteration

g = gen()
print(next(g))  # 1
print(next(g))  # 2
try:
    next(g)
except StopIteration as e:
    print(e)  # "Selesai"
```

---

## 8. `iter()` dengan Sentinel

```python
# iter(callable, sentinel) - panggil callable sampai sentinel
import random

# Contoh: baca input sampai user ketik "quit"
inputs = iter(lambda: input("Ketik (quit untuk stop): "), "quit")

# Contoh: angka acak sampai dapat 0
random.seed(42)
numbers = []
for num in iter(lambda: random.randint(0, 10), 0):
    numbers.append(num)
print(numbers)  # List angka acak, diakhiri sebelum 0
```
