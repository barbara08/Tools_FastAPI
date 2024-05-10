# from myfunctions import numero_primo
import unittest

from myfunctions import prime_number, prime_number_v0


class TestPrimeNumber(unittest.TestCase):
    def test_is_prime(self):
        for n in [2, 3, 5, 7, 11, 13, 17]:
            self.assertEqual(prime_number(n), True)
            self.assertEqual(prime_number_v0(n), True)

    def test_is_no_prime(self):
        for n in [12, 30, 45, 27, 110, 13000, 49]:
            self.assertEqual(prime_number(n), False)
            self.assertEqual(prime_number_v0(n), False)

    def test_is_no_prime_lt_2(self):
        self.assertEqual(prime_number(0), False)
        self.assertEqual(prime_number(1), False)
        self.assertEqual(prime_number_v0(0), False)
        self.assertEqual(prime_number_v0(1), False)

    def test_negative_number(self):
        self.assertEqual(prime_number(-15), False)
        self.assertEqual(prime_number_v0(-15), False)

    def test_with_not_int(self):
        # Dos formas de realizarlos
        with self.assertRaises(TypeError):
            prime_number_v0(23.01)
        with self.assertRaises(TypeError):
            prime_number((1, 2, 3))
        self.assertRaises(TypeError, 'prime_number_v0', [23, 6])
        self.assertRaises(TypeError, 'prime_number', [23, 6])


# Syntax: assertEqual(firstValue, secondValue, message)

# Dos formas con asssetRaises
# Syntax:
    # assertRaises(TypeError, 'prime_number_v0', (1, 2, 3))
# Syntax:
    # with self.assertRaises(TypeError):
    # prime_number_v0(23.01)

if __name__ == '__main__':
    unittest.main()
