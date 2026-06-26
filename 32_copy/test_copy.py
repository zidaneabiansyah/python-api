"""
Testing copy.copy() / copy.deepcopy()
======================================
 Jalankan: pytest test_copy.py -v
"""

import pytest
import copy


# 1. TEST SHALLOW COPY

def test_shallow_copy_list():
    a = [1, 2, 3]
    b = copy.copy(a)
    assert a == b
    assert a is not b

def test_shallow_copy_nested():
    a = [[1, 2], [3, 4]]
    b = copy.copy(a)
    # Top level independent
    b[0] = [99, 99]
    assert a[0] == [1, 2]

def test_shallow_copy_nested_shared():
    a = [[1, 2], [3, 4]]
    b = copy.copy(a)
    # Nested still shared
    b[0][0] = 99
    assert a[0][0] == 99


# 2. TEST DEEP COPY

def test_deep_copy_list():
    a = [1, 2, 3]
    b = copy.deepcopy(a)
    assert a == b
    assert a is not b

def test_deep_copy_nested():
    a = [[1, 2], [3, 4]]
    b = copy.deepcopy(a)
    b[0][0] = 99
    assert a[0][0] == 1  # Independent!

def test_deep_copy_dict():
    d = {"a": [1, 2], "b": [3, 4]}
    d2 = copy.deepcopy(d)
    d2["a"].append(3)
    assert len(d["a"]) == 2


# 3. TEST CIRCULAR REFERENCE

def test_circular_reference():
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    a = Node(1)
    b = Node(2)
    a.next = b
    b.next = a

    a_copy = copy.deepcopy(a)
    assert a_copy.value == 1
    assert a_copy.next.value == 2
    assert a_copy.next.next is a_copy  # Circular preserved
    assert a_copy is not a


# 4. TEST SHALLOW vs DEEP DIFFERENCE

def test_shallow_deep_difference():
    original = [[1, 2], [3, 4]]
    shallow = copy.copy(original)
    deep = copy.deepcopy(original)

    original[0][0] = "X"

    assert shallow[0][0] == "X"  # Shallow ikut berubah
    assert deep[0][0] == 1       # Deep tidak berubah


# 5. TEST CUSTOM COPY

def test_custom_copy():
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def __copy__(self):
            return Point(self.x, self.y)

    p1 = Point(5, 10)
    p2 = copy.copy(p1)
    assert p2.x == 5
    assert p1 is not p2
