"""
Testing dengan PYTEST
=====================
 pytest adalah third-party testing framework yang lebih powerful

 Install: pip install pytest
 Jalankan: pytest test_pytest.py -v
 Atau: pytest (otomatis cari test_*.py)
"""

import pytest
from main import tambah, kurang, kali, bagi, cek_genap, sapa, Kalkulator


# 1. TEST FUNGSI - Simple Assert

def test_tambah():
    assert tambah(5, 3) == 8

def test_kurang():
    assert kurang(10, 5) == 5

def test_kali():
    assert kali(4, 3) == 12

def test_bagi():
    assert bagi(10, 2) == 5.0


# 2. TEST EXPECTED EXCEPTION

def test_bagi_nol_error():
    with pytest.raises(ValueError, match="Tidak bisa membagi dengan nol"):
        bagi(10, 0)

def test_sapa_kosong_error():
    with pytest.raises(ValueError):
        sapa("")


# 3. TEST DENGAN PARAMETER - @pytest.mark.parametrize

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 8),
    (-5, -3, -8),
    (0, 0, 0),
    (100, 200, 300),
])
def test_tambah_param(a, b, expected):
    assert tambah(a, b) == expected


@pytest.mark.parametrize("angka, expected", [
    (2, True),
    (3, False),
    (0, True),
    (-4, True),
])
def test_cek_genap_param(angka, expected):
    assert cek_genap(angka) == expected


# 4. FIXTURE - Setup yang bisa di-reuse

@pytest.fixture
def kalkulator():
    """Buat instance Kalkulator baru untuk setiap test"""
    return Kalkulator()


def test_kalkulator_tambah(kalkulator):
    assert kalkulator.tambah(5, 3) == 8


def test_kalkulator_riwayat(kalkulator):
    kalkulator.tambah(5, 3)
    kalkulator.tambah(10, 2)
    assert len(kalkulator.riwayat) == 2


def test_kalkulator_riwayat_format(kalkulator):
    kalkulator.tambah(5, 3)
    assert kalkulator.riwayat[0] == "5 + 3 = 8"


def test_kalkulator_reset(kalkulator):
    kalkulator.tambah(5, 3)
    assert kalkulator.reset() is True
    assert len(kalkulator.riwayat) == 0


# 5. MARK - Kategorisasi test

@pytest.mark.skip(reason="Belum diimplementasi")
def testbelum_dikerjakan():
    pass


@pytest.mark.skipif(1 + 1 == 3, reason="Math is broken")
def test_skipif():
    assert True


@pytest.mark.xfail(reason="Known bug")
def test_known_bug():
    assert kurang(5, 10) == 5  # Seharusnya -5


# 6. CAPSYS - Capture print output

def test_sapa_print(capsys):
    print("Halo Dunia!")
    captured = capsys.readouterr()
    assert "Halo Dunia!" in captured.out


# 7. TEMPFILE - Temporary file/folder

def test_write_file(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("Hello World")
    assert file.read_text() == "Hello World"
    assert file.exists()
