from pathlib import Path

# 1. Path dasar

print("PATH DASAR")
p = Path("contoh.txt")
print(f"objek path: {p}")
print(f"nama file: {p.name}")
print(f"stem (tanpa ext): {p.stem}")
print(f"extension: {p.suffix}")

# 2. absolute path

p2 = Path.cwd() / "data" / "lagu.mp3"
print(f"\nabsolute path: {p2}")
print(f"parent: {p2.parent}")
print(f"parents: {[str(x) for x in p2.parents]}")
print(f"drive/root: {p2.anchor}")

# 3. cek file/folder

print("\nCEK FILE")
home = Path.home()
print(f"home: {home}")
print(f"exists: {home.exists()}")
print(f"is_dir: {home.is_dir()}")
print(f"is_file: {home.is_file()}")

# 4. bikin folder & rename

print("\nOPERASI")
folder_baru = Path("test_folder")
folder_baru.mkdir(exist_ok=True)
print(f"folder dibuat: {folder_baru}")

file_baru = Path("test_folder/halo.txt")
file_baru.write_text("Halo dari pathlib!")
print(f"file dibuat: {file_baru}")
print(f"isi: {file_baru.read_text()}")

# rename
file_baru.rename("test_folder/hello.txt")
print(f"rename jadi: {Path('test_folder/hello.txt')}")

# hapus
Path("test_folder/hello.txt").unlink()
folder_baru.rmdir()
print("file & folder dibersihkan")

# 5. glob — cari file dengan pattern

print("\nGLOB")
base = Path(".")
for py_file in base.glob("**/main.py"):
    print(f"  {py_file}")

# 6. iterasi folder

print("\nITERASI FOLDER")
for entry in base.iterdir():
    if entry.is_dir():
        print(f"  [DIR] {entry.name}")
