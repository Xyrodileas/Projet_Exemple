import unittest
from fizzbuzz import fizzbuzz
class TestFonctionFizzBuzz(unittest.TestCase):
    # Code de test pour la methode fizzbuzz :
    def test_fizz_buzz(self):
        str15 = fizzbuzz(15)
        self.assertEqual(str15, "FizzBuzz")

# Ceci lance le test si on exécute le script
# directement.
if __name__ == '__main__':
    unittest.main()
