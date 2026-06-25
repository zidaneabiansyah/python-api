"""
THREADING vs MULTIPROCESSING
==============================
 Threading: Multiple threads dalam 1 process (share memory)
 Multiprocessing: Multiple processes terpisah (tidak share memory)

何时用:
 - I/O bound (file, network, API) -> Thread
 - CPU bound (hitungan berat) -> Process
"""

import time
import threading
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from typing import List


# =============================================
# 1. THREADING DASAR
# =============================================

def io_task(name: str, duration: int) -> str:
    """Simulasi I/O task (download, read file, API call)"""
    print(f"  [{name}] Mulai (akan selesai dalam {duration}s)...")
    time.sleep(duration)  # Simulasi I/O wait
    print(f"  [{name}] Selesai!")
    return f"Hasil {name}"


print("=" * 60)
print("1. THREADING DASAR")
print("=" * 60)

# Sequential (satu per satu)
print("\n--- Sequential ---")
start = time.time()
io_task("Task-1", 2)
io_task("Task-2", 1)
io_task("Task-3", 1)
print(f"  Total: {time.time() - start:.2f}s")

# Concurrent (bersamaan pakai thread)
print("\n--- Threading ---")
start = time.time()
t1 = threading.Thread(target=io_task, args=("Thread-1", 2))
t2 = threading.Thread(target=io_task, args=("Thread-2", 1))
t3 = threading.Thread(target=io_task, args=("Thread-3", 1))

t1.start()
t2.start()
t3.start()

t1.join()  # Tunggu selesai
t2.join()
t3.join()
print(f"  Total: {time.time() - start:.2f}s")


# =============================================
# 2. THREAD POOL EXECUTOR
# =============================================

print("\n" + "=" * 60)
print("2. THREAD POOL EXECUTOR")
print("=" * 60)

def download(url: str) -> str:
    print(f"  Download {url}...")
    time.sleep(1)
    return f"File dari {url}"


urls = [
    "https://example.com/file1.zip",
    "https://example.com/file2.zip",
    "https://example.com/file3.zip",
    "https://example.com/file4.zip",
]

# Pakai ThreadPoolExecutor
print("\n--- ThreadPoolExecutor ---")
start = time.time()
with ThreadPoolExecutor(max_workers=3) as executor:
    # map() - hasil sesuai urutan input
    results = list(executor.map(download, urls))

print(f"  Hasil: {results}")
print(f"  Total: {time.time() - start:.2f}s")


# =============================================
# 3. MULTIPROCESSING DASAR
# =============================================

print("\n" + "=" * 60)
print("3. MULTIPROCESSING DASAR")
print("=" * 60)

def cpu_heavy(n: int) -> int:
    """Simulasi CPU bound task (hitungan berat)"""
    total = 0
    for i in range(n):
        total += i * i
    return total


N = 10_000_000

# Sequential
print("\n--- Sequential ---")
start = time.time()
cpu_heavy(N)
cpu_heavy(N)
cpu_heavy(N)
print(f"  3x CPU heavy: {time.time() - start:.2f}s")

# Concurrent (pakai process)
print("\n--- Multiprocessing ---")
start = time.time()
if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(cpu_heavy, N) for _ in range(3)]
        results = [f.result() for f in futures]
print(f"  3x CPU heavy: {time.time() - start:.2f}s")


# =============================================
# 4. PROCESS POOL EXECUTOR
# =============================================

print("\n" + "=" * 60)
print("4. PROCESS POOL EXECUTOR")
print("=" * 60)

def hitung_kuadrat(angka: int) -> int:
    """Hitung kuadrat (CPU bound)"""
    time.sleep(0.1)  # Simulasi
    return angka ** 2


angka = list(range(10))

print("\n--- ProcessPoolExecutor ---")
start = time.time()
if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=4) as executor:
        # map() - parallel
        results = list(executor.map(hitung_kuadrat, angka))

print(f"  Hasil: {results}")
print(f"  Total: {time.time() - start:.2f}s")


# =============================================
# 5. THREADING DENGAN LOCK (Synchronization)
# =============================================

print("\n" + "=" * 60)
print("5. THREAD LOCK (Synchronization)")
print("=" * 60)

counter = 0
lock = threading.Lock()

def increment_with_lock(n: int) -> None:
    global counter
    for _ in range(n):
        lock.acquire()  # Ambil lock
        try:
            counter += 1
        finally:
            lock.release()  # Lepas lock

# Tanpa lock (race condition)
def increment_no_lock(n: int) -> None:
    global counter
    for _ in range(n):
        counter += 1  # Race condition!

