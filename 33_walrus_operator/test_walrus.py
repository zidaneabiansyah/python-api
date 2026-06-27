"""
Testing Walrus Operator
========================
 Jalankan: pytest test_walrus.py -v
"""


# 1. TEST BASIC WALRUS

def test_walrus_basic():
    data = [1, 2, 3]
    if (n := len(data)) > 2:
        assert n == 3


# 2. TEST WALRUS DI IF

def test_walrus_if_max():
    angka = [3, 1, 4, 1, 5]
    if (maks := max(angka)) > 4:
        assert maks == 5

def test_walrus_if_list():
    angka = [1, 2, 3, 4]
    if (genap := [x for x in angka if x % 2 == 0]):
        assert genap == [2, 4]


# 3. TEST WALRUS DI LIST COMPREHENSION

def test_walrus_comprehension():
    data = [1, -2, 3, -4, 5]
    result = [y for x in data if (y := abs(x)) > 2]
    assert result == [3, 4, 5]


# 4. TEST WALRUS DI FUNGSI

def test_proses_data_kosong():
    from main import proses_data
    assert proses_data([]) == "Data kosong"

def test_proses_data_satu():
    from main import proses_data
    assert proses_data([42]) == "Satu item: 42"

def test_proses_data_banyak():
    from main import proses_data
    assert "5 items" in proses_data([1, 2, 3, 4, 5])


# 5. TEST SAFE DIVIDE

def test_safe_divide_normal():
    from main import safe_divide
    assert safe_divide(10, 2) == 5.0

def test_safe_divide_zero():
    from main import safe_divide
    assert safe_divide(10, 0) is None
