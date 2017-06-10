from primeNumbers import primeNumbers
import unittest
import sys

class TestPrimeNumbers(unittest.TestCase):
    
    def test_Answers(self):
        """ Test if the list returned is actually prime numbers """
        self.assertEqual(primeNumbers(9),[1,2,3,5,7])

    def test_InputTypeInt(self):
        """ Test input is inntager """
        with self.assertRaises(TypeError):
            primeNumbers([])

    def test_NoPrimesLimitZero(self):
        """ Testing no prime numbers for zero limit """
        self.assertEqual(primeNumbers(0),[], "Not Primes for Limit Zero")
        
    def test_NincludedInPrimes(self):
        """ Test n include if a prime number"""
        self.assertNotEqual(primeNumbers(11),[1,2,3,5,7,9,11], "N must be part of List if it is Prime")

    def test_OnlyPrimesInList(self):
        """ensure the list contains prime numbers only"""
        self.assertNotIn(4,primeNumbers(12), msg = "Number not a prime number")

if __name__ == '__main__':
    unittest.main()
