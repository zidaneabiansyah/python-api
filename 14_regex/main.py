import re

# 1. re.search — cari pattern pertama

teks = "Halo, email saya adalah budi@email.com dan andi@mail.com"

email = re.search(r"\S+@\S+", teks)
if email:
    print(f"search: {email.group()}")

# 2. re.findall — cari semua match

semua_email = re.findall(r"\S+@\S+", teks)
print(f"findall: {semua_email}")

# 3. re.match — cocok dari awal string

print(f"match 'Halo': {re.match(r'Halo', teks)}")
print(f"match 'email': {re.match(r'email', teks)}")

# 4. re.split — potong string pake pattern

kalimat = "apel,mangga;jeruk pisang"
hasil = re.split(r"[,; ]", kalimat)
print(f"split: {hasil}")

# 5. re.sub — replace pake pattern

sensor = re.sub(r"\S+@\S+", "[EMAIL]", teks)
print(f"sub: {sensor}")

# 6. group — ambil bagian tertentu

log = "ERROR 2025-01-15: Disk penuh"
pattern = r"(ERROR|WARN|INFO) (\d{4}-\d{2}-\d{2}): (.+)"
match = re.search(pattern, log)
if match:
    print(f"\nfull match: {match.group()}")
    print(f"group 1 (level): {match.group(1)}")
    print(f"group 2 (tanggal): {match.group(2)}")
    print(f"group 3 (pesan): {match.group(3)}")

# 7. named group — pake nama instead of angka

log2 = "ERROR 2025-06-18: Server crash"
pattern2 = r"(?P<level>\w+) (?P<tanggal>[\d-]+): (?P<pesan>.+)"
m = re.search(pattern2, log2)
if m:
    print(f"\nlevel: {m.group('level')}")
    print(f"tanggal: {m.group('tanggal')}")
    print(f"pesan: {m.group('pesan')}")

# 8. pola umum

data = """
Telpon: 0812-3456-7890
IP: 192.168.1.1
Web: https://example.com
"""

telp = re.findall(r"\d{4}-\d{4}-\d{4}", data)
ip = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", data)
url = re.findall(r"https?://\S+", data)

print(f"\ntelpon: {telp}")
print(f"ip: {ip}")
print(f"url: {url}")

# 9. compile — buat pattern sekali, pake berkali-kali

pattern_email = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
teks2 = "Hubungi support@company.com atau info@shop.net"
print(f"\ncompile findall: {pattern_email.findall(teks2)}")

# 10. flags — ubah behavior

teks3 = "Python\npython\nPYTHON"
print(f"IGNORECASE: {re.findall(r'python', teks3, re.IGNORECASE)}")
print(f"MULTILINE: {re.findall(r'^python', teks3, re.MULTILINE | re.IGNORECASE)}")

# RINGKASAN POLA REGEX:
# .       = karakter apapun
# \d      = digit (0-9)
# \w      = word character (a-z, A-Z, 0-9, _)
# \s      = whitespace (spasi, tab, newline)
# \S      = bukan whitespace
# ^       = awal string / baris
# $       = akhir string / baris
# *       = 0 atau lebih
# +       = 1 atau lebih
# ?       = 0 atau 1
# {n,m}   = n sampai m kali
# [...]   = salah satu karakter di dalam
# [^...]  = karakter yang TIDAK ada di dalam
# ()      = group
# |       = atau
