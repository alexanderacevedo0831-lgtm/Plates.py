import os
import sys

# Ensure this directory (where plates.py is) is in the Python path

sys.path.append(os.path.dirname(__file__))

from plates import is_valid, starts_with_two_letters, length_is_valid , numbers_at_end, no_punctuation # type: ignore

def test_is_valid_():
    # Valid plates
    assert is_valid("CS50") == True
    assert is_valid("AB1234") == True

    # Invalid plates
    assert is_valid("A") == False  # Too short
    assert is_valid("ABCDEFG") == False  # Too long
    assert is_valid("1AB234") == False  # Does not start with two letters
    assert is_valid("CS05") == False  # Leading zero in numbers
    assert is_valid("CS50P") == False  # Letters after numbers
    assert is_valid("CS.50") == False  # Punctuation

def test_length_and_requirements():  
    assert length_is_valid("AB1234") == True
    assert length_is_valid("A") == False
    assert starts_with_two_letters("AB1234") == True
    assert starts_with_two_letters("A1") == False


def test_numbers_at_end():
    assert numbers_at_end("XY99") == True
    assert numbers_at_end("XY9A") == False
    assert numbers_at_end("XY09") == False

def test_no_punctuation():
    assert no_punctuation("CD4567") == True
    assert no_punctuation("CD 4567") == False
    assert no_punctuation("CD-4567") == False

def test_input_type():
    # Non-string input should return False
    assert is_valid(12345) == False
    assert is_valid(None) == False
