# Test generated by RoostGPT for test rahul-local-test using AI Type Open AI and AI Model gpt-4

"""
1. Scenario: Add two positive numbers
   - Test if the function correctly adds two positive numbers. eg. num1=2, num2=3. Expected output: 5

2. Scenario: Add two negative numbers
   - Test if the function correctly adds two negative numbers. eg. num1=-2, num2=-3. Expected output: -5

3. Scenario: Add a positive number and a negative number
   - Test if the function correctly adds a positive number and a negative number. eg. num1=2, num2=-3. Expected output: -1

4. Scenario: Add a negative number and a positive number
   - Test if the function correctly adds a negative number and a positive number. eg. num1=-2, num2=3. Expected output: 1

5. Scenario: Add zero and a positive number
   - Test if the function correctly adds zero and a positive number. eg. num1=0, num2=3. Expected output: 3

6. Scenario: Add zero and a negative number
   - Test if the function correctly adds zero and a negative number. eg. num1=0, num2=-3. Expected output: -3

7. Scenario: Add zero and zero
   - Test if the function correctly adds zero and zero. eg. num1=0, num2=0. Expected output: 0

8. Scenario: Add two large numbers
   - Test if the function correctly adds two large numbers without any overflow. eg. num1=10^6, num2=10^6. Expected output: 2*10^6

9. Scenario: Add two floating point numbers
   - Test if the function correctly adds two floating point numbers. eg. num1=1.5, num2=2.5. Expected output: 4.0

10. Scenario: Add a floating point number and an integer
    - Test if the function correctly adds a floating point number and an integer. eg. num1=1.5, num2=2. Expected output: 3.5

"""
import pytest
from add import add_numbers

def test_Add_numbers_4beee899f4():
    # Scenario: Add two positive numbers
    assert add_numbers(2, 3) == 5, "Test case 1 failed"

    # Scenario: Add two negative numbers
    assert add_numbers(-2, -3) == -5, "Test case 2 failed"

    # Scenario: Add a positive number and a negative number
    assert add_numbers(2, -3) == -1, "Test case 3 failed"

    # Scenario: Add a negative number and a positive number
    assert add_numbers(-2, 3) == 1, "Test case 4 failed"

    # Scenario: Add zero and a positive number
    assert add_numbers(0, 3) == 3, "Test case 5 failed"

    # Scenario: Add zero and a negative number
    assert add_numbers(0, -3) == -3, "Test case 6 failed"

    # Scenario: Add zero and zero
    assert add_numbers(0, 0) == 0, "Test case 7 failed"

    # Scenario: Add two large numbers
    assert add_numbers(10**6, 10**6) == 2*10**6, "Test case 8 failed"

    # Scenario: Add two floating point numbers
    assert add_numbers(1.5, 2.5) == 4.0, "Test case 9 failed"

    # Scenario: Add a floating point number and an integer
    assert add_numbers(1.5, 2) == 3.5, "Test case 10 failed"

pytest.main()
