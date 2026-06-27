"""
WALRUS OPERATOR (:=)
====================
 Python 3.8+ walrus operator menugaskan nilai ke variabel
 sekaligus mengembalikan nilainya dalam satu ekspresi
"""


# =============================================
# 1. TANPA WALRUS vs DENGAN WALRUS
# =============================================

print("=== TANPA WALRUS vs DENGAN WALRUS ===")

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Tanpa walrus: panggil len() 2 kali
n1 = len(data)
if n1 > 5:
    print(f"Tanpa walrus: panjang {n1} > 5")

# Dengan walrus: panggil len() 1 kali
if (n := len(data)) > 5:
    print(f"Dengan walrus: panjang {n} > 5")


# =============================================
# 2. WALRUS DI IF
# =============================================

print("\n=== WALRUS DI IF ===")

angka = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Cek apakah ada bilangan > 8
if (maks := max(angka)) > 8:
    print(f"Maksimum: {maks}")

# Cek apakah ada bilangan genap
if (genap := [x for x in angka if x % 2 == 0]):
    print(f"Bilangan genap: {genap}")

# Sorting
if (terurut := sorted(angka)) != angka:
    print(f"Belum terurut! Urutan benar: {terurut}")


# =============================================
# 3. WALRUS DI WHILE
# =============================================

print("\n=== WALRUS DI WHILE ===")

# Simulasi input dengan list
inputs = ["hello", "world", "", "python", ""]
input_iter = iter(inputs)

# Tanpa walrus (DRY)
print("Tanpa walrus:")
while True:
    line = next(input_iter, "")
    if line == "":
        break
    print(f"  Input: {line}")

# Dengan walrus
input_iter = iter(inputs)
print("Dengan walrus:")
while (line := next(input_iter, "")) != "":
    print(f"  Input: {line}")


# =============================================
# 4. WALRUS DI LIST COMPREHENSION
# =============================================

print("\n=== WALRUS DI LIST COMPREHENSION ===")

# Filter dengan transform
angka = [1, -2, 3, -4, 5, -6, 0, 7]

# Ambil nilai absolut yang > 2
abs_besar = [y for x in angka if (y := abs(x)) > 2]
print(f"Abs > 2: {abs_besar}")

# Filter + panjang
kata = ["hi", "hello", "python", "world", "code", "programming"]
panjang_5 = [(k, len(k)) for k in kata if (l := len(k)) >= 5]
print(f"Panjang >= 5: {panjang_5}")


# =============================================
# 5. WALRUS DI FILTER & LAMBDA
# =============================================

print("\n=== WALRUS DI FILTER & LAMBDA ===")

data = [10, 25, 3, 48, 7, 92, 15]

# Filter angka yang kuadratnya > 100
kuadrat_besar = list(filter(lambda x: (x2 := x**2) > 100, data))
print(f"Kuadrat > 100: {kuadrat_besar}")

# Map dengan walrus
hasil = list(map(lambda x: (k := x**2) + x, data[:5]))
print(f"x² + x: {hasil}")


# =============================================
# 6. WALRUS DI FUNGSI
# =============================================

print("\n=== WALRUS DI FUNGSI ===")


def proses_data(data):
    """Proses data dengan walrus untuk DRY"""
    if (n := len(data)) == 0:
        return "Data kosong"
    elif n == 1:
        return f"Satu item: {data[0]}"
    elif n <= 3:
        return f"Sedikit: {data}"
    else:
        return f"Banyak ({n} items)"


print(proses_data([]))
print(proses_data([42]))
print(proses_data([1, 2]))
print(proses_data([1, 2, 3, 4, 5]))


# =============================================
# 7. WALRUS DI EXCEPTION HANDLING
# =============================================

print("\n=== WALRUS DI EXCEPTION ===")


def safe_divide(a, b):
    """Bagi dengan aman, tangkap ZeroDivisionError"""
    try:
        return a / b
    except ZeroDivisionError:
        return None


results = [(a, safe_divide(10, a)) for a in [2, 0, 5, 0, 1]]
for angka, hasil in results:
    if hasil is not None:
        print(f"  10/{angka} = {hasil}")
    else:
        print(f"  10/{angka} = ERROR (div by zero)")


# =============================================
# 8. WALRUS DI SET COMPREHENSION
# =============================================

print("\n=== WALRUS DI SET COMPREHENSION ===")

kata = ["hello", "world", "hi", "python", "code"]

# Panjang unik dari kata
panjang_unik = {l for k in kata if (l := len(k)) > 2}
print(f"Panjang unik > 2: {panjang_unik}")

# Huruf pertama unik
huruf_pertama = {h for k in kata if (h := k[0]) not in {'h', 'w'}}
print(f"Huruf pertama bukan h/w: {huruf_pertama}")


# =============================================
# 9. WALRUS DI DICT COMPREHENSION
# =============================================

print("\n=== WALRUS DI DICT COMPREHENSION ===")

angka = [1, 2, 3, 4, 5]

# Dict dengan kuadrat
kuadrat_dict = {x: x**2 for x in angka if x**2 > 5}
print(f"Kuadrat > 5: {kuadrat_dict}")

# Dict dari list of tuples
items = [("a", 1), ("b", 2), ("c", 3)]
dict_filtered = {k: v * 10 for k, v in items if v > 1}
print(f"Filtered & multiplied: {dict_filtered}")


# =============================================
# 10. REAL-WORLD: PARSING LOG
# =============================================

print("\n=== REAL-WORLD: PARSING LOG ===")

logs = [
    "2024-01-15 ERROR: Connection timeout",
    "2024-01-15 INFO: User login",
    "2024-01-15 WARNING: Disk space low",
    "2024-01-15 ERROR: Database error",
]

# Ekstrak level dari log
errors = [msg for log in logs if (parts := log.split()) and (level := parts[1]) == "ERROR"]
print(f"Errors: {errors}")

# Hitung per level
from collections import Counter
levels = [log.split()[1] for log in logs]
print(f"Level count: {dict(Counter(levels))}")
