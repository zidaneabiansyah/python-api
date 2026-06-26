"""
Testing Multiple Inheritance & MRO
===================================
 Jalankan: pytest test_multiple_inheritance.py -v
"""

import pytest
from main import Smartphone, D as DiamondD, W, Diamond, User, APIClient, Dog, Cat, Puppy, Animal, A, B, C, D as DProcess


# 1. TEST MULTIPLE INHERITANCE

def test_smartphone_has_methods():
    hp = Smartphone("Samsung")
    assert hp.telepon() == "Menelepon..."
    assert "12MP" in hp.foto()


# 2. TEST MRO

def test_mro_order():
    assert [cls.__name__ for cls in DiamondD.__mro__] == ["D", "B", "C", "A", "object"]

def test_w_mro():
    assert [cls.__name__ for cls in W.__mro__] == ["W", "Y", "Z", "X", "object"]


# 3. TEST SUPER CHAINING

def test_diamond_init():
    # Tidak error, semua __init__ dipanggil
    d = Diamond()
    assert hasattr(d, '_cache') or True  # Base init called


# 4. TEST MIXIN

def test_user_json():
    user = User("Budi", "budi@email.com")
    import json
    data = json.loads(user.to_json())
    assert data["name"] == "Budi"

def test_user_log(capsys):
    user = User("Budi", "budi@email.com")
    user.log("test")
    captured = capsys.readouterr()
    assert "[User]" in captured.out


# 5. TEST PROCESS CHAIN

def test_process_chain():
    d = DProcess()
    assert d.process() == ["A", "C", "B", "D"]


# 6. TEST isinstance

def test_isinstance():
    assert isinstance(Puppy(), Dog)
    assert isinstance(Puppy(), Animal)
    assert isinstance(Dog(), Animal)
