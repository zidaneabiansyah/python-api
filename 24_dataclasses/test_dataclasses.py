"""
Test untuk Dataclasses
"""
import pytest
from main import Point, Mahasiswa, Color, Suhu, Produk, UserProfile


class TestPoint:
    def test_repr(self):
        p = Point(5, 10)
        assert repr(p) == "Point(x=5, y=10)"

    def test_equality(self):
        p1 = Point(5, 10)
        p2 = Point(5, 10)
        assert p1 == p2

    def test_inequality(self):
        p1 = Point(5, 10)
        p2 = Point(3, 7)
        assert p1 != p2


class TestMahasiswa:
    def test_default_values(self):
        mhs = Mahasiswa("Budi", 20)
        assert mhs.jurusan == "Umum"
        assert mhs.ipk == 0.0
        assert mhs.aktivitas == []

    def test_mutable_default_isolation(self):
        mhs1 = Mahasiswa("Budi", 20)
        mhs2 = Mahasiswa("Andi", 22)
        mhs1.aktivitas.append("Coding")
        assert len(mhs2.aktivitas) == 0


class TestColor:
    def test_immutable(self):
        c = Color(255, 0, 0)
        with pytest.raises(AttributeError):
            c.r = 100

    def test_hashable(self):
        c = Color(255, 0, 0)
        d = {c: "merah"}
        assert d[Color(255, 0, 0)] == "merah"


class TestSuhu:
    def test_post_init_error(self):
        with pytest.raises(ValueError):
            Suhu(-300)

    def test_fahrenheit(self):
        s = Suhu(100)
        assert s.fahrenheit == 212.0


class TestProduk:
    def test_asdict(self):
        p = Produk("Laptop", 10000000, 5)
        d = {"nama": "Laptop", "harga": 10000000, "stok": 5}
        assert asdict(p) == d


class TestUserProfile:
    def test_email_lowercase(self):
        user = UserProfile("budi", "BUDI@EMAIL.COM")
        assert user.email == "budi@email.com"

    def test_display_name_with_fullname(self):
        user = UserProfile("budi", "budi@email.com", "Budi Prasetio")
        assert user.display_name == "Budi Prasetio"

    def test_display_name_without_fullname(self):
        user = UserProfile("budi", "budi@email.com")
        assert user.display_name == "budi"

    def test_add_tag_unique(self):
        user = UserProfile("budi", "budi@email.com")
        user.add_tag("admin")
        user.add_tag("admin")  # Duplicate
        assert len(user.tags) == 1

    def test_deactivate(self):
        user = UserProfile("budi", "budi@email.com")
        user.deactivate()
        assert user.is_active is False
