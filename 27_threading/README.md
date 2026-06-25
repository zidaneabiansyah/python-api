# Threading vs Multiprocessing dalam Python

## Daftar Isi
1. [Perbedaan Dasar](#1-perbedaan-dasar)
2. [Threading](#2-threading)
3. [Multiprocessing](#3-multiprocessing)
4. [Synchronization](#4-synchronization)
5. [Queue](#5-queue)
6. [Kapan Pakai](#6-kapan-pakai)

---

## 1. Perbedaan Dasar

| Fitur | Threading | Multiprocessing |
|-------|-----------|-----------------|
| Memory | Share | Terpisah |
| Overhead | Ringan | Berat |
| GIL | Ya (blocked) | Tidak |
| I/O Bound | ✅ Cocok | ✅ Bisa |
| CPU Bound | ❌ Tidak | ✅ Cocok |
| Communication | Share memory | IPC (Queue, Pipe) |

---

## 2. Threading

### Basic
```python
import threading

def task(name):
    print(f"Task {name}")

# Buat thread
t = threading.Thread(target=task, args=("A",))
t.start()
t.join()  # Tunggu selesai
```

### Thread Pool
```python
from concurrent.futures import ThreadPoolExecutor

def download(url):
    # Simulasi download
    return f"File dari {url}"

urls = ["url1", "url2", "url3"]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(download, urls))
```

### GIL (Global Interpreter Lock)
- Python hanya menjalankan 1 thread per CPU core
- Thread tidak efisien untuk CPU bound tasks
- Tapi bagus untuk I/O bound (network, file, database)

---

## 3. Multiprocessing

### Basic
```python
import multiprocessing

def cpu_heavy(n):
    return sum(i*i for i in range(n))

if __name__ == "__main__":
    p = multiprocessing.Process(target=cpu_heavy, args=(1000000,))
    p.start()
    p.join()
```

### Process Pool
```python
from concurrent.futures import ProcessPoolExecutor

def hitung(n):
    return sum(i*i for i in range(n))

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(hitung, [1000000]*4))
```

### Shared Memory
```python
from multiprocessing import Value, Array

counter = Value('i', 0)  # Shared integer

def increment(counter):
    with counter.get_lock():
        counter.value += 1
```

---

## 4. Synchronization

### Lock
```python
lock = threading.Lock()

counter = 0
def increment():
    global counter
    for _ in range(100000):
        with lock:  # Ambil lock
            counter += 1
        # Lock dilepas otomatis
```

### RLock (Reentrant Lock)
```python
rlock = threading.RLock()

# Bisa di-lock berkali-kali oleh thread yang sama
with rlock:
    with rlock:  # OK! Reentrant
        pass
```

### Semaphore
```python
sem = threading.Semaphore(3)  # Maks 3 concurrent

def task():
    with sem:  # Ambil tiket
        # Bisa diakses max 3 thread sekaligus
        pass
```

---

## 5. Queue

### Producer-Consumer Pattern
```python
import queue

q = queue.Queue()

def producer():
    for i in range(10):
        q.put(i)
    q.put(None)  # Sentinel

def consumer():
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Proses: {item}")

# Queue thread-safe!
```

---

## 6. Kapan Pakai

### Pakai Thread untuk:
- ✅ Download/upload files
- ✅ API calls
- ✅ Database queries
- ✅ File I/O
- ✅ Web scraping

### Pakai Process untuk:
- ✅ Image/video processing
- ✅ Data computation
- ✅ Machine learning
- ✅ Mathematical calculations
- ✅ Any CPU-intensive work

---

## Best Practices

1. **Gunakan Pool Executor** - Lebih mudah dari manage thread/process manual
2. **Hindari Shared State** - Gunakan Queue untuk komunikasi
3. **Gunakan Lock** - Untuk shared mutable state
4. **Naming** - Beri nama thread/process untuk debugging
5. **Daemon** - Thread/process yang dijadiakan daemon akan mati saat main program selesai

```python
t = threading.Thread(target=task, daemon=True)
t.start()
# Main program selesai -> thread juga selesai
```
