import pytest
from calendar import isleap
import calculate

def test_judge_leap_year_true():
    assert calculate.judge_leap_year(2000) == True

def test_judge_non_leap_year_false():
    assert calculate.judge_leap_year(2001) == False

def test_judge_century_non_leap_year_false():
    assert calculate.judge_leap_year(1900) == False

def test_judge_edge_case_year():
    assert calculate.judge_leap_year(1) == False

def test_judge_future_year():
    assert calculate.judge_leap_year(2100) == False
    
def test_judge_negative_year_input():
    with pytest.raises(ValueError):
        calculate.judge_leap_year(-4)
        
def test_judge_zero_year_input():
    with pytest.raises(ValueError):
        calculate.judge_leap_year(0)
