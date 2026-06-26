"""
Testing __slots__
=================
 Jalankan: pytest test_slots.py -v
"""

import pytest
import sys
from main import PointDefault, PointSlots, User, Animal, Dog, Puppy, StrictClass, Vector, Point3D


# 1. TEST DEFAULT vs SLOTS

def test_default_punya_dict():
    assert hasattr(PointDefault(1, 2), '__dict__')

def test_slots_tidak_punya_dict():
    assert not hasattr(PointSlots(1, 2), '__dict__')

def test_slots_punya_slots():
    assert hasattr(PointSlots(1, 2), '__slots__')


# 2. TEST ATTRIBUTE ACCESS

def test_slots_attribute():
    p = PointSlots(5, 10)
    assert p.x == 5
    assert p.y == 10


# 3. TEST SLOTS TIDAK BISA TAMBAH ATTRIBUTE

def test_slots_tidak_bisa_tambah():
    p = PointSlots(1, 2)
    with pytest.raises(AttributeError):
        p.z = 3


# 4. TEST USER DENGAN PROPERTY

def test_user_property():
    user = User("Budi", "budi@email.com", 25)
    assert user.name == "Budi"
    assert user.age == 25

def test_user_age_setter():
    user = User("Budi", "budi@email.com", 25)
    user.age = 30
    assert user.age == 30

def test_user_age_negatif():
    user = User("Budi", "budi@email.com", 25)
    with pytest.raises(ValueError):
        user.age = -5


# 5. TEST INHERITANCE

def test_dog_slots():
    dog = Dog("Buddy", "Golden")
    assert dog.name == "Buddy"
    assert dog.breed == "Golden"
    assert dog.species == "Canine"

def test_puppy_inherits_slots():
    puppy = Puppy("Max", "Labrador")
    assert hasattr(puppy, '__slots__')
    assert not hasattr(puppy, '__dict__')


# 6. TEST STRICT CLASS

def test_strict_class():
    obj = StrictClass(1, 2)
    assert obj.x == 1
    with pytest.raises(AttributeError):
        obj.z = 3


# 7. TEST VECTOR DATACLASS SLOTS

def test_vector_slots():
    v = Vector(3, 4)
    assert v.magnitude() == 5.0
    assert not hasattr(v, '__dict__')


# 8. TEST MEMORY SAVINGS

def test_memory_savings():
    p1 = PointDefault(1, 2)
    p2 = PointSlots(1, 2)
    # Slots harus lebih kecil
    assert sys.getsizeof(p2) <= sys.getsizeof(p1)
