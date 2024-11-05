# tests/test_some_module.py

from ayush_py import greet

def test_greet():
    assert greet('Alice') == 'Hello, Alice!'
    assert greet('Bob') == 'Hello, Bob!'
