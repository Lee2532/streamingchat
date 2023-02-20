import pytest


def increment(x):
    return x + 1


def test_increment():
    print("test code run")
    assert increment(3) == 4
    assert increment(0) == 1
    assert increment(-1) == 0
    print("test code exit")
