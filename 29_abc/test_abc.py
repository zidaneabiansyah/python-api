"""
Testing Abstract Base Classes
==============================
 Jalankan: pytest test_abc.py -v
"""

import pytest
from abc import ABC
from main import (
    Kucing, Burung, Circle, Rectangle, Triangle,
    Gamer, Line, Playlist, SQLiteDB, PostgreSQLDB,
    AudioPlugin, VideoPlugin, Plugin
)


# 1. TEST ABC TIDAK BISA DIINSTANSIASI

def test_abc_tidak_bisa_instansiasi():
    from main import Hewan
    with pytest.raises(TypeError):
        Hewan()


# 2. TEST KUCING

def test_kucing_bersuara():
    assert Kucing().bersuara() == "Meow!"

def test_kucing_bergerak():
    assert "4 kaki" in Kucing().bergerak()


# 3. TEST SHAPE

def test_circle_area():
    assert Circle(5).area() == pytest.approx(78.53975, rel=1e-3)

def test_rectangle_area():
    assert Rectangle(4, 6).area() == 24

def test_triangle_perimeter():
    assert Triangle(3, 4, 5, 4).perimeter() == 12


# 4. TEST PLAYER

def test_gamer_score():
    gamer = Gamer("Budi", 100)
    assert gamer.score == 100
    gamer.play()
    assert gamer.score == 110


# 5. TEST REGISTER

def test_register():
    assert issubclass(Line, Plugin) is False  # Line bukan Plugin
    assert hasattr(Line, 'draw')


# 6. TEST PLAYLIST (Sequence ABC)

def test_playlist_len():
    p = Playlist()
    p.add("A")
    p.add("B")
    assert len(p) == 2

def test_playlist_getitem():
    p = Playlist()
    p.add("X")
    assert p[0] == "X"

def test_playlist_contains():
    p = Playlist()
    p.add("Song")
    assert "Song" in p


# 7. TEST PLUGIN

def test_plugin_registry():
    plugins = Plugin.get_plugins()
    assert "AudioPlugin" in plugins
    assert "VideoPlugin" in plugins
