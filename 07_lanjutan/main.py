# 1. LIST COMPREHENSION

print("LIST COMPREHENSION")
kuadrat = [x**2 for x in range(5)]
print(f"Kuadrat: {kuadrat}")

genap = [x for x in range(10) if x % 2 == 0]
print(f"Genap: {genap}")

# 2. DICT COMPREHENSION

print("\nDICT COMPREHENSION")
kuadrat_dict = {x: x**2 for x in range(5)}
print(f"Dict kuadrat: {kuadrat_dict}")

# 3. SET COMPREHENSION

print("\nSET COMPREHENSION")
duplikat = [1, 2, 2, 3, 3, 4]
unik_kuadrat = {x**2 for x in duplikat}
print(f"Unik kuadrat: {unik_kuadrat}")

# 4. CLOSURE

print("\nCLOSURE")


def buat_counter():
    counter = 0

    def increment():
        nonlocal counter
        counter += 1
        return counter

    return increment


counter1 = buat_counter()
print(f"Counter 1: {counter1()}")
print(f"Counter 1: {counter1()}")
counter2 = buat_counter()
print(f"Counter 2: {counter2()}")
print(f"Counter 1 lagi: {counter1()}")

# 5. DECORATOR

print("\nDECORATOR")


def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Memanggil {func.__name__} dengan {args} {kwargs}")
        hasil = func(*args, **kwargs)
        print(f"Hasil: {hasil}")
        return hasil

    return wrapper


@logger
def luas_lingkaran(r):
    return 3.14 * r * r


print(f"Luas lingkaran r=7: {luas_lingkaran(7)}")

# decorator dengan argumen


def ulangi(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator


@ulangi(3)
def sapa(nama):
    print(f"Halo {nama}!")


print("\nDecorator dengan argumen:")
sapa("Budi")

# 6. GENERATOR

print("\nGENERATOR")


def counter_atas(maks):
    n = 0
    while n <= maks:
        yield n
        n += 1


for val in counter_atas(3):
    print(f"Counter: {val}")

# generator expression
print("\nGenerator expression:")
gen = (x**2 for x in range(5))
for val in gen:
    print(val)

# 7. CONTEXT MANAGER (with statement)

print("\nCONTEXT MANAGER")


class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


with FileManager("test.txt", "w") as f:
    f.write("Halo dari context manager!\n")

with FileManager("test.txt", "r") as f:
    print(f.read())

# context manager dengan contextlib
from contextlib import contextmanager


@contextmanager
def file_manager(filename, mode):
    f = open(filename, mode)
    yield f
    f.close()


with file_manager("test.txt", "r") as f:
    print(f.read())

# cleanup
import os
os.remove("test.txt")
print("File test.txt dihapus")
