import unittest

from myfunctions import prime_number, prime_number_v0, generate_password, decimal_to_binary, binary_to_decimal, is_palindrome

# 1. TEST PARA NÚMERO PRIMOS


class xTestPrimeNumber(unittest.TestCase):
    def xtest_is_prime(self):
        for n in [2, 3, 5, 7, 11, 13, 17]:
            self.assertEqual(prime_number(n), True)
            self.assertEqual(prime_number_v0(n), True)

    def xtest_is_no_prime(self):
        for n in [12, 30, 45, 27, 110, 13000, 49]:
            self.assertEqual(prime_number(n), False)
            self.assertEqual(prime_number_v0(n), False)

    def xtest_is_no_prime_lt_2(self):
        self.assertEqual(prime_number(0), False)
        self.assertEqual(prime_number(1), False)
        self.assertEqual(prime_number_v0(0), False)
        self.assertEqual(prime_number_v0(1), False)

    def xtest_negative_number(self):
        self.assertEqual(prime_number(-15), False)
        self.assertEqual(prime_number_v0(-15), False)

    def xtest_with_not_int(self):
        # Dos formas de realizarlos
        with self.assertRaises(TypeError):
            prime_number_v0(23.01)
        with self.assertRaises(TypeError):
            prime_number((1, 2, 3))
        self.assertRaises(TypeError, 'prime_number_v0', [23, 6])
        self.assertRaises(TypeError, 'prime_number', [23, 6])


# 2. TEST PARA GENERAR PASSWORD ALEATORIOS

class xTestRandomPassWord(unittest.TestCase):

    def xtest_is_generate(self):
        self.assertEqual(len(generate_password(8)), 8)

    def xtest_is_generate_2(self):
        self.assertEqual(len(generate_password(16)), 16)

    def xtest_is_generate_3(self):
        self.assertEqual(len(generate_password(12)), 12)

    def xtest_is_not_generate(self):
        # self.assertRaises(ValueError, "generate_password", [17])  # DE ESTA FORMA NO SALE, SALE CON WITH
        with self.assertRaises(ValueError):
            generate_password(17)

    def xtest_is_not_generate_2(self):
        with self.assertRaises(ValueError):
            generate_password(7)


# 3. TEST PARA PASAR DECIMAL A BINARIO

class TestDecimal_to_binary(unittest.TestCase):
    def test_decimal_to_binary(self):
        self.assertEqual(decimal_to_binary(10), "1010")
        self.assertEqual(decimal_to_binary(15), "1111")
        self.assertEqual(decimal_to_binary(0), "0")
        self.assertEqual(decimal_to_binary(2), "10")
        self.assertEqual(decimal_to_binary(1), "1")

    def test_decimal_to_binary_with_error(self):
        with self.assertRaises(TypeError):
            decimal_to_binary("adsf")
        with self.assertRaises(TypeError):
            decimal_to_binary([1])
        with self.assertRaises(TypeError):
            decimal_to_binary({1})
        with self.assertRaises(TypeError):
            decimal_to_binary("1")

    def test_decimal_to_binary_with_negative_number(self):
        with self.assertRaises(ValueError):
            decimal_to_binary(-7)

# 4. TEST PARA PASAR NÚMERO BINARIO A DECIMAL


class TestBinary_to_decimal(unittest.TestCase):
    def test_binary_to_decimal(self):
        self.assertEqual(binary_to_decimal(1010), 10)
        self.assertEqual(binary_to_decimal(100), 4)

    def test_binary_to_decimal_with_error(self):
        with self.assertRaises(ValueError):
            binary_to_decimal("adsf")
        with self.assertRaises(ValueError):
            binary_to_decimal([1])
        with self.assertRaises(ValueError):
            binary_to_decimal({1})
        with self.assertRaises(ValueError):
            binary_to_decimal(-7)


class TestIsPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertEqual(is_palindrome("Ana lleva al oso la avellana"), True)
        self.assertEqual(is_palindrome("Ana"), True)
        self.assertEqual(is_palindrome(" Ana "), True)
        self.assertEqual(is_palindrome("Sara Baras "), True)

    def test_otros(self):
        self.assertEqual(is_palindrome("Hola que tal"), False)
        self.assertEqual(is_palindrome(None), False)
        self.assertEqual(is_palindrome(True), False)
        self.assertEqual(is_palindrome(False), False)
        self.assertEqual(is_palindrome(111), True)
        self.assertEqual(is_palindrome(1101), False)
        self.assertEqual(is_palindrome(111.3), False)
        self.assertEqual(is_palindrome((111,)), False)
        self.assertEqual(is_palindrome((111.3,)), False)
        self.assertEqual(is_palindrome([111,]), False)
        self.assertEqual(is_palindrome([111.3,]), False)
        self.assertEqual(is_palindrome({"a": 111.3, }), False)
        self.assertEqual(is_palindrome({"a": "a"}), False)


if __name__ == '__main__':
    unittest.main()
