"""
Testing Enum Module
====================
 Jalankan: pytest test_enum.py -v
"""

import pytest
from main import Direction, Status, Priority, Color, Hari, Level, Permission, APIStatus, HTTPMethod


# 1. TEST BASIC ENUM

def test_direction_value():
    assert Direction.NORTH.value == 1

def test_direction_name():
    assert Direction.NORTH.name == "NORTH"

def test_direction_access():
    assert Direction(1) == Direction.NORTH
    assert Direction["NORTH"] == Direction.NORTH


# 2. TEST STRING VALUE

def test_status_value():
    assert Status.PENDING.value == "pending"

def test_status_from_string():
    assert Status("approved") == Status.APPROVED


# 3. TEST AUTO

def test_priority_auto():
    assert Priority.LOW.value == 1
    assert Priority.MEDIUM.value == 2
    assert Priority.HIGH.value == 3
    assert Priority.CRITICAL.value == 4


# 4. TEST METHOD

def test_is_terminal():
    assert Status.APPROVED.is_terminal() is True
    assert Status.PENDING.is_terminal() is False

def test_from_string():
    assert Status.from_string("rejected") == Status.REJECTED

def test_from_string_invalid():
    with pytest.raises(ValueError):
        Status.from_string("invalid")


# 5. TEST ITERASI

def test_hari_count():
    assert len(list(Hari)) == 7


# 6. TEST DICT KEY

def test_dict_key():
    counter = {Status.PENDING: 0, Status.APPROVED: 0}
    counter[Status.PENDING] += 1
    assert counter[Status.PENDING] == 1


# 7. TEST INTENUM

def test_intenum_comparison():
    assert Level.DEBUG == 10
    assert Level.INFO > 15


# 8. TEST FLAG

def test_flag_combined():
    assert Permission.ADMIN == Permission.READ | Permission.WRITE | Permission.EXECUTE

def test_flag_contains():
    assert Permission.READ in Permission.ADMIN


# 9. TEST API STATUS

def test_api_status_to_dict():
    d = APIStatus.SUCCESS.to_dict()
    assert d["status"] == "success"
    assert d["name"] == "success"

def test_api_status_is_ok():
    assert APIStatus.SUCCESS.is_ok is True
    assert APIStatus.ERROR.is_ok is False
