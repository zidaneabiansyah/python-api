"""
ITERATOR PROTOCOL
=================
 Iterator Protocol terdiri dari dua method: __iter__ dan __next__
 __iter__ mengembalikan iterator itu sendiri
 __next__ mengembalikan elemen berikutnya atau raise StopIteration
"""

from itertools import islice


# =============================================
# 1. ITERABLE vs ITERATOR
# =============================================

print("=== ITERABLE vs ITERATOR ===")

# List adalah iterable (punya __iter__)
my_list = [10, 20, 30]
print(f"my_list punya __iter__: {hasattr(my_list, '__iter__')}")
print(f"my_list punya __next__: {hasattr(my_list, '__next__')}")

# iter() membuat iterator dari iterable
my_iter = iter(my_list)
print(f"my_iter punya __iter__: {hasattr(my_iter, '__iter__')}")
print(f"my_iter punya __next__: {hasattr(my_iter, '__next__')}")

# next() mengambil elemen satu per satu
print(f"next: {next(my_iter)}")
print(f"next: {next(my_iter)}")
print(f"next: {next(my_iter)}")


# =============================================
# 2. CUSTOM ITERATOR: COUNTDOWN
# =============================================

print("\n=== COUNTDOWN ITERATOR ===")


class Countdown:
    """Iterator hitung mundur dari start ke 1"""

    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1


countdown = Countdown(5)
print("Hitung mundur:", end=" ")
for num in countdown:
    print(num, end=" ")
print()


# =============================================
# 3. CUSTOM ITERATOR: FIBONACCI
# =============================================

print("\n=== FIBONACCI ITERATOR ===")


class Fibonacci:
    """Iterator Fibonacci sampai max_count"""

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


fib = list(Fibonacci(10))
print(f"Fibonacci 10 bilangan: {fib}")


# =============================================
# 4. ITERATOR vs GENERATOR
# =============================================

print("\n=== ITERATOR vs GENERATOR ===")


# Style Iterator (verbose)
class SquaresIterator:
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


# Style Generator (singkat)
def squares_generator(n):
    for i in range(n):
        yield i ** 2


print("Iterator style:", list(SquaresIterator(5)))
print("Generator style:", list(squares_generator(5)))


# =============================================
# 5. next() dengan DEFAULT VALUE
# =============================================

print("\n=== next() DENGAN DEFAULT ===")

it = iter([1, 2, 3])
print(f"next: {next(it)}")
print(f"next: {next(it)}")
print(f"next: {next(it)}")

# Default value jika iterator habis (tidak raise StopIteration)
habis = next(it, "Iterator sudah habis!")
print(f"Default: {habis}")


# =============================================
# 6. FOR LOOP = ITERATOR DI BALIK LAYAR
# =============================================

print("\n=== FOR LOOP DI BALIK LAYAR ===")

nums = [100, 200, 300]

# Cara for loop bekerja:
it = iter(nums)
while True:
    try:
        x = next(it)
        print(f"  Dapat: {x}")
    except StopIteration:
        print("  Selesai!")
        break


# =============================================
# 7. INFINITE ITERATOR
# =============================================

print("\n=== INFINITE ITERATOR ===")


class InfiniteCounter:
    """Counter tak hingga, gunakan islice untuk membatasi"""

    def __init__(self, start=0, step=1):
        self.current = start
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        value = self.current
        self.current += self.step
        return value


# Ambil 5 bilangan ganjil dari iterator tak hingga
counter = InfiniteCounter(start=1, step=2)
odd_five = list(islice(counter, 5))
print(f"5 bilangan ganjil pertama: {odd_five}")

# Ambil 8 bilangan genap
even_counter = InfiniteCounter(start=0, step=2)
even_eight = list(islice(even_counter, 8))
print(f"8 bilangan genap pertama: {even_eight}")


# =============================================
# 8. ITERATOR UNTUK OBJEK CUSTOM
# =============================================

print("\n=== ITERATOR PADA KOLEKSI ===")


class BookShelf:
    """Rak buku yang bisa diiterasi"""
    
    def __init__(self):
        self.books = []

    def add(self, book):
        self.books.append(book)

    def __iter__(self):
        return iter(self.books)  # Delegate ke list iterator

    def __len__(self):
        return len(self.books)


shelf = BookShelf()
shelf.add("Python Dasar")
shelf.add("Python Lanjutan")
shelf.add("Clean Code")

for book in shelf:
    print(f"  Buku: {book}")

# Menggunakan iterator manual
it = iter(shelf)
print(f"  Buku pertama: {next(it)}")
print(f"  Buku kedua: {next(it)}")


# =============================================
# 9. ITERABLE YANG BISA DIULANG
# =============================================

print("\n=== ITERABLE YANG BISA DIULANG ===")


class RepeatableRange:
    """Range yang bisa diiterasi berulang kali"""

    def __init__(self, stop):
        self.stop = stop

    def __iter__(self):
        return RangeIterator(self.stop)


class RangeIterator:
    def __init__(self, stop):
        self.stop = stop
        self.current = 0

    def __iter__(self):
        return self  # Mengembalikan iterator baru setiap kali

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        self.current += 1
        return self.current


r = RepeatableRange(3)

# Iterasi pertama
print("Iterasi pertama:", end=" ")
for x in r:
    print(x, end=" ")
print()

# Bisa diulang (karena __iter__ mengembalikan iterator baru)
print("Iterasi kedua:", end=" ")
for x in r:
    print(x, end=" ")
print()
