import os
import sys

# Ensure this directory (where bank.py is) is in the Python path
sys.path.append(os.path.dirname(__file__))

from bank import value

def test_value_hello():
    assert value("hello") == 0
    assert value(" Hello there ") == 0
    assert value("HELLO") == 0

def test_value_h():
    assert value("hi") == 20
    assert value(" Hey ") == 20
    assert value("hELLo") == 20

def test_value_other():
    assert value("good morning") == 100
    assert value("  goodbye ") == 100
    assert value("xyz") == 100

def test_value_case_insensitivity():
    assert value("HeLLo") == 0
    assert value("hOwdy") == 20
    assert value("WORLD") == 100

def test_input_with_whitespace():
    assert value("   hello   ") == 0
    assert value("   hi   ") == 20
    assert value("   bye   ") == 100

def test_input_type():
    try:
        value(123)
    except AttributeError:
        assert True
    else:
        assert False