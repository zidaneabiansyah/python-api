"""
Test untuk Type Hints
"""
import pytest
from main import (
    sapa, tambah, proses_angka, hitung_huruf, koordinat,
    ambil_unik, cari_user, konversi, Stack, pertama, swap,
    Pair, Circle, Square, render, bergerak, buat_user, proses_user,
    UserId, UserDict,
)


class TestBasicTypeHints:
    def test_sapa(self):
        assert sapa("Budi") == "Halo, Budi!"

    def test_tambah(self):
        assert tambah(5, 3) == 8


class TestCollections:
    def test_proses_angka(self):
        assert proses_angka([1, 2, 3]) == [2, 4, 6]

    def test_hitung_huruf(self):
        result = hitung_huruf("hello")
        assert result["h"] == 1
        assert result["l"] == 2

    def test_koordinat(self):
        x, y = koordinat()
        assert isinstance(x, float)
        assert isinstance(y, float)

    def test_ambil_unik(self):
        result = ambil_unik(["a", "b", "a"])
        assert result == {"a", "b"}


class TestOptionalUnion:
    def test_cari_user_found(self):
        user = cari_user(1)
        assert user is not None
        assert user["nama"] == "Budi"

    def test_cari_user_not_found(self):
        user = cari_user(999)
        assert user is None

    def test_konversi_string(self):
        assert konversi("42") == 42

    def test_konversi_int(self):
        assert konversi(42) == 42


class TestStack:
    def test_push_pop(self):
        stack: Stack[int] = Stack()
        stack.push(1)
        stack.push(2)
        assert stack.pop() == 2

    def test_peek(self):
        stack: Stack[str] = Stack()
        stack.push("hello")
        assert stack.peek() == "hello"

    def test_is_empty(self):
        stack: Stack[int] = Stack()
        assert stack.is_empty() is True
        stack.push(1)
        assert stack.is_empty() is False


class TestGenericFunctions:
    def test_pertama(self):
        assert pertama([1, 2, 3]) == 1

    def test_pertama_empty(self):
        assert pertama([]) is None

    def test_swap(self):
        a, b = swap("a", 1)
        assert a == 1
        assert b == "a"


class TestPair:
    def test_pair(self):
        p = Pair("nama", "Budi")
        assert p.key == "nama"
        assert p.value == "Budi"


class TestProtocol:
    def test_circle_draw(self):
        c = Circle()
        assert c.draw() == "Menggambar lingkaran"

    def test_square_draw(self):
        s = Square()
        assert s.draw() == "Menggambar persegi"


class TestLiteralFinal:
    def test_bergerak(self):
        assert "atas" in bergerak("atas")


class TestTypedDict:
    def test_buat_user(self):
        user = buat_user(1, "Budi", "budi@test.com")
        assert user["id"] == 1
        assert user["nama"] == "Budi"
        assert user["active"] is True

    def test_proses_user(self):
        user: UserDict = {
            "id": 1, "nama": "Budi",
            "email": "budi@test.com", "active": True
        }
        result = proses_user(user)
        assert "Budi" in result
        assert "active" in result
