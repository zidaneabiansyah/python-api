"""
MATCH-CASE PATTERN MATCHING (Python 3.10+)
============================================
 Pattern matching adalah fitur baru Python 3.10+
 Lebih powerful dari switch-case di bahasa lain
"""


# =============================================
# 1. MATCH-CASE DASAR
# =============================================

print("=== MATCH-CASE DASAR ===")


def proses_perintah(command):
    match command:
        case "start":
            return "Memulai program..."
        case "stop":
            return "Menghentikan program..."
        case "pause":
            return "Menjeda program..."
        case _:
            return f"Perintah tidak dikenal: {command}"


print(proses_perintah("start"))
print(proses_perintah("stop"))
print(proses_perintah("unknown"))


# =============================================
# 2. LITERAL PATTERNS
# =============================================

print("\n=== LITERAL PATTERNS ===")


def http_status(code):
    match code:
        case 200:
            return "OK"
        case 301:
            return "Moved Permanently"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return f"Status {code}"


for code in [200, 404, 500, 418]:
    print(f"  {code}: {http_status(code)}")


# =============================================
# 3. CAPTURE PATTERNS
# =============================================

print("\n=== CAPTURE PATTERNS ===")


def identifikasi_titik(point):
    match point:
        case (0, 0):
            return "Origin"
        case (x, 0):
            return f"Di sumbu X: x={x}"
        case (0, y):
            return f"Di sumbu Y: y={y}"
        case (x, y):
            return f"Titik umum: ({x}, {y})"


titik_test = [(0, 0), (5, 0), (0, 3), (4, 7)]
for t in titik_test:
    print(f"  {t}: {identifikasi_titik(t)}")


# =============================================
# 4. WILDCARD PATTERN (_)
# =============================================

print("\n=== WILDCARD PATTERN ===")


def evaluasi_nilai(score):
    match score:
        case 100:
            return "Sempurna!"
        case s if s >= 80:
            return f"Bagus ({s})"
        case s if s >= 60:
            return f"Cukup ({s})"
        case _:
            return f"Perlu perbaikan ({score})"


for s in [100, 85, 65, 45]:
    print(f"  Score {s}: {evaluasi_nilai(s)}")


# =============================================
# 5. GUARD (if)
# =============================================

print("\n=== GUARD (if) ===")


def kategori_usia(age):
    match age:
        case n if n < 0:
            return "Tidak valid"
        case n if n < 13:
            return "Anak-anak"
        case n if n < 18:
            return "Remaja"
        case n if n < 65:
            return "Dewasa"
        case _:
            return "Lansia"


for age in [-5, 10, 16, 30, 70]:
    print(f"  Usia {age}: {kategori_usia(age)}")


# =============================================
# 6. OR PATTERN (|)
# =============================================

print("\n=== OR PATTERN ===")


def proses_status(status):
    match status:
        case "success" | "ok" | "done":
            return "Berhasil!"
        case "error" | "fail" | "failed":
            return "Gagal!"
        case "pending" | "waiting":
            return "Menunggu..."
        case _:
            return f"Status: {status}"


for s in ["success", "error", "pending", "unknown"]:
    print(f"  {s}: {proses_status(s)}")


# =============================================
# 7. SEQUENCE PATTERNS
# =============================================

print("\n=== SEQUENCE PATTERNS ===")


def proses_list(items):
    match items:
        case []:
            return "Kosong"
        case [single]:
            return f"Satu item: {single}"
        case [first, second]:
            return f"Dua item: {first}, {second}"
        case [first, *rest]:
            return f"First: {first}, Rest: {rest}"


lists = [[], [42], [1, 2], [1, 2, 3, 4, 5]]
for lst in lists:
    print(f"  {lst}: {proses_list(lst)}")


# =============================================
# 8. MAPPING PATTERNS
# =============================================

print("\n=== MAPPING PATTERNS ===")


def proses_user(user):
    match user:
        case {"name": name, "age": age, "role": "admin"}:
            return f"Admin: {name} (umur {age})"
        case {"name": name, "age": age}:
            return f"User: {name} (umur {age})"
        case {"name": name}:
            return f"User: {name} (tanpa info)"
        case {}:
            return "Data kosong"


users = [
    {"name": "Budi", "age": 25, "role": "admin"},
    {"name": "Andi", "age": 30},
    {"name": "Citra"},
    {},
]

for u in users:
    print(f"  {u}: {proses_user(u)}")


# =============================================
# 9. CLASS PATTERNS
# =============================================

print("\n=== CLASS PATTERNS ===")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


def describe_shape(shape):
    match shape:
        case Point(x=0, y=0):
            return "Origin"
        case Point(x=x, y=0):
            return f"Di sumbu X: {x}"
        case Point(x=0, y=y):
            return f"Di sumbu Y: {y}"
        case Point(x=x, y=y):
            return f"Titik ({x}, {y})"
        case Rectangle(width=w, height=h) if w == h:
            return f"Square {w}x{h}"
        case Rectangle(width=w, height=h):
            return f"Rectangle {w}x{h}"
        case _:
            return "Shape tidak dikenal"


shapes = [Point(0, 0), Point(5, 0), Point(0, 3), Point(4, 7),
          Rectangle(5, 5), Rectangle(3, 4)]
for s in shapes:
    print(f"  {s}: {describe_shape(s)}")


# =============================================
# 10. NESTED PATTERNS
# =============================================

print("\n=== NESTED PATTERNS ===")


def proses_data(data):
    match data:
        case {"user": {"name": str(name), "address": {"city": str(city)}}}:
            return f"{name} tinggal di {city}"
        case {"user": {"name": str(name), "age": int(age)}} if age > 18:
            return f"{name} dewasa (umur {age})"
        case {"user": {"name": str(name)}}:
            return f"{name} (data tidak lengkap)"
        case {"error": msg}:
            return f"Error: {msg}"
        case _:
            return "Data tidak valid"


data_list = [
    {"user": {"name": "Budi", "address": {"city": "Jakarta"}}},
    {"user": {"name": "Andi", "age": 25}},
    {"user": {"name": "Citra"}},
    {"error": "Connection failed"},
    "invalid",
]

for d in data_list:
    print(f"  {proses_data(d)}")


# =============================================
# 11. REAL-WORLD: COMMAND PARSER
# =============================================

print("\n=== REAL-WORLD: COMMAND PARSER ===")


def parse_command(command):
    match command.split():
        case ["get", resource]:
            return f"Mengambil {resource}"
        case ["get", resource, "where", *conditions]:
            return f"Mengambil {resource} dengan kondisi: {conditions}"
        case ["set", resource, value]:
            return f"Mengatur {resource} = {value}"
        case ["delete", resource]:
            return f"Menghapus {resource}"
        case ["help"]:
            return "Commands: get, set, delete, help"
        case _:
            return f"Command tidak valid: {command}"


commands = [
    "get users",
    "get users where active=true limit=10",
    "set name Budi",
    "delete post 123",
    "help",
    "unknown command",
]

for cmd in commands:
    print(f"  > {cmd}")
    print(f"    {parse_command(cmd)}")
