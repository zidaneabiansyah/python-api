import asyncio
import time

# =============================================
# 1. KENAPA PERLU ASYNC?
# =============================================
# Bayangkan kamu masak mie instan sambil nyeduh kopi.
# - Kamu rebus air (tunggu 3 menit) -> sambil nunggu, kamu nyeduh kopi
# - Itulah ASYNC: ngerjakan hal lain sambil nunggu I/O
#
# TANPA async (synchronous):
#   rebus_air() -> 3 menit
#   nyeduh_kopi() -> 2 menit
#   Total: 5 menit
#
# PAKE async (concurrent):
#   rebus_air() + nyeduh_kopi() berjalan BERGANTIAN
#   Total: ~3 menit (lebih cepat!)

print("=" * 50)
print("1. SYNC vs ASYNC - Perbandingan")
print("=" * 50)


def tugas_sync(nama, durasi):
    print(f"  [SYNC] {nama} mulai...")
    time.sleep(durasi)
    print(f"  [SYNC] {nama} selesai ({durasi}s)")
    return f"Hasil {nama}"


async def tugas_async(nama, durasi):
    print(f"  [ASYNC] {nama} mulai...")
    await asyncio.sleep(durasi)
    print(f"  [ASYNC] {nama} selesai ({durasi}s)")
    return f"Hasil {nama}"


async def main_perbandingan():
    print("\n--- Sync: jalan URUT ---")
    start = time.time()
    tugas_sync("Masak nasi", 2)
    tugas_sync("Goreng telur", 1)
    print(f"  Sync total: {time.time() - start:.2f}s")

    print("\n--- Async: jalan BERGANTIAN (concurrent) ---")
    start = time.time()
    # asyncio.gather() = jalankan banyak task sekaligus
    await asyncio.gather(
        tugas_async("Masak nasi", 2),
        tugas_async("Goreng telur", 1),
    )
    print(f"  Async total: {time.time() - start:.2f}s")


asyncio.run(main_perbandingan())


# =============================================
# 2. DASAR-DASAR ASYNC
# =============================================

print("\n" + "=" * 50)
print("2. DASAR-DASAR ASYNC")
print("=" * 50)


async def sapa(nama):
    """Fungsi async: pake `async def`"""
    await asyncio.sleep(1)  # await = "tunggu bentar, sambil jalanin yg lain"
    return f"Halo {nama}!"


async def main_dasar():
    # Cara panggil fungsi async: pake await
    hasil = await sapa("Budi")
    print(f"  {hasil}")

    # Kalo lupa await, dapet coroutine object, bukan hasilnya
    print("  (Kalo lupa await -> dapet coroutine object, bukan hasil)")


asyncio.run(main_dasar())


# =============================================
# 3. create_task - Jalanin Background
# =============================================

print("\n" + "=" * 50)
print("3. CREATE TASK - Background task")
print("=" * 50)

# create_task() = bikin task yang jalan di background
# Cocok kalo kita mau jalanin sesuatu tanpa nunggu selesai


async def proses_lama():
    print("  [TASK] Proses lama mulai...")
    await asyncio.sleep(3)
    print("  [TASK] Proses lama selesai!")
    return "Data penting"


async def main_task():
    # Bikin task (jalan di background)
    task = asyncio.create_task(proses_lama())

    print("  [MAIN] Lagi ngapa-ngapain...")
    await asyncio.sleep(1)
    print("  [MAIN] Masih ngapa-ngapain...")

    # Ambil hasil task (nanti, kalo udah selesai)
    hasil = await task
    print(f"  [MAIN] Hasil task: {hasil}")


asyncio.run(main_task())


# =============================================
# 4. asyncio.gather - Jalanin Banyak Sekaligus
# =============================================

print("\n" + "=" * 50)
print("4. GATHER - Jalanin banyak task")
print("=" * 50)


async def download_file(nama, ukuran_mb):
    print(f"  Download {nama} ({ukuran_mb}MB)...")
    await asyncio.sleep(ukuran_mb * 0.5)  # simulasi kecepatan
    print(f"  {nama} selesai!")
    return f"{nama} - OK"


async def main_gather():
    hasil = await asyncio.gather(
        download_file("foto1.jpg", 2),
        download_file("video.mp4", 4),
        download_file("dokumen.pdf", 1),
    )
    print(f"  Semua selesai: {hasil}")

    # Alternatif: pake list
    files = [
        ("foto2.jpg", 1),
        ("musik.mp3", 3),
    ]
    tasks = [download_file(nama, size) for nama, size in files]
    hasil2 = await asyncio.gather(*tasks)
    print(f"  Batch 2: {hasil2}")


asyncio.run(main_gather())


# =============================================
# 5. asyncio.wait_for - Timeout
# =============================================

print("\n" + "=" * 50)
print("5. TIMEOUT - Batas waktu")
print("=" * 50)


async def lambat():
    await asyncio.sleep(10)
    return "Lambat banget"


