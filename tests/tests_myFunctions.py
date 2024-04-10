import pytest
import io
import sys
import src.myFunctions as myFunctions


def test_sum():
    results = myFunctions.sumOfInts(num1=7, num2=3)
    assert results == 10


def test_floatSum():
    results = myFunctions.sumOfFloat(number_1=7.5, number_2=2.5)
    assert results == 10.0


def test_get_ascii_code():
    character = 'a'
    ascii_code = myFunctions.get_ascii_code(character)
    assert ascii_code == 97


def test_print_ascii_stream(capsys):
    sentence = "Hello, World!"
    myFunctions.print_ascii_stream(sentence)
    captured = capsys.readouterr()
    assert captured.out.strip() == "72 101 108 108 111 44 32 87 111 114 108 100 33"


def test_connect_to_google():
    myFunctions.connect_to_google()
    assert True



