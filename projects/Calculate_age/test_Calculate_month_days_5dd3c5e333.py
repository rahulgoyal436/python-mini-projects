import pytest
from calculate import month_days

def test_month_days_for_31_days_months():
    for month in [1, 3, 5, 7, 8, 10, 12]:
        assert month_days(month, False) == 31

def test_month_days_for_30_days_months():
    for month in [4, 6, 9, 11]:
        assert month_days(month, False) == 30

def test_month_days_for_feb_leap_year():
    assert month_days(2, True) == 29

def test_month_days_for_feb_non_leap_year():
    assert month_days(2, False) == 28

def test_month_days_for_invalid_months():
    for month in [0, 13, -1]:
        with pytest.raises(ValueError):
            month_days(month, False)

def test_month_days_for_non_boolean_leap_year():
    for leap_year in ["True", 1]:
        with pytest.raises(TypeError):
            month_days(2, leap_year)

def test_month_days_with_no_parameters():
    with pytest.raises(TypeError):
        month_days()

def test_month_days_with_extra_parameters():
    with pytest.raises(TypeError):
        month_days(1, False, True)
