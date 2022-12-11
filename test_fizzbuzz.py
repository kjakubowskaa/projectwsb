from ap_fizzbuzz import *
# tutaj wszystko z pliki importujemy

#import ap_fizzbuzz jak to użyjemy to plik sam, wtedy musi być ap_fizzbuzz.fizzbuzz

def test_0():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(2) == 2
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(4) == 4
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
