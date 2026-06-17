from functools import partial, lru_cache, wraps, reduce

# 1. partial — bikin fungsi baru dengan argumen tetap

def pangkat(angka, eksponen):
    return angka ** eksponen

kuadrat = partial(pangkat, eksponen=2)
kubik = partial(pangkat, eksponen=3)

print("PARTIAL")
print(f"kuadrat 5: {kuadrat(5)}")
print(f"kubik 3: {kubik(3)}")

# 2. lru_cache — cache hasil fungsi (biar ga hitung ulang)

print("\nLRU CACHE")

@lru_cache(maxsize=32)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"fibonacci 10: {fibonacci(10)}")
print(f"fibonacci 20: {fibonacci(20)}")
print(f"cache info: {fibonacci.cache_info()}")
print(f"fibonacci 10 (cached): {fibonacci(10)}")
print(f"cache info: {fibonacci.cache_info()}")

# 3. wraps — jaga metadata fungsi asli dari decorator

print("\nWRAPS")

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"  panggil {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def sapa(nama):
    """Menyapa seseorang"""
    return f"Halo {nama}!"

print(sapa("Budi"))
print(f"nama fungsi: {sapa.__name__}")
print(f"docstring: {sapa.__doc__}")
# tanpa wraps, __name__ jadi 'wrapper'

# 4. reduce — akumulasi tiap item

print("\nREDUCE")

angka = [1, 2, 3, 4, 5]
total = reduce(lambda a, b: a + b, angka)
print(f"sum pake reduce: {total}")

faktorial = reduce(lambda a, b: a * b, range(1, 6))
print(f"5! pake reduce: {faktorial}")
