#from myfunctions import numero_primo
import unittest
import random

from myfunctions import prime_number, prime_number2, prime_number3


class TestPrimeNumber(unittest.TestCase):
    def test_is_prime(self):
        for n in [2,3,5,7,11,13,17]:
            self.assertEqual(prime_number(n), True)
    
    def test_1_no_prime(self):
        self.assertEqual(prime_number(1), False)

    def test_15_no_prime(self):
        self.assertEqual(prime_number(15), False)

    def test_9_no_prime(self):
        self.assertEqual(prime_number3(15), False)

    def test_23_is_prime(self):
        self.assertEqual(prime_number3(23), True)
    

#Syntax: assertEqual(firstValue, secondValue, message)


if __name__ == '__main__': 
    unittest.main() 