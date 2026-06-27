# Extended Unpacking dalam Python

## Daftar Isi
1. [Unpacking Dasar](#1-unpacking-dasar)
2. [`*` untuk List/Tuple](#2--untuk-listtuple)
3. [`**` untuk Dict](#3--untuk-dict)
4. [Unpacking di Function Arguments](#4-unpacking-di-function-arguments)
5. [Extended Unpacking di Assignment](#5-extended-unpacking-di-assignment)
6. [Merge Collections](#6-merge-collections)

---

## 1. Unpacking Dasar

```python
# Tuple unpacking
a, b, c = (1, 2, 3)

# List unpacking
x, y, z = [10, 20, 30]

# Swap
a, b = b, a
```

---

## 2. `*` untuk List/Tuple

```python
first, *middle, last = [1, 2, 3, 4, 5]
# first = 1, middle = [2, 3, 4], last = 5

*head, last = [1, 2, 3, 4]
# head = [1, 2, 3], last = 4

first, *tail = [1, 2, 3, 4]
# first = 1, tail = [2, 3, 4]

# Gabungkan list
a = [1, 2]
b = [3, 4]
c = [*a, *b]  # [1, 2, 3, 4]
```

---

## 3. `**` untuk Dict

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Merge dict
merged = {**dict1, **dict2}  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Override
config = {"timeout": 30, "retries": 3}
override = {"timeout": 60}
final = {**config, **override}  # {'timeout': 60, 'retries': 3}
```

---

## 4. Unpacking di Function Arguments

```python
def fungsi(a, b, c):
    print(a, b, c)

args = [1, 2, 3]
fungsi(*args)  # Sama dengan fungsi(1, 2, 3)

kwargs = {"a": 1, "b": 2, "c": 3}
fungsi(**kwargs)  # Sama dengan fungsi(a=1, b=2, c=3)
```

---

## 5. Extended Unpacking di Assignment

```python
# Hanya ambil beberapa elemen, sisanya dikumpulkan
a, *b = range(5)       # a=0, b=[1,2,3,4]
*a, b = range(5)       # a=[0,1,2,3], b=4
a, *b, c = range(5)    # a=0, b=[1,2,3], c=4
a, b, *c = range(5)    # a=0, b=1, c=[2,3,4]
```

---

## 6. Merge Collections

```python
# List
merged_list = [*list1, *list2, *list3]

# Set
merged_set = {*set1, *set2}

# Dict (override yang belakang)
merged_dict = {**dict1, **dict2, "key": "value"}
```
