# Match-Case Pattern Matching (Python 3.10+)

## Daftar Isi
1. [Match-Case Dasar](#1-match-case-dasar)
2. [Literal Patterns](#2-literal-patterns)
3. [Capture Patterns](#3-capture-patterns)
4. [Wildcard Pattern (`_`)](#4-wildcard-pattern-_)
5. [Guard (`if`)](#5-guard-if)
6. [OR Pattern (`|`)](#6-or-pattern-|)
7. [Sequence Patterns](#7-sequence-patterns)
8. [Mapping Patterns](#8-mapping-patterns)
9. [Class Patterns](#9-class-patterns)
10. [Nested Patterns](#10-nested-patterns)

---

## 1. Match-Case Dasar

```python
# Sama seperti switch-case di bahasa lain, tapi lebih powerful
command = "start"

match command:
    case "start":
        print("Memulai...")
    case "stop":
        print("Berhenti...")
    case _:
        print("Perintah tidak dikenal")
```

---

## 2. Literal Patterns

```python
# Cocokkan dengan nilai literal
match status_code:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
```

---

## 3. Capture Patterns

```python
# Tangkap nilai ke variabel
match command:
    case "quit":
        print("Keluar")
    case other:
        print(f"Unknown: {other}")

# Capture pattern: merekam nilai
match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"Di sumbu X: {x}")
    case (0, y):
        print(f"Di sumbu Y: {y}")
    case (x, y):
        print(f"Titik ({x}, {y})")
```

---

## 4. Wildcard Pattern (`_`)

```python
# _ adalah catch-all (seperti default)
match command:
    case "start":
        print("Start")
    case "stop":
        print("Stop")
    case _:
        print("Lainnya")
```

---

## 5. Guard (`if`)

```python
# Tambahkan kondisi dengan if
match age:
    case n if n < 0:
        print("Tidak valid")
    case n if n < 18:
        print("Anak-anak")
    case n if n < 65:
        print("Dewasa")
    case _:
        print("Lansia")
```

---

## 6. OR Pattern (`|`)

```python
# Cocokkan beberapa nilai sekaligus
match status:
    case "success" | "ok" | "done":
        print("Berhasil")
    case "error" | "fail":
        print("Gagal")
    case _:
        print("Status lain")
```

---

## 7. Sequence Patterns

```python
# Cocokkan urutan elemen
match point:
    case [x, y]:
        print(f"2D: ({x}, {y})")
    case [x, y, z]:
        print(f"3D: ({x}, {y}, {z})")

# Dengan * (rest pattern)
match items:
    case [first, *rest]:
        print(f"First: {first}, Rest: {rest}")
    case []:
        print("Kosong")
```

---

## 8. Mapping Patterns

```python
# Cocokkan dict/objek dengan mapping pattern
match user:
    case {"name": name, "age": age}:
        print(f"{name} umur {age}")
    case {"name": name}:
        print(f"{name} (tanpa umur)")
    case {}:
        print("Data kosong")
```

---

## 9. Class Patterns

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

match point:
    case Point(x=0, y=0):
        print("Origin")
    case Point(x=x, y=0):
        print(f"Di sumbu X: {x}")
    case Point(x=0, y=y):
        print(f"Di sumbu Y: {y}")
    case Point(x=x, y=y):
        print(f"Titik ({x}, {y})")
```

---

## 10. Nested Patterns

```python
# Pattern bisa bersarang
match data:
    case {"user": {"name": name, "address": {"city": city}}}:
        print(f"{name} tinggal di {city}")
    case {"user": {"name": name}}:
        print(f"{name} (tanpa alamat)")
```
