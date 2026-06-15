from datetime import datetime, date, time, timedelta

# 1. datetime sekarang

sekarang = datetime.now()
print(f"sekarang: {sekarang}")
print(f"tahun: {sekarang.year}")
print(f"bulan: {sekarang.month}")
print(f"hari: {sekarang.day}")
print(f"jam: {sekarang.hour}")
print(f"menit: {sekarang.minute}")
print(f"detik: {sekarang.second}")

# 2. date & time terpisah

hari_ini = date.today()
print(f"\nhari ini: {hari_ini}")

waktu = time(14, 30, 0)
print(f"waktu: {waktu}")

# 3. membuat datetime sendiri

tgl_lahir = datetime(2000, 1, 15, 8, 30)
print(f"\ntgl lahir: {tgl_lahir}")

# 4. format datetime (strftime)

print(f"\nformat 1: {sekarang.strftime('%d/%m/%Y')}")
print(f"format 2: {sekarang.strftime('%A, %d %B %Y')}")
print(f"format 3: {sekarang.strftime('%H:%M:%S')}")
print(f"format 4: {sekarang.strftime('%Y-%m-%d %H:%M')}")

# format code umum:
# %d = day (01-31)
# %m = month (01-12)
# %Y = year (2026)
# %H = hour (00-23)
# %M = minute (00-59)
# %S = second (00-59)
# %A = weekday name
# %B = month name

# 5. parse string ke datetime (strptime)

tgl_str = "15-01-2025 14:30"
parsed = datetime.strptime(tgl_str, "%d-%m-%Y %H:%M")
print(f"\nparsed: {parsed}")

# 6. timedelta — operasi waktu

sekarang = datetime.now()
tiga_hari_lagi = sekarang + timedelta(days=3)
print(f"\n3 hari lagi: {tiga_hari_lagi}")

seminggu_lalu = sekarang - timedelta(weeks=1)
print(f"seminggu lalu: {seminggu_lalu}")

# selisih waktu
selisih = tiga_hari_lagi - sekarang
print(f"selisih: {selisih.days} hari, {selisih.seconds} detik")

beda = timedelta(hours=5, minutes=30)
print(f"5 jam 30 menit: {beda}")

# 7. perbandingan datetime

tgl1 = datetime(2025, 1, 1)
tgl2 = datetime(2025, 6, 15)
print(f"\ntgl1 < tgl2: {tgl1 < tgl2}")
print(f"tgl1 == tgl2: {tgl1 == tgl2}")
