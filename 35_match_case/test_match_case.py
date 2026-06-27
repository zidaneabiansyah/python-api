"""
Testing Match-Case Pattern Matching
====================================
 Jalankan: pytest test_match_case.py -v
"""


# 1. TEST BASIC MATCH

def test_match_start():
    from main import proses_perintah
    assert proses_perintah("start") == "Memulai program..."

def test_match_stop():
    from main import proses_perintah
    assert proses_perintah("stop") == "Menghentikan program..."

def test_match_unknown():
    from main import proses_perintah
    assert "tidak dikenal" in proses_perintah("xyz")


# 2. TEST HTTP STATUS

def test_http_200():
    from main import http_status
    assert http_status(200) == "OK"

def test_http_404():
    from main import http_status
    assert http_status(404) == "Not Found"


# 3. TEST CAPTURE PATTERN

def test_origin():
    from main import identifikasi_titik
    assert identifikasi_titik((0, 0)) == "Origin"

def test_sumbu_x():
    from main import identifikasi_titik
    assert "sumbu X" in identifikasi_titik((5, 0))


# 4. TEST SEQUENCE PATTERN

def test_list_kosong():
    from main import proses_list
    assert proses_list([]) == "Kosong"

def test_list_satu():
    from main import proses_list
    assert "Satu item" in proses_list([42])

def test_list_many():
    from main import proses_list
    assert "First" in proses_list([1, 2, 3, 4])


# 5. TEST MAPPING PATTERN

def test_user_admin():
    from main import proses_user
    user = {"name": "Budi", "age": 25, "role": "admin"}
    assert "Admin" in proses_user(user)

def test_user_regular():
    from main import proses_user
    user = {"name": "Andi", "age": 30}
    assert "User" in proses_user(user)


# 6. TEST CLASS PATTERN

def test_point_origin():
    from main import Point, describe_shape
    assert describe_shape(Point(0, 0)) == "Origin"

def test_point_sumbu_x():
    from main import Point, describe_shape
    assert "sumbu X" in describe_shape(Point(5, 0))
