import sqlite3

conn = sqlite3.connect("belajar.db")
cursor = conn.cursor()

# 1. CREATE TABLE

print("CREATE TABLE")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS mahasiswa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT NOT NULL,
        jurusan TEXT,
        angkatan INTEGER
    )
""")
print("tabel mahasiswa siap")

# 2. INSERT

print("\nINSERT")
cursor.execute("INSERT INTO mahasiswa (nama, jurusan, angkatan) VALUES (?, ?, ?)",
               ("Budi", "Informatika", 2022))
cursor.execute("INSERT INTO mahasiswa (nama, jurusan, angkatan) VALUES (?, ?, ?)",
               ("Andi", "Sistem Informasi", 2022))
cursor.execute("INSERT INTO mahasiswa (nama, jurusan, angkatan) VALUES (?, ?, ?)",
               ("Siti", "Informatika", 2023))
cursor.execute("INSERT INTO mahasiswa (nama, jurusan, angkatan) VALUES (?, ?, ?)",
               ("Rina", "Teknik Komputer", 2023))
conn.commit()
print("4 data berhasil ditambahkan")

# 3. SELECT

print("\nSELECT semua:")
cursor.execute("SELECT * FROM mahasiswa")
for row in cursor.fetchall():
    print(f"  {row}")

print("\nSELECT where:")
cursor.execute("SELECT * FROM mahasiswa WHERE jurusan = ?", ("Informatika",))
for row in cursor.fetchall():
    print(f"  {row}")

print("\nSELECT satu baris:")
cursor.execute("SELECT * FROM mahasiswa WHERE id = ?", (1,))
print(f"  {cursor.fetchone()}")

# 4. UPDATE

print("\nUPDATE")
cursor.execute("UPDATE mahasiswa SET angkatan = ? WHERE nama = ?", (2024, "Budi"))
conn.commit()

cursor.execute("SELECT * FROM mahasiswa WHERE nama = ?", ("Budi",))
print(f"  setelah update: {cursor.fetchone()}")

# 5. DELETE

print("\nDELETE")
cursor.execute("DELETE FROM mahasiswa WHERE nama = ?", ("Rina",))
conn.commit()

cursor.execute("SELECT * FROM mahasiswa")
print("  sisa data:")
for row in cursor.fetchall():
    print(f"  {row}")

# 6. with statement (auto commit & close)

print("\nWITH STATEMENT")
with sqlite3.connect("belajar.db") as conn2:
    cursor2 = conn2.cursor()
    cursor2.execute("SELECT * FROM mahasiswa")
    print(f"  data via with: {cursor2.fetchall()}")
# auto conn2.close()

# 7. INNER JOIN (contoh relasi)

print("\nINNER JOIN")
cursor.execute("CREATE TABLE IF NOT EXISTS nilai (id_mahasiswa INTEGER, matkul TEXT, nilai INTEGER)")
cursor.executemany("INSERT INTO nilai VALUES (?, ?, ?)", [
    (1, "Matematika", 85),
    (1, "Fisika", 78),
    (2, "Matematika", 90),
    (3, "Fisika", 88),
])
conn.commit()

cursor.execute("""
    SELECT m.nama, n.matkul, n.nilai
    FROM mahasiswa m
    JOIN nilai n ON m.id = n.id_mahasiswa
""")
print("  hasil join:")
for row in cursor.fetchall():
    print(f"  {row}")

import os
conn.close()
os.remove("belajar.db")
print("\nfile database dihapus")
