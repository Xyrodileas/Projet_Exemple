# coding: utf8

import unittest
from fizzbuzz import fizzbuzz
class TestFonctionFizzBuzz(unittest.TestCase):
    # Code de test pour la methode fizzbuzz :
    def test_fizz_buzz5(self):
        str15 = fizzbuzz(5)
        self.assertEqual(str15, "Buzz")

    def test_fizz_buzz3(self):
        str15 = fizzbuzz(3)
        self.assertEqual(str15, "Fizz")

    def test_fizz_buzz15(self):
        str15 = fizzbuzz(15)
        self.assertEqual(str15, "FizzBuzz")

    def test_fizz_buzz30(self):
        str15 = fizzbuzz(30)
        self.assertEqual(str15, "FizzBuzz")

    def test_fizz_buzz27(self):
        str15 = fizzbuzz(27)
        self.assertEqual(str15, "Fizz")

    def test_fizz_buzz1(self):
        str15 = fizzbuzz(1)
        self.assertEqual(str15, "1")

    def test_fizz_buzz(self):
        str15 = fizzbuzz(2)
        self.assertEqual(str15, "2")

# Ceci lance le test si on exécute le script
# directement.
if __name__ == '__main__':
    unittest.main()
