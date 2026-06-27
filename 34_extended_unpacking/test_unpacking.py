"""
Testing Extended Unpacking
===========================
 Jalankan: pytest test_unpacking.py -v
"""


# 1. TEST BASIC UNPACKING

def test_tuple_unpacking():
    a, b, c = (1, 2, 3)
    assert a == 1 and b == 2 and c == 3

def test_swap():
    a, b = 1, 2
    a, b = b, a
    assert a == 2 and b == 1


# 2. TEST * UNPACKING

def test_first_middle_last():
    first, *middle, last = [1, 2, 3, 4, 5]
    assert first == 1
    assert middle == [2, 3, 4]
    assert last == 5

def test_head_last():
    *head, last = [1, 2, 3, 4]
    assert head == [1, 2, 3]
    assert last == 4

def test_first_tail():
    first, *tail = [1, 2, 3, 4]
    assert first == 1
    assert tail == [2, 3, 4]


# 3. TEST MERGE

def test_merge_list():
    a = [1, 2]
    b = [3, 4]
    assert [*a, *b] == [1, 2, 3, 4]

def test_merge_dict():
    d1 = {"a": 1}
    d2 = {"b": 2}
    assert {**d1, **d2} == {"a": 1, "b": 2}

def test_merge_dict_override():
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 99}
    assert {**d1, **d2} == {"a": 1, "b": 99}


# 4. TEST UNPACKING DI FUNCTION

def test_args_unpacking():
    from main import tambah
    assert tambah(*[1, 2, 3]) == 6

def test_kwargs_unpacking():
    from main import tambah
    assert tambah(**{"a": 10, "b": 20, "c": 30}) == 60


# 5. TEST EXTENDED ASSIGNMENT

def test_extended_assignment():
    a, *b, c = range(5)
    assert a == 0
    assert b == [1, 2, 3]
    assert c == 4
