# Test generated by RoostGPT for test rahul-local-test using AI Type Open AI and AI Model gpt-4

"""
Scenario 1: Leap Year Test
Description: Test to check if the function correctly identifies a leap year.
- Input: year = 2000
- Expected Output: True

Scenario 2: Non-Leap Year Test
Description: Test to check if the function correctly identifies a non-leap year.
- Input: year = 2001
- Expected Output: False

Scenario 3: Test for Year 1900
Description: Test to check if the function correctly identifies the year 1900 as a non-leap year because it is divisible by 100 but not by 400.
- Input: year = 1900
- Expected Output: False

Scenario 4: Test for Year 1600
Description: Test to check if the function correctly identifies the year 1600 as a leap year because it is divisible by 400.
- Input: year = 1600
- Expected Output: True

Scenario 5: Test for Negative Year
Description: Test to check how the function handles negative years.
- Input: year = -2000
- Expected Output: Undefined/Exception/Error

Scenario 6: Test for Zero Year
Description: Test to check how the function handles the year zero.
- Input: year = 0
- Expected Output: Undefined/Exception/Error

Scenario 7: Test for Year with Decimal Values
Description: Test to check how the function handles years with decimal values.
- Input: year = 2000.5
- Expected Output: Undefined/Exception/Error

Scenario 8: Test for Large Year
Description: Test to check how the function handles large year values.
- Input: year = 10000
- Expected Output: True or False based on the leap year calculation.
"""
import pytest
from calendar import isleap
from calculate import judge_leap_year

def test_judge_leap_year():
    # Scenario 1: Leap Year Test
    assert judge_leap_year(2000) == True, "Test case 1 failed"
    
    # Scenario 2: Non-Leap Year Test
    assert judge_leap_year(2001) == False, "Test case 2 failed"
    
    # Scenario 3: Test for Year 1900
    assert judge_leap_year(1900) == False, "Test case 3 failed"
    
    # Scenario 4: Test for Year 1600
    assert judge_leap_year(1600) == True, "Test case 4 failed"
    
    # Scenario 5: Test for Negative Year
    with pytest.raises(ValueError):
        judge_leap_year(-2000)
        
    # Scenario 6: Test for Zero Year
    with pytest.raises(ValueError):
        judge_leap_year(0)
        
    # Scenario 7: Test for Year with Decimal Values
    with pytest.raises(TypeError):
        judge_leap_year(2000.5)
        
    # Scenario 8: Test for Large Year
    # As per Gregorian calendar, year is leap if it is multiple of 400 or multiple of 4 but not of 100.
    # Year 10000 is multiple of 400 hence it is a leap year.
    assert judge_leap_year(10000) == True, "Test case 8 failed"

