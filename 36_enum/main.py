"""
ENUM MODULE
===========
 Enum membuat konstanta terbatas dengan nama
 Lebih baik dari magic strings/numbers
"""

from enum import Enum, auto, IntEnum, Flag, IntFlag


# =============================================
# 1. BASIC ENUM
# =============================================

print("=== BASIC ENUM ===")


class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4


# Akses
d = Direction.NORTH
print(f"Value: {d}")           # Direction.NORTH
print(f"Value: {d.value}")     # 1
print(f"Name: {d.name}")       # "NORTH"
print(f"Repr: {repr(d)}")      # <Direction.NORTH: 1>


# =============================================
# 2. ENUM DENGAN STRING VALUE
# =============================================

print("\n=== ENUM DENGAN STRING VALUE ===")


class Status(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    CANCELLED = "cancelled"


for status in Status:
    print(f"  {status.name} = {status.value}")

# Cari berdasarkan value
s = Status("approved")
print(f"\nCari 'approved': {s}")
print(f"Is approved: {s == Status.APPROVED}")


# =============================================
# 3. AUTO
# =============================================

print("\n=== AUTO ===")


class Priority(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    CRITICAL = auto()


for p in Priority:
    print(f"  {p.name} = {p.value}")


# =============================================
# 4. ENUM DENGAN TUPLE VALUE
# =============================================

print("\n=== ENUM DENGAN TUPLE VALUE ===")


class Color(Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)


for color in Color:
    r, g, b = color.value
    print(f"  {color.name}: RGB({r}, {g}, {b})")


# =============================================
# 5. METHOD DI ENUM
# =============================================

print("\n=== METHOD DI ENUM ===")


class Status(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"

    def is_terminal(self):
        """Cek apakah status adalah terminal (sudah selesai)"""
        return self in (Status.APPROVED, Status.REJECTED)

    @classmethod
    def from_string(cls, s):
        """Konversi string ke Enum"""
        for status in cls:
            if status.value == s:
                return status
        raise ValueError(f"Unknown status: {s}")


# Test methods
print(f"  PENDING is_terminal: {Status.PENDING.is_terminal()}")
print(f"  APPROVED is_terminal: {Status.APPROVED.is_terminal()}")

# from_string
s = Status.from_string("rejected")
print(f"  from_string('rejected'): {s}")


# =============================================
# 6. ITERASI ENUM
# =============================================

print("\n=== ITERASI ENUM ===")


class Hari(Enum):
    SENIN = 1
    SELASA = 2
    RABU = 3
    KAMIS = 4
    JUMAT = 5
    SABTU = 6
    MINGGU = 7


print("Semua hari:")
for hari in Hari:
    print(f"  {hari.name} = {hari.value}")

# Cari berdasarkan value
print(f"\nHari ke-3: {Hari(3)}")
print(f"Hari 'SENIN': {Hari['SENIN']}")


# =============================================
# 7. ENUM SEBAGAI DICT KEY
# =============================================

print("\n=== ENUM SEBAGAI DICT KEY ===")


class Status(Enum):
    PENDING = 1
    APPROVED = 2
    REJECTED = 3


# Enum hashable (punya __hash__)
counter = {Status.PENDING: 0, Status.APPROVED: 0, Status.REJECTED: 0}

transaksi = [Status.PENDING, Status.APPROVED, Status.PENDING, Status.REJECTED, Status.APPROVED]
for t in transaksi:
    counter[t] += 1

print("  Counter:", {k.name: v for k, v in counter.items()})


# =============================================
# 8. INTENUM
# =============================================

print("\n=== INTENUM ===")


class Level(IntEnum):
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50


# IntEnum bisa dibandingkan dengan int
print(f"  DEBUG == 10: {Level.DEBUG == 10}")
print(f"  INFO > 15: {Level.INFO > 15}")
print(f"  WARNING + 5: {Level.WARNING + 5}")


# =============================================
# 9. FLAG
# =============================================

print("\n=== FLAG ===")


class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()
    ADMIN = READ | WRITE | EXECUTE


print(f"  READ: {Permission.READ}")
print(f"  READ | WRITE: {Permission.READ | Permission.WRITE}")
print(f"  ADMIN: {Permission.ADMIN}")
print(f"  Has READ in ADMIN: {Permission.READ in Permission.ADMIN}")
print(f"  Has WRITE in ADMIN: {Permission.WRITE in Permission.ADMIN}")


# =============================================
# 10. REAL-WORLD: API STATUS
# =============================================

print("\n=== REAL-WORLD: API STATUS ===")


class APIStatus(Enum):
    SUCCESS = "success"
    ERROR = "error"
    LOADING = "loading"
    IDLE = "idle"

    def to_dict(self):
        return {"status": self.value, "name": self.name.lower()}

    @property
    def is_ok(self):
        return self == APIStatus.SUCCESS


class HTTPMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"

    def __str__(self):
        return self.value

    @property
    def is_safe(self):
        """HTTP method yang aman (tidak mengubah data)"""
        return self == HTTPMethod.GET


for method in HTTPMethod:
    safe = "safe" if method.is_safe else "unsafe"
    print(f"  {method} ({safe})")


# =============================================
# 11. ENUM DAN MATCH-CASE
# =============================================

print("\n=== ENUM DAN MATCH-CASE ===")


class Command(Enum):
    START = "start"
    STOP = "stop"
    PAUSE = "pause"
    RESTART = "restart"


def proses_command(cmd):
    match cmd:
        case Command.START:
            return "Memulai..."
        case Command.STOP:
            return "Berhenti..."
        case Command.PAUSE:
            return "Menjeda..."
        case Command.RESTART:
            return "Memulai ulang..."


for cmd in Command:
    print(f"  {cmd.name}: {proses_command(cmd)}")
