# 1. split & join

kalimat = "saya-belajar-python"
kata_list = kalimat.split("-")
print(f"split: {kata_list}")

gabung = " ".join(kata_list)
print(f"join: {gabung}")

# 2. strip, lstrip, rstrip

teks = "  halo dunia  "
print(f"strip: '{teks.strip()}'")
print(f"lstrip: '{teks.lstrip()}'")
print(f"rstrip: '{teks.rstrip()}'")

# 3. upper, lower, capitalize, title

nama = "budi prasetio"
print(f"upper: {nama.upper()}")
print(f"lower: {'BUDI'.lower()}")
print(f"capitalize: {nama.capitalize()}")
print(f"title: {nama.title()}")

# 4. replace

teks2 = "saya suka apel"
print(f"replace: {teks2.replace('apel', 'mangga')}")

# 5. find, index, count

teks3 = "saya suka suka suka python"
print(f"find 'suka': {teks3.find('suka')}")
print(f"rfind 'suka': {teks3.rfind('suka')}")
print(f"count 'suka': {teks3.count('suka')}")

# 6. startswith, endswith

filename = "laporan.pdf"
print(f"startswith 'laporan': {filename.startswith('laporan')}")
print(f"endswith '.pdf': {filename.endswith('.pdf')}")

# 7. isalpha, isdigit, isnumeric, isspace

print(f"'abc'.isalpha: {'abc'.isalpha()}")
print(f"'123'.isdigit: {'123'.isdigit()}")
print(f"'  '.isspace: {'  '.isspace()}")

# 8. format string

nama = "Budi"
umur = 25
print(f"f-string: {nama} berumur {umur}")
print("format: {} berumur {}".format(nama, umur))
print("index: {0} umur {1}, halo {0}".format(nama, umur))

# 9. zfill, center, ljust, rjust

angka = "42"
print(f"zfill 5: {angka.zfill(5)}")
print(f"center 10: '{angka.center(10)}'")
print(f"ljust 10: '{angka.ljust(10, '.')}'")
print(f"rjust 10: '{angka.rjust(10, '.')}'")
