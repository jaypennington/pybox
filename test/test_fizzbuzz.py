import pybox.src.fizzbuzz.fizzbuzz as fb


def test_fizzbuzz():
    assert fb.fizzbuzz(3) == "Fizz"
    assert fb.fizzbuzz(4) == "4"
    assert fb.fizzbuzz(5) == "Buzz"
    assert fb.fizzbuzz(15) == "FizzBuzz"