print("\n--- Tanpa Lock (Race Condition) ---")
counter = 0
threads = []
start = time.time()
for _ in range(5):
    t = threading.Thread(target=increment_no_lock, args=(100000,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print(f"  Counter: {counter} (seharusnya 500000)")
print(f"  Time: {time.time() - start:.2f}s")

print("\n--- Dengan Lock ---")
counter = 0
threads = []
start = time.time()
for _ in range(5):
    t = threading.Thread(target=increment_with_lock, args=(100000,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print(f"  Counter: {counter} (seharusnya 500000)")
print(f"  Time: {time.time() - start:.2f}s")


# =============================================
# 6. THREADING DENGAN QUEUE
# =============================================

print("\n" + "=" * 60)
print("6. THREADING DENGAN QUEUE")
print("=" * 60)

import queue

def producer(q: queue.Queue, items: List[str]) -> None:
    """Produksi item"""
    for item in items:
        time.sleep(0.5)
        q.put(item)
        print(f"  [Producer] Produksi: {item}")
    q.put(None)  # Sentinel

def consumer(q: queue.Queue, name: str) -> None:
    """Konsumsi item"""
    while True:
        item = q.get()
        if item is None:
            break
        time.sleep(0.3)
        print(f"  [{name}] Konsumsi: {item}")
        q.task_done()


print("\n--- Producer-Consumer ---")
q = queue.Queue()

# Buat producer dan consumer threads
prod_thread = threading.Thread(target=producer, args=(q, ["A", "B", "C", "D"]))
cons1_thread = threading.Thread(target=consumer, args=(q, "Cons-1"))
cons2_thread = threading.Thread(target=consumer, args=(q, "Cons-2"))

prod_thread.start()
cons1_thread.start()
cons2_thread.start()

prod_thread.join()
cons1_thread.join()
cons2_thread.join()


# =============================================
# 7. MULTIPROCESSING DENGAN SHAREDMEMORY
# =============================================

print("\n" + "=" * 60)
print("7. SHARED MEMORY (Multiprocessing)")
print("=" * 60)

from multiprocessing import Value, Array

def tambah_shared(counter: Value, n: int) -> None:
    """Tambah counter secara shared"""
    for _ in range(n):
        with counter.get_lock():
            counter.value += 1


print("\n--- Shared Counter ---")
if __name__ == "__main__":
    counter = Value('i', 0)  # Shared integer

    processes = []
    start = time.time()
    for _ in range(4):
        p = multiprocessing.Process(target=tambah_shared, args=(counter, 100000))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f"  Counter: {counter.value} (seharusnya 400000)")
    print(f"  Time: {time.time() - start:.2f}s")


# =============================================
# 8. CONCURRENT FUTURES - THREAD vs PROCESS
# =============================================

print("\n" + "=" * 60)
print("8. THREAD vs PROCESS COMPARISON")
print("=" * 60)

def io_bound_task(n: int) -> float:
    """I/O bound - thread lebih cocok"""
    time.sleep(0.1)
    return n * 2

def cpu_bound_task(n: int) -> int:
    """CPU bound - process lebih cocok"""
    total = 0
    for i in range(n):
        total += i
    return total


N_IO = 20
N_CPU = 1_000_000

# I/O Bound - Thread
print("\n--- I/O Bound Test ---")
start = time.time()
with ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(io_bound_task, range(N_IO)))
print(f"  Thread (I/O): {time.time() - start:.2f}s")

start = time.time()
with ProcessPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(io_bound_task, range(N_IO)))
print(f"  Process (I/O): {time.time() - start:.2f}s")

# CPU Bound - Process
print("\n--- CPU Bound Test ---")
start = time.time()
with ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(cpu_bound_task, [N_CPU]*4))
print(f"  Thread (CPU): {time.time() - start:.2f}s")

if __name__ == "__main__":
    start = time.time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(cpu_bound_task, [N_CPU]*4))
    print(f"  Process (CPU): {time.time() - start:.2f}s")


# =============================================
# 9. CONTOH NYATA - Web Scraper
# =============================================

print("\n" + "=" * 60)
print("9. CONTOH NYATA - Download Manager")
print("=" * 60)

from concurrent.futures import as_completed

def download_file(url: str) -> dict:
    """Simulasi download file"""
    size = len(url) * 10  # Simulasi ukuran
    time.sleep(0.5)
    return {"url": url, "size": size, "status": "OK"}


urls = [
    "https://example.com/file1.zip",
    "https://example.com/file2.zip",
    "https://example.com/file3.zip",
    "https://example.com/file4.zip",
    "https://example.com/file5.zip",
]

print("\n--- Download Manager ---")
start = time.time()

with ThreadPoolExecutor(max_workers=3) as executor:
    # Submit semua tasks
    future_to_url = {executor.submit(download_file, url): url for url in urls}

    # Process selesai (bisa urutan berbeda)
    for future in as_completed(future_to_url):
        url = future_to_url[future]
        try:
            result = future.result()
            print(f"  ✓ {result['url']} - {result['size']} bytes")
        except Exception as e:
            print(f"  ✗ {url} error: {e}")

print(f"  Total: {time.time() - start:.2f}s")


# =============================================
# RINGKASAN
# =============================================
print("\n" + "=" * 60)
print("RINGKASAN")
print("=" * 60)
print("""
Threading:
  + Share memory
  + Cocok untuk I/O bound
  + Lebih ringan
  - GIL (Global Interpreter Lock)
  - Tidak parallel di CPU bound

Multiprocessing:
  + True parallel
  + Cocok untuk CPU bound
  + Isolasi (crash tidak affect lain)
  - Tidak share memory
  - Lebih berat (overhead)
  - Perlu IPC untuk komunikasi

Kapan pakai:
  I/O bound (file, network, API) -> Thread
  CPU bound (hitungan, image processing) -> Process
  Mixed -> Pool Executor
""")
