"""
ABSTRACT BASE CLASSES (ABC)
===========================
 ABC mendefinisikan kontrak untuk class turunan
 Method abstract WAJIB diimplementasi oleh subclass
"""

from abc import ABC, abstractmethod
from collections.abc import Sequence


# =============================================
# 1. ABC DASAR
# =============================================

print("=== ABC DASAR ===")


class Hewan(ABC):
    """Base class untuk semua hewan"""

    @abstractmethod
    def bersuara(self):
        """Harus diimplementasi oleh subclass"""
        pass

    @abstractmethod
    def bergerak(self):
        pass

    # Method biasa (bukan abstract) bisa diwarisi
    def info(self):
        return f"Saya adalah {self.__class__.__name__}"


class Kucing(Hewan):
    def bersuara(self):
        return "Meow!"

    def bergerak(self):
        return "Berlari dengan 4 kaki"


class Burung(Hewan):
    def bersuara(self):
        return "Cuit!"

    def bergerak(self):
        return "Terbang dengan sayap"


kucing = Kucing()
burung = Burung()

print(f"Kucing: {kucing.bersuara()}, {kucing.bergerak()}")
print(f"Burung: {burung.bersuara()}, {burung.bergerak()}")
print(f"Info: {kucing.info()}")

# Tidak bisa instansiasi ABC langsung
try:
    hewan = Hewan()
except TypeError as e:
    print(f"\nError instansiasi ABC: {e}")


# =============================================
# 2. SHAPE - ABC DENGAN PROPERTY
# =============================================

print("\n=== SHAPE ABC ===")


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        return f"{self.__class__.__name__}: area={self.area():.2f}, perimeter={self.perimeter():.2f}"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, a, b, c, height):
        self.a = a
        self.b = b
        self.c = c
        self.height = height

    def area(self):
        return 0.5 * self.a * self.height

    def perimeter(self):
        return self.a + self.b + self.c


shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5, 4)]
for shape in shapes:
    print(f"  {shape.describe()}")


# =============================================
# 3. PLAYER DENGAN PROPERTY ABSTRACT
# =============================================

print("\n=== PLAYER PROPERTY ABSTRACT ===")


class Player(ABC):
    @property
    @abstractmethod
    def score(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def play(self):
        pass


class Gamer(Player):
    def __init__(self, _name, points):
        self._name = _name
        self._score = points

    @property
    def score(self):
        return self._score

    @property
    def name(self):
        return self._name

    def play(self):
        self._score += 10


gamer = Gamer("Budi", 100)
print(f"Nama: {gamer.name}, Score: {gamer.score}")
gamer.play()
print(f"Setelah bermain: {gamer.score}")


# =============================================
# 4. ABC DENGAN register()
# =============================================

print("\n=== ABC register() ===")


class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass


class Line:
    """Class tanpa inheritance dari Drawable"""
    def draw(self):
        return "Menggambar garis"


class Circle2:
    """Class lain tanpa inheritance"""
    def draw(self):
        return "Menggambar lingkaran"


# Register tanpa inheritance
Drawable.register(Line)
Drawable.register(Circle2)

# Cek subclass
print(f"Line issubclass Drawable: {issubclass(Line, Drawable)}")
print(f"Circle2 issubclass Drawable: {issubclass(Circle2, Drawable)}")

line = Line()
print(f"Line.draw(): {line.draw()}")


# =============================================
# 5. BUILT-IN ABC: collections.abc
# =============================================

print("\n=== COLLECTIONS.ABC ===")


# Membuat class yang memenuhi kontrak Sequence
class Playlist(Sequence):
    """Playlist musik yang memenuhi Sequence ABC"""

    def __init__(self):
        self._songs = []

    def add(self, song):
        self._songs.append(song)

    # Wajib diimplementasi untuk Sequence
    def __getitem__(self, index):
        return self._songs[index]

    def __len__(self):
        return len(self._songs)

    # Sekarang otomatis punya: __contains__, __iter__, __reversed__
    # index(), count() dari Sequence


playlist = Playlist()
playlist.add("Python Song")
playlist.add("Code Blues")
playlist.add("Debug Lullaby")

print(f"Lagu pertama: {playlist[0]}")
print(f"Jumlah lagu: {len(playlist)}")
print(f"'Code Blues' ada: {'Code Blues' in playlist}")
print(f"Index 'Debug Lullaby': {playlist.index('Debug Lullaby')}")
print(f"Semua lagu: {list(playlist)}")


# =============================================
# 6. MULTIPLE ABSTRACT METHODS
# =============================================

print("\n=== MULTIPLE ABSTRACT METHODS ===")


class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def query(self, sql):
        pass

    @abstractmethod
    def close(self):
        pass

    # Template method pattern
    def execute(self, sql):
        self.connect()
        result = self.query(sql)
        self.close()
        return result


class SQLiteDB(Database):
    def connect(self):
        print("  Connecting to SQLite...")

    def query(self, sql):
        print(f"  Executing: {sql}")
        return []

    def close(self):
        print("  Closing connection")


class PostgreSQLDB(Database):
    def connect(self):
        print("  Connecting to PostgreSQL...")

    def query(self, sql):
        print(f"  Executing: {sql}")
        return []

    def close(self):
        print("  Closing connection")


for db in [SQLiteDB(), PostgreSQLDB()]:
    print(f"\n{db.__class__.__name__}:")
    db.execute("SELECT * FROM users")


# =============================================
# 7. ABC DENGAN __init_subclass__
# =============================================

print("\n=== __init_subclass__ ===")


class Plugin(ABC):
    _registry = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if not getattr(cls, '__abstractmethods__', None):
            Plugin._registry[cls.__name__] = cls

    @abstractmethod
    def run(self):
        pass

    @classmethod
    def get_plugins(cls):
        return cls._registry.copy()


class AudioPlugin(Plugin):
    def run(self):
        return "Playing audio"


class VideoPlugin(Plugin):
    def run(self):
        return "Playing video"


print(f"Registered plugins: {Plugin.get_plugins()}")
for name, cls in Plugin.get_plugins().items():
    print(f"  {name}: {cls().run()}")
