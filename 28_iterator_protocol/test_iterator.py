"""
Testing Iterator Protocol
==========================
 Jalankan: pytest test_iterator.py -v
"""

import pytest
from itertools import islice
from main import Countdown, Fibonacci, SquaresIterator, squares_generator, InfiniteCounter, BookShelf, RepeatableRange


# 1. TEST COUNTDOWN

def test_countdown():
    assert list(Countdown(5)) == [5, 4, 3, 2, 1]

def test_countdown_satu():
    assert list(Countdown(1)) == [1]

def test_countdown_nol():
    assert list(Countdown(0)) == []


# 2. TEST FIBONACCI

def test_fibonacci():
    assert list(Fibonacci(5)) == [1, 1, 2, 3, 5]

def test_fibonacci_satu():
    assert list(Fibonacci(1)) == [1]

def test_fibonacci_kosong():
    assert list(Fibonacci(0)) == []


# 3. TEST ITERATOR vs GENERATOR SAMA

def test_squares_sama():
    assert list(SquaresIterator(5)) == list(squares_generator(5))


# 4. TEST next() DENGAN DEFAULT

def test_next_default():
    it = iter([1, 2, 3])
    next(it); next(it); next(it)
    assert next(it, "habis") == "habis"


# 5. TEST INFINITE COUNTER

def test_infinite_counter():
    counter = InfiniteCounter(start=0, step=10)
    assert list(islice(counter, 4)) == [0, 10, 20, 30]

def test_infinite_counter_ganjil():
    counter = InfiniteCounter(start=1, step=2)
    assert list(islice(counter, 5)) == [1, 3, 5, 7, 9]


# 6. TEST BOOKSHELF

def test_bookshelf_iterasi():
    shelf = BookShelf()
    shelf.add("A")
    shelf.add("B")
    assert list(shelf) == ["A", "B"]

def test_bookshelf_len():
    shelf = BookShelf()
    shelf.add("A")
    assert len(shelf) == 1


# 7. TEST REPEATABLE RANGE

def test_repeatable_range():
    r = RepeatableRange(3)
    assert list(r) == [1, 2, 3]
    # Bisa diulang
    assert list(r) == [1, 2, 3]
