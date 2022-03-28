import unittest
from algorithms.random_prime import get_prime_numbers, random_prime, min_max

class TestRandomPrime(unittest.TestCase):
    
    def test_random_prime_returns_correct_magnitude(self):
        (p,q) = get_prime_numbers(100)
        product = p*q
        self.assertGreater(product, pow(2,100))
        (p,q) = get_prime_numbers(1000)
        product = p*q
        self.assertGreater(product, pow(2,1000))
    
    def test_random_prime_returns_integer_within_interval(self):
        n = random_prime((100,200))
        self.assertGreater(n, 100)
        self.assertLess(n,200)

    def test_min_max_returns_correct_boundaries_for_first_prime(self):
        (min,max) = min_max(520,None)
        self.assertEqual(min, pow(2,520))
        self.assertEqual(max, pow(2,521)-1)

    def test_min_max_returns_correct_boundaries_for_second_prime(self):
        (min,max) = min_max(10, 1000)
        self.assertEqual(min, pow(2,10)//1000+pow(10,10))
        self.assertEqual(max, (pow(2,11)-1)//1000)