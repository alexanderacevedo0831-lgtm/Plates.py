import os
import sys

# Ensure this directory (where fuel.py is) is in the Python path

sys.path.append(os.path.dirname(__file__))

from fuel import gauge, convert

def test_gauge():
    assert gauge(0.0) == "E"
    assert gauge(1.0) == "F"
    assert gauge(0.5) == "50%"
    assert gauge(0.01) == "E"
    assert gauge(0.99) == "F"

def test_convert():
    assert convert("1/2") == True
    assert convert("3/4") == True
    assert convert("0/1") == True
    assert convert("1/0") == False  # Division by zero
    assert convert("-1/2") == False  # Negative value
    assert convert("2/1") == False  # Greater than 1
    assert convert("abc") == False  # Invalid format
    assert convert("1/a") == False  # Invalid format

def test_invalid_inputs():
    assert convert("1/0") == False  # Division by zero
    assert convert("-1/2") == False  # Negative value
    assert convert("2/1") == False  # Greater than 1
    assert convert("abc") == False  # Invalid format
    assert convert("1/a") == False  # Invalid format