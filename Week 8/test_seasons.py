from seasons import age_in_minutes_words
import pytest
import sys


def test_valid_times():
    assert age_in_minutes_words("12:00", "13:00") == "sixty"
    assert age_in_minutes_words("00:00", "01:00") == "sixty"
    assert age_in_minutes_words("00:00", "00:30") == "thirty"
    assert age_in_minutes_words("00:00", "00:15") == "fifteen"

def test_invalid_times():
    with pytest.raises(ValueError):
        age_in_minutes_words("24:00", "01:00")
    with pytest.raises(ValueError):
        age_in_minutes_words("12:60", "13:00")
    with pytest.raises(ValueError):
        age_in_minutes_words("12:00", "24:00")
    with pytest.raises(ValueError):
        age_in_minutes_words("12:00", "12:60")

    try:
        age_in_minutes_words("25:00", "01:00")
    except ValueError:
        sys.exit()
    