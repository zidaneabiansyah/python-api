import json

# 1. Python -> JSON (serialization / dump)

data = {
    "nama": "Budi",
    "umur": 25,
    "menikah": False,
    "hobi": ["coding", "membaca"],
    "alamat": {
        "kota": "Jakarta",
        "provinsi": "DKI Jakarta"
    }
}

json_str = json.dumps(data, indent=2)
print("Python ke JSON:")
print(json_str)

# compact (tanpa indent)
json_compact = json.dumps(data)
print(f"\ncompact: {json_compact}")

# 2. JSON -> Python (deserialization / load)

json_data = '{"nama": "Andi", "umur": 30, "menikah": true}'
parsed = json.loads(json_data)
print(f"\nJSON ke Python: {parsed}")
print(f"nama: {parsed['nama']}")
print(f"umur: {parsed['umur']}")

# 3. JSON ke file

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
print("\ndata.json berhasil dibuat")

# 4. JSON dari file

with open("data.json", "r") as f:
    data_baca = json.load(f)
print(f"baca dari file: {data_baca}")

# 5. error handling

invalid_json = '{"nama": "Budi"'
try:
    json.loads(invalid_json)
except json.JSONDecodeError as e:
    print(f"\nerror parsing JSON: {e}")

# 6. tipe data mapping

# Python          JSON
# dict            object
# list, tuple     array
# str             string
# int, float      number
# True/False      true/false
# None            null

print("\ntipe data mapping:")
print(f"  None -> {json.dumps(None)}")
print(f"  tuple (1,2) -> {json.dumps((1, 2))}")
print(f"  True -> {json.dumps(True)}")

import os
os.remove("data.json")
