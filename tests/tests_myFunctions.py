import pytest
import src.myFunctions as myFunctions


def test_sum():
    results = myFunctions.sumOfInts(num1=7, num2=3)
    assert results == 10


def test_floatSum():
    results = myFunctions.sumOfFloat(number_1=7.5, number_2=2.5)
    assert results == 10.0
