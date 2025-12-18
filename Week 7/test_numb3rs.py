import os
import sys

# Ensure this directory (where numb3rs.py is) is in the Python path

sys.path.append(os.path.dirname(__file__))

from numb3rs import validate as is_valid

def test_validate():
    # Valid IPv4 addresses
    assert is_valid("145.0.9.1") == True
    assert is_valid("255.1.1.4") == True
    assert is_valid("127.0.0.1") == True

    # Invalid IPv4 addresses
    assert is_valid("256.100.50.25") == False  # Octet > 255
    assert is_valid("192.168.1") == False      # Not enough octets
    assert is_valid("-0.11.5.1") == False     # Negative octet
    assert is_valid("110.11.3.5.6") == False  # Too many octets
    assert is_valid("abc.def.ghi.jkl") == False
    assert is_valid("000.001.010.100") == False  # Leading zeros

# If not returning boolean, treat as False
def test_non_boolean_return():
    assert is_valid("300.400.500.600") == False  # Out of range
    assert is_valid("...") == False
                   # Empty octets