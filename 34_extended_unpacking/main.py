"""
EXTENDED UNPACKING
==================
 * (star) untuk unpacking list/tuple/list
 ** (double star) untuk unpacking dict
"""


# =============================================
# 1. UNPACKING DASAR
# =============================================

print("=== UNPACKING DASAR ===")

# Tuple unpacking
a, b, c = (1, 2, 3)
print(f"a={a}, b={b}, c={c}")

# List unpacking
x, y, z = [10, 20, 30]
print(f"x={x}, y={y}, z={z}")

# Swap
a, b = b, a
print(f"Setelah swap: a={a}, b={b}")

# Nested unpacking
(a, b), c = [1, 2], 3
print(f"a={a}, b={b}, c={c}")


# =============================================
# 2. * UNTUK LIST/TUPLE
# =============================================

print("\n=== * UNTUK LIST/TUPLE ===")

# first, *middle, last
data = [1, 2, 3, 4, 5]
first, *middle, last = data
print(f"first={first}, middle={middle}, last={last}")

# *head, last
*head, last = [1, 2, 3, 4]
print(f"head={head}, last={last}")

# first, *tail
first, *tail = [1, 2, 3, 4]
print(f"first={first}, tail={tail}")

# Hanya satu elemen
first, *rest = [42]
print(f"first={first}, rest={rest}")

# Semua ke *middle
*middle, = [1, 2, 3]
print(f"middle={middle}")


# =============================================
# 3. * UNTUK MERGE LIST/TUPLE
# =============================================

print("\n=== MERGE DENGAN * ===")

list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_c = [7, 8, 9]

# Gabungkan
merged = [*list_a, *list_b, *list_c]
print(f"Merged: {merged}")

# Dengan elemen tambahan
result = [0, *list_a, *list_b, 10]
print(f"Dengan tambahan: {result}")

# Set unpacking
set_a = {1, 2, 3}
set_b = {3, 4, 5}
merged_set = {*set_a, *set_b}
print(f"Set merged: {merged_set}")


# =============================================
# 4. ** UNTUK DICT
# =============================================

print("\n=== ** UNTUK DICT ===")

dict_a = {"a": 1, "b": 2}
dict_b = {"c": 3, "d": 4}

# Merge dict
merged_dict = {**dict_a, **dict_b}
print(f"Merged dict: {merged_dict}")

# Override
config = {"timeout": 30, "retries": 3, "debug": False}
override = {"timeout": 60, "debug": True}
final = {**config, **override}
print(f"Config final: {final}")

# Tambah elemen baru
extended = {**dict_a, "new_key": "new_value", **dict_b}
print(f"Extended: {extended}")


# =============================================
# 5. UNPACKING DI FUNCTION ARGUMENTS
# =============================================

print("\n=== UNPACKING DI FUNCTION ===")


def tambah(a, b, c):
    return a + b + c


def sapa(nama, salam="Halo"):
    return f"{salam}, {nama}!"


# *args: unpack list/tuple
args = [1, 2, 3]
print(f"tambah(*args): {tambah(*args)}")

# **kwargs: unpack dict
kwargs = {"a": 10, "b": 20, "c": 30}
print(f"tambah(**kwargs): {tambah(**kwargs)}")

# Mixed
print(f"sapa(*['Budi']): {sapa(*['Budi'])}")
print(f"sapa(**dict): {sapa(**{'nama': 'Andi', 'salam': 'Selamat pagi'})}")


# =============================================
# 6. UNPACKING DI FUNGSI DENGAN *args DAN **kwargs
# =============================================

print("\n=== FUNGSI DENGAN *args DAN **kwargs ===")


def flexible(*args, **kwargs):
    print(f"  args: {args}")
    print(f"  kwargs: {kwargs}")


print("Panggil 1:")
flexible(1, 2, 3, name="Budi", age=25)

print("\nPanggil 2:")
flexible(*[10, 20], **{"x": 1, "y": 2})

print("\nPanggil 3:")
flexible()


# =============================================
# 7. EXTENDED UNPACKING DI ASSIGNMENT
# =============================================

print("\n=== EXTENDED UNPACKING DI ASSIGNMENT ===")

# Beberapa pola
data = range(10)

a, *b = data
print(f"a={a}, b={b}")

*a, b = data
print(f"a={a}, b={b}")

a, *b, c = data
print(f"a={a}, b={b}, c={c}")

a, b, *c = data
print(f"a={a}, b={b}, c={c}")

a, b, *c, d = data
print(f"a={a}, b={b}, c={c}, d={d}")


# =============================================
# 8. REAL-WORLD: CONFIG MERGING
# =============================================

print("\n=== REAL-WORLD: CONFIG MERGING ===")

# Default config
default_config = {
    "host": "localhost",
    "port": 8080,
    "debug": False,
    "timeout": 30,
    "retries": 3,
}

# User override
user_config = {
    "host": "production.com",
    "port": 443,
    "debug": True,
}

# Environment-specific
env_config = {
    "timeout": 60,
}

# Final config (urutan: default < user < env)
final_config = {**default_config, **user_config, **env_config}
print(f"Final config: {final_config}")

# Tambah SSL
ssl_config = {**final_config, "ssl": True, "cert_path": "/etc/ssl/cert.pem"}
print(f"With SSL: {ssl_config}")


# =============================================
# 9. REAL-WORLD: FUNCTION WRAPPER
# =============================================

print("\n=== REAL-WORLD: FUNCTION WRAPPER ===")


def log_calls(func, *args, **kwargs):
    """Wrapper untuk logging pemanggilan fungsi"""
    print(f"  Memanggil {func.__name__}")
    print(f"  Args: {args}")
    print(f"  Kwargs: {kwargs}")
    result = func(*args, **kwargs)
    print(f"  Hasil: {result}")
    return result


def kali(a, b):
    return a * b


def pangkat(a, b=2):
    return a ** b


log_calls(kali, 3, 4)
log_calls(pangkat, 5, b=3)
