# 1. IMPORT MODULE BUILT-IN

import math
import random
from datetime import datetime

print("MODULE BUILT-IN")
print(f"Akar 16: {math.sqrt(16)}")
print(f"Random 1-10: {random.randint(1, 10)}")
print(f"Sekarang: {datetime.now()}")

# 2. IMPORT CUSTOM MODULE

import matematika

print("\nCUSTOM MODULE")
print(f"5 + 3 = {matematika.tambah(5, 3)}")
print(f"10 - 4 = {matematika.kurang(10, 4)}")
print(f"PI: {matematika.PI}")

# 3. FROM ... IMPORT

from matematika import kali, bagi

print("\nFROM ... IMPORT")
print(f"6 * 7 = {kali(6, 7)}")
print(f"10 / 2 = {bagi(10, 2)}")

# 4. IMPORT DENGAN ALIAS

import matematika as mt

print("\nIMPORT ALIAS")
print(f"8 + 2 = {mt.tambah(8, 2)}")

# 5. IMPORT DARI PACKAGE

from package_example import sapa
from package_example.sapa import sapa_pagi

print("\nPACKAGE")
sapa.sapa("Budi")
sapa_pagi("Andi")

# 6. DIR — lihat isi module

print("\nDIR MODULE")
print(dir(matematika))
