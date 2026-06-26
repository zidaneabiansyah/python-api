"""
MULTIPLE INHERITANCE & MRO
===========================
 Multiple Inheritance: class mewarisi lebih dari satu parent
 MRO (Method Resolution Order): urutan pencarian method
 Menggunakan C3 Linearization
"""


# =============================================
# 1. MULTIPLE INHERITANCE DASAR
# =============================================

print("=== MULTIPLE INHERITANCE DASAR ===")


class Telepon:
    def __init__(self):
        self.baterai = 100

    def telepon(self):
        return "Menelepon..."

    def info(self):
        return f"Baterai: {self.baterai}%"


class Kamera:
    def __init__(self):
        self.resolusi = "12MP"

    def foto(self):
        return f"Mengambil foto {self.resolusi}"

    def info(self):
        return f"Kamera: {self.resolusi}"


class Smartphone(Telepon, Kamera):
    def __init__(self, merek):
        Telepon.__init__(self)
        Kamera.__init__(self)
        self.merek = merek

    def info(self):
        return f"{self.merek} | {Telepon.info(self)} | {Kamera.info(self)}"


hp = Smartphone("Samsung")
print(f"Telepon: {hp.telepon()}")
print(f"Foto: {hp.foto()}")
print(f"Info: {hp.info()}")


# =============================================
# 2. DIAMOND PROBLEM
# =============================================

print("\n=== DIAMOND PROBLEM ===")

#      A
#     / \
#    B   C
#     \ /
#      D


class A:
    def greet(self):
        return "Halo dari A"


class B(A):
    def greet(self):
        return "Halo dari B"


class C(A):
    def greet(self):
        return "Halo dari C"


class D(B, C):
    pass


d = D()
print(f"D.greet(): {d.greet()}")  # B lebih dulu
print(f"MRO: {[cls.__name__ for cls in D.__mro__]}")


# =============================================
# 3. MRO (METHOD RESOLUTION ORDER)
# =============================================

print("\n=== MRO ===")


class X:
    def greet(self):
        return "X"


class Y(X):
    def greet(self):
        return "Y"


class Z(X):
    def greet(self):
        return "Z"


class W(Y, Z):
    pass


print(f"W.greet(): {W().greet()}")
print(f"W.__mro__: {[cls.__name__ for cls in W.__mro__]}")
print(f"W.mro(): {[cls.__name__ for cls in W.mro()]}")


# =============================================
# 4. super() DENGAN MULTIPLE INHERITANCE
# =============================================

print("\n=== super() DENGAN MULTIPLE INHERITANCE ===")


class Base:
    def __init__(self):
        print("  Base.__init__")


class Left(Base):
    def __init__(self):
        super().__init__()
        print("  Left.__init__")


class Right(Base):
    def __init__(self):
        super().__init__()
        print("  Right.__init__")


class Diamond(Left, Right):
    def __init__(self):
        super().__init__()
        print("  Diamond.__init__")


print("Diamond initialization:")
d = Diamond()

print(f"\nMRO: {[cls.__name__ for cls in Diamond.__mro__]}")


# =============================================
# 5. MIXIN PATTERN
# =============================================

print("\n=== MIXIN PATTERN ===")


class JsonMixin:
    """Mixin untuk serialisasi JSON"""
    def to_json(self):
        import json
        return json.dumps(self.__dict__, indent=2)


class LogMixin:
    """Mixin untuk logging"""
    def log(self, msg):
        print(f"  [{self.__class__.__name__}] {msg}")


class ValidasiMixin:
    """Mixin untuk validasi"""
    def validate(self):
        errors = []
        for field, value in self.__dict__.items():
            if value is None or value == "":
                errors.append(f"{field} tidak boleh kosong")
        return errors


class User(JsonMixin, LogMixin, ValidasiMixin):
    def __init__(self, name, email):
        self.name = name
        self.email = email


user = User("Budi", "budi@email.com")
print(f"JSON:\n{user.to_json()}")
user.log("User berhasil dibuat!")

# Cek semua mixin methods
print(f"Ada to_json: {hasattr(user, 'to_json')}")
print(f"Ada log: {hasattr(user, 'log')}")
print(f"Ada validate: {hasattr(user, 'validate')}")


# =============================================
# 6. MIXIN REAL-WORLD: CACHE
# =============================================

print("\n=== CACHE MIXIN ===")


class CacheMixin:
    """Mixin untuk caching sederhana"""
    def __init__(self):
        super().__init__()
        self._cache = {}

    def cached(self, key, func, *args):
        if key not in self._cache:
            self._cache[key] = func(*args)
        return self._cache[key]

    def clear_cache(self):
        self._cache.clear()


class APIClient(CacheMixin):
    def __init__(self):
        super().__init__()
        self.base_url = "https://api.example.com"

    def get_user(self, user_id):
        def fetch():
            return {"id": user_id, "name": f"User {user_id}"}
        return self.cached(f"user_{user_id}", fetch)


client = APIClient()
print(f"User 1: {client.get_user(1)}")
print(f"User 1 (cached): {client.get_user(1)}")
print(f"Cache size: {len(client._cache)}")


# =============================================
# 7. isinstance() DAN issubclass()
# =============================================

print("\n=== isinstance DAN issubclass ===")


class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Puppy(Dog):
    pass

dog = Dog()
puppy = Puppy()

# isinstance
print(f"dog is Animal: {isinstance(dog, Animal)}")
print(f"dog is Dog: {isinstance(dog, Dog)}")
print(f"puppy is Dog: {isinstance(puppy, Dog)}")
print(f"puppy is Animal: {isinstance(puppy, Animal)}")

# issubclass
print(f"Dog subclass Animal: {issubclass(Dog, Animal)}")
print(f"Puppy subclass Dog: {issubclass(Puppy, Dog)}")
print(f"Puppy subclass Animal: {issubclass(Puppy, Animal)}")


# =============================================
# 8. MRO DENGAN super() CHAINING
# =============================================

print("\n=== super() CHAINING ===")


class A:
    def process(self):
        return ["A"]


class B(A):
    def process(self):
        return super().process() + ["B"]


class C(A):
    def process(self):
        return super().process() + ["C"]


class D(B, C):
    def process(self):
        return super().process() + ["D"]


d = D()
print(f"Process chain: {d.process()}")
print(f"MRO: {[cls.__name__ for cls in D.__mro__]}")
