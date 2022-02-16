import logging

import pybox.src.factorial.factorial as fact


def test_factorial():
    assert fact.factorial(0) == 1
    assert fact.factorial(1) == 1
    assert fact.factorial(3) == 6


def test_error():
    assert fact.factorial(-2) == logging.ERROR