import logging

# 1. basic logging

logging.basicConfig(level=logging.DEBUG)

print("BASIC LOGGING")
logging.debug("pesan debug")
logging.info("info biasa")
logging.warning("ada peringatan!")
logging.error("terjadi error!")
logging.critical("kritis! sistem down!")

# 2. logging ke file

file_log = logging.getLogger("file_logger")
handler = logging.FileHandler("app.log")
handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
file_log.addHandler(handler)
file_log.setLevel(logging.INFO)

print("\nLOGGING KE FILE")
file_log.info("aplikasi mulai")
file_log.warning("memory hampir penuh")
file_log.error("koneksi database gagal")

with open("app.log") as f:
    print(f.read())

# 3. format custom

print("FORMAT CUSTOM")
console = logging.StreamHandler()
console.setFormatter(logging.Formatter("%(levelname)s | %(message)s"))

custom_log = logging.getLogger("custom")
custom_log.addHandler(console)
custom_log.setLevel(logging.INFO)

custom_log.info("ini pake format custom")

# 4. multiple handler

print("\nMULTIPLE HANDLER")
multi_log = logging.getLogger("multi")
multi_log.setLevel(logging.DEBUG)

file_h = logging.FileHandler("multi.log")
file_h.setLevel(logging.ERROR)
console_h = logging.StreamHandler()
console_h.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(message)s")
file_h.setFormatter(formatter)
console_h.setFormatter(formatter)

multi_log.addHandler(file_h)
multi_log.addHandler(console_h)

multi_log.info("info ini muncul di console doang")
multi_log.error("error ini muncul di console DAN file")

# 5. exception logging (traceback)

print("\nEXCEPTION LOGGING")
try:
    1 / 0
except ZeroDivisionError:
    logging.exception("terjadi error:")

import os
os.remove("app.log")
os.remove("multi.log")
