from um import count
import pytest


def test_valid_times():
    assert count("Um, I think um we should um go.") == 3
    assert count(" Hey are you coming? ") == 0
    assert count("Um...") == 1
    assert count("Yummy food!") == 0

def test_invalid_times():
    assert count("umbrella") == 0
    assert count(" aluminum ") == 0
    assert count("Um, umm, ummm...") == 1
    assert count("UM, um, Um, uM") == 4
    assert count("") == 0
    