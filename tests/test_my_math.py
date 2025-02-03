import pytest

from src.my_math import sum, multiply, difference

def test_sum():
    res = sum(1,1)
    assert res == 2

# Work together
## Test multiply

def test_multiply():
    res = multiply(10,10)
    assert res == 100

# Check for understanding
## Test difference
def test_different():
    res = differnece(10,-5)
    assert res == 5
# Work together
## Test absolute sum
def test_it_should_return_positive_numbers_1()
    res = absolute_sim(1,2)
    assert res == 3

def test_it_should_return_positive_numbers_()
    res = absolute_sim(-1,2)
    assert res == 3


# Check for understanding
## Test calculate age

def calc_age_1()
    res = calculate_birth_year(2025, 40, False)
    assert res == 1984
    