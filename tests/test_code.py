import pytest

def increment(x):
    return x + 1

def test_increment():
    for i in range(10):
        print(i)
    assert increment(3) == 4
    assert increment(0) == 1
    assert increment(-1) == 0