import pytest
import calculate
from calendar import isleap
import time

def test_non_leap_year():
    assert calculate.judge_leap_year(1900) == isleap(1900)

def test_leap_year():
    assert calculate.judge_leap_year(2000) == isleap(2000)

def test_year_divisible_by_four_not_leap():
    assert calculate.judge_leap_year(2100) == isleap(2100)

def test_year_divisible_by_four_hundred_is_leap():
    assert calculate.judge_leap_year(2400) == isleap(2400)

def test_year_divisible_by_four_not_hundred_is_leap():
    assert calculate.judge_leap_year(2024) == isleap(2024)

def test_valid_year_not_leap():
    assert calculate.judge_leap_year(3001) == isleap(3001)

def test_non_leap_year_in_distant_past():
    assert calculate.judge_leap_year(1801) == isleap(1801)

def test_leap_year_in_distant_past():
    assert calculate.judge_leap_year(1600) == isleap(1600)

def test_current_year():
    assert calculate.judge_leap_year(time.localtime(time.time()).tm_year) == isleap(time.localtime(time.time()).tm_year)

def test_future_year_expected_leap():
    assert calculate.judge_leap_year(2044) == isleap(2044)
