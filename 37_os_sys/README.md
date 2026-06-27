# `os` & `sys` Module dalam Python

## Daftar Isi
1. [os — File System Operations](#1-os--file-system-operations)
2. [os — Environment Variables](#2-os--environment-variables)
3. [os — Path Operations](#3-os--path-operations)
4. [os — Process Management](#4-os--process-management)
5. [sys — System Info](#5-sys--system-info)
6. [sys — Command Line Arguments](#6-sys--command-line-arguments)
7. [sys — stdin/stdout/stderr](#7-sys--stdinstdoutstderr)
8. [sys — Recursion Limit](#8-sys--recursion-limit)

---

## 1. os — File System Operations

```python
import os

# Current directory
os.getcwd()

# List directory
os.listdir('.')
os.listdir('/home')

# Create/remove
os.mkdir('new_dir')
os.makedirs('a/b/c')  # Recursive
os.rmdir('new_dir')
os.removedirs('a/b/c')

# Rename
os.rename('old.txt', 'new.txt')

# File info
os.path.exists('file.txt')
os.path.isfile('file.txt')
os.path.isdir('dir/')
os.path.getsize('file.txt')
os.stat('file.txt').st_mtime  # Modified time
```

---

## 2. os — Environment Variables

```python
import os

# Baca env var
home = os.environ.get('HOME')
path = os.environ.get('PATH')

# Set env var (hanya untuk session ini)
os.environ['MY_VAR'] = 'hello'

# Hapus
del os.environ['MY_VAR']
```

---

## 3. os — Path Operations

```python
import os

path = '/home/user/docs/file.txt'

os.path.basename(path)    # 'file.txt'
os.path.dirname(path)     # '/home/user/docs'
os.path.splitext(path)    # ('/home/user/docs/file', '.txt')
os.path.join('a', 'b', 'c')  # 'a/b/c'
os.path.abspath('file.txt')   # Absolute path
os.path.expanduser('~/file')  # '/home/user/file'
```

---

## 4. os — Process Management

```python
import os

# Process ID
os.getpid()
os.getppid()  # Parent PID

# Jalankan command
os.system('ls -la')

# Environment
os.name  # 'posix' (Linux/Mac) atau 'nt' (Windows)
```

---

## 5. sys — System Info

```python
import sys

sys.version       # Versi Python
sys.platform      # 'linux', 'darwin', 'win32'
sys.executable    # Path python executable
sys.path          # Module search path
sys.maxsize       # Integer terbesar
sys.byteorder     # 'little' atau 'big'
```

---

## 6. sys — Command Line Arguments

```python
import sys

# sys.argv adalah list argument dari command line
# python script.py arg1 arg2
print(sys.argv[0])  # script.py
print(sys.argv[1])  # arg1
print(sys.argv[2])  # arg2
```

---

## 7. sys — stdin/stdout/stderr

```python
import sys

# Tulis ke stdout
sys.stdout.write("Hello\n")

# Tulis ke stderr
sys.stderr.write("Error!\n")

# Baca dari stdin
line = sys.stdin.readline()
```

---

## 8. sys — Recursion Limit

```python
import sys

# Default: 1000
print(sys.getrecursionlimit())

# Ubah limit
sys.setrecursionlimit(5000)
```
