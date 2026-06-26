"""
copy.copy() / copy.deepcopy()
==============================
 copy.copy()     → Shallow Copy: objek baru, tapi nested object masih share
 copy.deepcopy() → Deep Copy: objek baru + nested object juga baru
"""

import copy


# =============================================
# 1. ASSIGNMENT BUKAN COPY
# =============================================

print("=== ASSIGNMENT BUKAN COPY ===")

a = [1, 2, [3, 4]]
b = a  # Assignment: b dan a menunjuk objek YANG SAMA

print(f"a: {a}")
print(f"b: {b}")
print(f"a is b: {a is b}")  # True

# Modifikasi b juga mengubah a
b.append(5)
b[2][0] = 99

print(f"\nSetelah modifikasi b:")
print(f"a: {a}")  # Ikut berubah!
print(f"b: {b}")


# =============================================
# 2. SHALLOW COPY: copy.copy()
# =============================================

print("\n=== SHALLOW COPY ===")

a = [1, 2, [3, 4]]
b = copy.copy(a)

print(f"a: {a}")
print(f"b: {b}")
print(f"a is b: {a is b}")  # False: objek berbeda

# Modifikasi top-level tidak mempengaruhi a
b[0] = 99
b.append(100)

print(f"\nSetelah modifikasi top-level b:")
print(f"a: {a}")  # Tidak berubah
print(f"b: {b}")

# TAPI: nested object masih share reference!
b[2][0] = 999  # Ini MEMPERNGARUHI a!

print(f"\nSetelah modifikasi nested b[2][0]:")
print(f"a: {a}")  # a[2][0] juga berubah!
print(f"b: {b}")


# =============================================
# 3. DEEP COPY: copy.deepcopy()
# =============================================

print("\n=== DEEP COPY ===")

a = [1, 2, [3, 4]]
b = copy.deepcopy(a)

print(f"a: {a}")
print(f"b: {b}")
print(f"a is b: {a is b}")  # False

# Modifikasi nested tidak mempengaruhi a
b[2][0] = 999

print(f"\nSetelah modifikasi nested b[2][0]:")
print(f"a: {a}")  # Tidak berubah!
print(f"b: {b}")


# =============================================
# 4. PERBANDINGAN SHALLOW vs DEEP
# =============================================

print("\n=== PERBANDINGAN SHALLOW vs DEEP ===")

original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

# Modifikasi nested
original[0][0] = "CHANGED"

print(f"Original: {original}")
print(f"Shallow:  {shallow}")  # Ikut berubah
print(f"Deep:     {deep}")     # Tidak berubah


# =============================================
# 5. CUSTOM __copy__ DAN __deepcopy__
# =============================================

print("\n=== CUSTOM COPY ===")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __copy__(self):
        print("  __copy__ dipanggil")
        return Point(self.x, self.y)

    def __deepcopy__(self, memo):
        print(f"  __deepcopy__ dipanggil untuk {self}")
        return Point(copy.deepcopy(self.x, memo), copy.deepcopy(self.y, memo))


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"Line({self.start}, {self.end})"


p1 = Point(1, 2)
p2 = Point(3, 4)
line = Line(p1, p2)

print("Shallow copy Line:")
line_copy = copy.copy(line)
print(f"  start is same? {line_copy.start is line.start}")  # True
print(f"  end is same? {line_copy.end is line.end}")  # True

print("\nDeep copy Line:")
line_deep = copy.deepcopy(line)
print(f"  start is same? {line_deep.start is line.start}")  # False
print(f"  end is same? {line_deep.end is line.end}")  # False


# =============================================
# 6. COPY DENGAN memo (MENCEGAH INFINITE LOOP)
# =============================================

print("\n=== COPY DENGAN memo ===")


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __deepcopy__(self, memo):
        if id(self) in memo:
            return memo[id(self)]
        
        new_node = Node(copy.deepcopy(self.value, memo))
        memo[id(self)] = new_node
        new_node.next = copy.deepcopy(self.next, memo)
        return new_node


# Buat circular reference
a = Node(1)
b = Node(2)
a.next = b
b.next = a  # Circular!

# Deep copy tanpa memo = infinite loop!
a_copy = copy.deepcopy(a)
print(f"Original a: {a.value}, next: {a.next.value}")
print(f"Copy a: {a_copy.value}, next: {a_copy.next.value}")
print(f"a_copy.next.next is a_copy: {a_copy.next.next is a_copy}")  # True (circular di-copy juga)


# =============================================
# 7. COPY UNTUK COLLECTION TYPES
# =============================================

print("\n=== COPY COLLECTION TYPES ===")

# List
list_original = [[1, 2], [3, 4], [5, 6]]
list_shallow = copy.copy(list_original)
list_deep = copy.deepcopy(list_original)

list_original[0][0] = "CHANGED"
print(f"List shallow: {list_shallow}")  # Ikut berubah
print(f"List deep:    {list_deep}")     # Tidak berubah

# Dict
dict_original = {"a": [1, 2], "b": {"x": 10}}
dict_shallow = copy.copy(dict_original)
dict_deep = copy.deepcopy(dict_original)

dict_original["a"].append(3)
dict_original["b"]["x"] = 99

print(f"\nDict shallow a: {dict_shallow['a']}")  # Ikut berubah
print(f"Dict shallow b: {dict_shallow['b']}")    # Ikut berubah
print(f"Dict deep a:    {dict_deep['a']}")       # Tidak berubah
print(f"Dict deep b:    {dict_deep['b']}")       # Tidak berubah

# Set
set_original = {1, 2, 3}
set_copy = copy.copy(set_original)
print(f"\nSet copy: {set_copy}")
print(f"Set is same: {set_copy is set_original}")  # False


# =============================================
# 8. PERBANDINGAN KECEPATAN
# =============================================

print("\n=== PERBANDINGAN KECEPATAN ===")

import time

data = [[i, i*2, i*3] for i in range(1000)]

# Shallow
start = time.time()
for _ in range(10000):
    copy.copy(data)
shallow_time = time.time() - start

# Deep
start = time.time()
for _ in range(10000):
    copy.deepcopy(data)
deep_time = time.time() - start

print(f"Shallow copy (10k kali): {shallow_time:.3f}s")
print(f"Deep copy (10k kali):    {deep_time:.3f}s")
print(f"Deep lebih lambat:       {deep_time/shallow_time:.1f}x")