async def main_timeout():
    try:
        # Kasih batas 2 detik, kalo lewat throw TimeoutError
        hasil = await asyncio.wait_for(lambat(), timeout=2)
        print(f"  Hasil: {hasil}")
    except asyncio.TimeoutError:
        print("  Timeout! Task terlalu lama (＞﹏＜)")


asyncio.run(main_timeout())


# =============================================
# 6. ASYNC CONTEXT MANAGER
# =============================================

print("\n" + "=" * 50)
print("6. ASYNC CONTEXT MANAGER")
print("=" * 50)


class DatabaseConnection:
    """Simulasi koneksi database"""

    async def __aenter__(self):
        print("  [DB] Membuka koneksi...")
        await asyncio.sleep(0.5)
        print("  [DB] Koneksi siap!")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("  [DB] Menutup koneksi...")
        await asyncio.sleep(0.3)
        print("  [DB] Koneksi ditutup")

    async def query(self, sql):
        await asyncio.sleep(0.5)
        return f"Hasil dari: {sql}"


async def main_async_cm():
    async with DatabaseConnection() as db:
        hasil = await db.query("SELECT * FROM users")
        print(f"  {hasil}")
    # otomatis panggil __aexit__


asyncio.run(main_async_cm())


# =============================================
# 7. ASYNC GENERATOR
# =============================================

print("\n" + "=" * 50)
print("7. ASYNC GENERATOR - async for")
print("=" * 50)


async def angka_berurutan(maks):
    """Async generator: pake `async for` buat iterate"""
    for i in range(maks):
        await asyncio.sleep(0.3)  # simulasi I/O tiap dapet angka
        yield i


async def main_async_gen():
    print("  Ngitung pake async generator:")
    async for angka in angka_berurutan(5):
        print(f"  Dapet angka: {angka}")


asyncio.run(main_async_gen())


# =============================================
# 8. CONTOH NYATA - Simulasi API Calls
# =============================================

print("\n" + "=" * 50)
print("8. CONTOH NYATA - Ambil data dari API")
print("=" * 50)

import random


async def panggil_api(endpoint, delay):
    """Simulasi panggil API public"""
    print(f"  [API] GET /{endpoint}...")
    await asyncio.sleep(delay)
    return {"endpoint": endpoint, "data": f"data dari {endpoint}", "status": 200}


async def main_nyata():
    print("\n  --- Async: 3 API call concurrent ---")
    start = time.time()

    # Bayangkan kita perlu data dari 3 API berbeda
    user_task = asyncio.create_task(panggil_api("users", 2))
    produk_task = asyncio.create_task(panggil_api("products", 3))
    order_task = asyncio.create_task(panggil_api("orders", 1))

    # Kita bisa ngapa-ngapain sambil nunggu
    print("  [MAIN] Sambil nunggu API, kita preprocessing...")
    await asyncio.sleep(0.5)
    print("  [MAIN] Preprocessing selesai!")
    print("  [MAIN] Data dari API mana yg duluan dateng?")

    # Cek siapa yg duluan selesai
    done, pending = await asyncio.wait(
        [user_task, produk_task, order_task],
        return_when=asyncio.FIRST_COMPLETED,
    )

    for task in done:
        hasil = task.result()
        print(f"  >>> {hasil['endpoint']} duluan selesai! {hasil}")

    # Tunggu sisanya
    if pending:
        print(f"  [MAIN] Nunggu {len(pending)} sisanya...")
        await asyncio.wait(pending)

    print(f"\n  [MAIN] Semua selesai dalam {time.time() - start:.2f}s")


asyncio.run(main_nyata())


# =============================================
# 9. SEMAPHORE - Batasi Concurrency
# =============================================

print("\n" + "=" * 50)
print("9. SEMAPHORE - Batasi jumlah task bersamaan")
print("=" * 50)

# Berguna kalo mau download 100 file tapi ga mau overload server


async def download_with_limit(sem, file_id):
    async with sem:  # ambil "tiket"
        print(f"  Download file #{file_id}...")
        await asyncio.sleep(random.uniform(0.5, 1.5))
        print(f"  File #{file_id} selesai!")
        return file_id


async def main_semaphore():
    sem = asyncio.Semaphore(3)  # maks 3 download bersamaan
    tasks = [download_with_limit(sem, i) for i in range(10)]
    hasil = await asyncio.gather(*tasks)
    print(f"  Semua file selesai: {hasil}")


asyncio.run(main_semaphore())


# =============================================
# RINGKASAN
# =============================================
# async def  -> bikin fungsi async
# await      -> panggil fungsi async (nunggu hasil)
# asyncio.run()  -> jalanin fungsi async pertama
# create_task()  -> jalanin task di background
# gather()       -> jalanin banyak task concurrent
# wait_for()     -> kasih timeout
# async with     -> async context manager
# async for      -> async generator
# Semaphore()    -> batasi jumlah task bersamaan
# wait()         -> tunggu task sampe kondisi tertentu

print("\n" + "=" * 50)
print("SELESAI! 🚀")
print("=" * 50)
