import os
import sys

# Ensure this directory (where twttr.py is) is in the Python path
sys.path.append(os.path.dirname(__file__))

from twttr import shorten

def test_vowel_removal():
    assert shorten("Twitter") == "Twttr"
    assert shorten("AEIOUaeiou") == ""
    assert shorten("CS50") == "CS50"
    assert shorten("Hello, World!") == "Hll, Wrld!"


def test_punctuation_and_spaces():
    assert shorten("Hello, World!") == "Hll, Wrld!"
    assert shorten( " a e i o u ") == "      "  # 6 spaces, not 5

def test_input_type():
    try:
        shorten(123)
    except TypeError:
        assert True
    else:
        assert False
