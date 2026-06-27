"""
OS & SYS MODULE
================
 os: operasi file system, environment, process
 sys: system info, arguments, stdin/stdout
"""

import os
import sys
import tempfile


# =============================================
# 1. OS — CURRENT DIRECTORY & LIST
# =============================================

print("=== OS — CURRENT DIRECTORY ===")

cwd = os.getcwd()
print(f"Current directory: {cwd}")

# List contents
contents = os.listdir('.')
print(f"Contents ({len(contents)} items):")
for item in sorted(contents)[:5]:
    print(f"  {item}")
print("  ...")


# =============================================
# 2. OS — PATH OPERATIONS
# =============================================

print("\n=== OS — PATH OPERATIONS ===")

test_path = "/home/user/documents/report.txt"

print(f"basename: {os.path.basename(test_path)}")
print(f"dirname: {os.path.dirname(test_path)}")
print(f"splitext: {os.path.splitext(test_path)}")
print(f"join: {os.path.join('a', 'b', 'c.txt')}")
print(f"exists '.': {os.path.exists('.')}")
print(f"isdir '.': {os.path.isdir('.')}")
print(f"isfile '.': {os.path.isfile('.')}")

# Abspath
print(f"abspath('test.py'): {os.path.abspath('test.py')}")
print(f"expanduser('~/file'): {os.path.expanduser('~/file')}")


# =============================================
# 3. OS — FILE OPERATIONS
# =============================================

print("\n=== OS — FILE OPERATIONS ===")

# Buat temporary file
with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
    f.write("Hello from temp file!")
    temp_path = f.name

print(f"Temp file: {temp_path}")
print(f"Exists: {os.path.exists(temp_path)}")
print(f"Size: {os.path.getsize(temp_path)} bytes")

# Hapus
os.remove(temp_path)
print(f"After delete: {os.path.exists(temp_path)}")

# Buat temporary directory
temp_dir = tempfile.mkdtemp()
print(f"Temp dir: {temp_dir}")
print(f"Is dir: {os.path.isdir(temp_dir)}")
os.rmdir(temp_dir)
print(f"After rmdir: {os.path.exists(temp_dir)}")


# =============================================
# 4. OS — ENVIRONMENT VARIABLES
# =============================================

print("\n=== OS — ENVIRONMENT VARIABLES ===")

# Common env vars
home = os.environ.get('HOME', 'N/A')
path = os.environ.get('PATH', 'N/A')
user = os.environ.get('USER', 'N/A')

print(f"HOME: {home}")
print(f"USER: {user}")
print(f"PATH: {path[:60]}...")

# Set custom env var
os.environ['MY_APP_ENV'] = 'development'
print(f"MY_APP_ENV: {os.environ['MY_APP_ENV']}")


# =============================================
# 5. OS — PROCESS INFO
# =============================================

print("\n=== OS — PROCESS INFO ===")

print(f"PID: {os.getpid()}")
print(f"PPID: {os.getppid()}")
print(f"OS name: {os.name}")
print(f"Platform: {sys.platform}")


# =============================================
# 6. OS — MKDIR & DIRECTORY OPS
# =============================================

print("\n=== OS — MKDIR ===")

test_dir = tempfile.mkdtemp()
sub_dir = os.path.join(test_dir, "sub", "deep")
os.makedirs(sub_dir)
print(f"Created: {sub_dir}")
print(f"Exists: {os.path.exists(sub_dir)}")

# Cleanup
os.removedirs(sub_dir)
print(f"After removedirs: {os.path.exists(sub_dir)}")


# =============================================
# 7. SYS — VERSION & PLATFORM
# =============================================

print("\n=== SYS — VERSION & PLATFORM ===")

print(f"Python version: {sys.version}")
print(f"Version info: {sys.version_info[:3]}")
print(f"Platform: {sys.platform}")
print(f"Executable: {sys.executable}")
print(f"Byteorder: {sys.byteorder}")
print(f"Maxsize: {sys.maxsize}")


# =============================================
# 8. SYS — MODULE SEARCH PATH
# =============================================

print("\n=== SYS — MODULE PATH ===")

print(f"sys.path length: {len(sys.path)}")
print("First 3 paths:")
for p in sys.path[:3]:
    print(f"  {p}")


# =============================================
# 9. SYS — COMMAND LINE ARGUMENTS
# =============================================

print("\n=== SYS — ARGV ===")

print(f"Script: {sys.argv[0]}")
print(f"Argumen: {sys.argv[1:]}")
print(f"Jumlah argumen: {len(sys.argv)}")


# =============================================
# 10. SYS — RECURSION LIMIT
# =============================================

print("\n=== SYS — RECURSION LIMIT ===")

print(f"Recursion limit: {sys.getrecursionlimit()}")

# Contoh recursion
def factorial(n, depth=0):
    if depth > 10:
        return "Terlalu dalam!"
    if n <= 1:
        return 1
    return n * factorial(n - 1, depth + 1)

print(f"5! = {factorial(5)}")


# =============================================
# 11. SYS — stdin/stdout/stderr
# =============================================

print("\n=== SYS — STDIN/STDOUT ===")

# Tulis ke stdout langsung (tanpa newline)
sys.stdout.write("Ditulis ke stdout")
sys.stdout.write("\n")

# Tulis ke stderr
sys.stderr.write("Ditulis ke stderr\n")


# =============================================
# 12. REAL-WORLD: DISK USAGE CHECKER
# =============================================

print("\n=== REAL-WORLD: DISK USAGE ===")


def cek_disk_usage(path):
    """Cek ukuran direktori"""
    total = 0
    file_count = 0
    dir_count = 0

    for root, dirs, files in os.walk(path):
        dir_count += len(dirs)
        for f in files:
            filepath = os.path.join(root, f)
            try:
                total += os.path.getsize(filepath)
                file_count += 1
            except OSError:
                pass

    return {
        "path": path,
        "files": file_count,
        "dirs": dir_count,
        "size_mb": total / 1024 / 1024,
    }


# Cek current directory
info = cek_disk_usage(".")
print(f"  Path: {info['path']}")
print(f"  Files: {info['files']}")
print(f"  Dirs: {info['dirs']}")
print(f"  Size: {info['size_mb']:.2f} MB")


# =============================================
# 13. REAL-WORLD: ENV LOADER
# =============================================

print("\n=== REAL-WORLD: ENV LOADER ===")


def load_env(filepath=".env"):
    """Load env vars dari file"""
    env_vars = {}
    if not os.path.exists(filepath):
        return env_vars

    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                env_vars[key.strip()] = value.strip()

    return env_vars


# Simulasi
print(f"  load_env() result: {load_env()}")
