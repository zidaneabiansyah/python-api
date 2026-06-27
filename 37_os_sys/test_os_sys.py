"""
Testing os & sys Module
========================
 Jalankan: pytest test_os_sys.py -v
"""

import os
import sys
import pytest
import tempfile


# 1. TEST OS PATH

def test_path_basename():
    assert os.path.basename("/home/user/file.txt") == "file.txt"

def test_path_dirname():
    assert os.path.dirname("/home/user/file.txt") == "/home/user"

def test_path_splitext():
    assert os.path.splitext("file.txt") == ("file", ".txt")

def test_path_join():
    result = os.path.join("a", "b", "c.txt")
    assert result.endswith("a/b/c.txt") or result.endswith("a\\b\\c.txt")


# 2. TEST OS EXISTS

def test_exists_dot():
    assert os.path.exists(".") is True

def test_isdir():
    assert os.path.isdir(".") is True

def test_isfile():
    assert os.path.isfile(__file__) is True


# 3. TEST ENVIRONMENT

def test_env_set():
    os.environ['TEST_VAR'] = 'test_value'
    assert os.environ.get('TEST_VAR') == 'test_value'
    del os.environ['TEST_VAR']


# 4. TEST SYS INFO

def test_python_version():
    assert sys.version_info[0] >= 3

def test_platform():
    assert sys.platform in ('linux', 'darwin', 'win32', 'linux-gnu')


# 5. TEST TEMPFILE

def test_tempfile():
    with tempfile.NamedTemporaryFile(delete=False) as f:
        path = f.name
    assert os.path.exists(path)
    os.remove(path)
    assert not os.path.exists(path)
