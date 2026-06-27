# Walrus Operator (`:=`) dalam Python

## Daftar Isi
1. [Apa itu Walrus Operator](#1-apa-itu-walrus-operator)
2. [`if` dengan Walrus](#2-if-dengan-walrus)
3. [`while` dengan Walrus](#3-while-dengan-walrus)
4. [List Comprehension dengan Walrus](#4-list-comprehension-dengan-walrus)
5. [Filter & Lambda dengan Walrus](#5-filter--lambda-dengan-walrus)
6. [Walrus dalam Fungsi](#6-walrus-dalam-fungsi)

---

## 1. Apa itu Walrus Operator

Walrus operator `:=` (Python 3.8+) **menugaskan nilai ke variabel sekaligus mengembalikan nilainya**. Nama "walrus" karena `:=` mirip kepala dan taring walrus.

```python
# Tanpa walrus
n = len([1, 2, 3])
if n > 2:
    print(n)

# Dengan walrus (lebih singkat)
if (n := len([1, 2, 3])) > 2:
    print(n)
```

---

## 2. `if` dengan Walrus

```python
data = [1, 2, 3, 4, 5]

# Tanpa walrus: panggil fungsi 2 kali
if len(data) > 3:
    print(f"Panjang: {len(data)}")

# Dengan walrus: panggil fungsi 1 kali
if (n := len(data)) > 3:
    print(f"Panjang: {n}")

# Walrus bisa dipakai di many contexts
if (result := sorted([3, 1, 2])) == [1, 2, 3]:
    print(f"Sorted: {result}")
```

---

## 3. `while` dengan Walrus

```python
# Tanpa walrus
line = input("Ketik (kosong untuk stop): ")
while line != "":
    print(f"Anda ketik: {line}")
    line = input("Ketik (kosong untuk stop): ")

# Dengan walrus (DRY - Don't Repeat Yourself)
while (line := input("Ketik (kosong untuk stop): ")) != "":
    print(f"Anda ketik: {line}")
```

---

## 4. List Comprehension dengan Walrus

```python
# Filter dan transform sekaligus
data = [1, -2, 3, -4, 5, 0]

# Hanya ambil positif, tapi juga dapat nilainya
positif = [y for x in data if (y := abs(x)) > 0]
print(positif)  # [1, 2, 3, 4, 5]

# Nested comprehension dengan walrus
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix if len(row) > 2 if (x := row[0]) > 0]
print(flat)  # [1, 4, 7]
```

---

## 5. Filter & Lambda dengan Walrus

```python
# Filter dengan kondisi kompleks
words = ["hello", "world", "python", "hi", "code"]

# Panjang > 3 dan huruf pertama 'h'
result = [
    (word, length)
    for word in words
    if (length := len(word)) > 3
    and word[0] == 'h'
]
print(result)  # [('hello', 5)]

# Dengan filter()
result2 = list(filter(lambda w: (l := len(w)) > 3, words))
print(result2)  # ['hello', 'world', 'python']
```

---

## 6. Walrus dalam Fungsi

```python
# Reuse hasil komputasi
def process_data(data):
    if (n := len(data)) == 0:
        return "Data kosong"
    elif n == 1:
        return f"Satu item: {data[0]}"
    else:
        return f"{n} items"

# Walrus dalam exception handling
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    return result
```
