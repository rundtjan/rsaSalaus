from random import Random
import unittest
from algorithms.Random_prime_generator import Random_prime_generator

random_prime_gen_100 = Random_prime_generator(100)
random_prime_gen_1000 = Random_prime_generator(1000)

class TestRandomPrimeGenerator(unittest.TestCase):

    def test_random_prime_returns_correct_magnitude(self):
        (n,p,q) = random_prime_gen_100.create()
        self.assertGreater(n, pow(2,99))
        self.assertEqual(p*q, n)
        (n,p,q) = random_prime_gen_1000.create()
        self.assertGreater(n, pow(2,999))
        self.assertEqual(p*q, n)

    def test_random_prime_returns_integer_within_interval(self):
        n = random_prime_gen_100._random_prime((100,200))
        self.assertGreater(n, 100)
        self.assertLess(n,200)

    def test_min_max_returns_correct_boundaries_for_first_prime(self):
        (min,max) = random_prime_gen_1000._min_max(520,None)
        self.assertEqual(min, pow(2,520-1))
        self.assertEqual(max, pow(2,521-1)-1)

    def test_min_max_returns_correct_boundaries_for_second_prime(self):
        (min,max) = random_prime_gen_1000._min_max(10, 1000)
        self.assertEqual(min, pow(2,9)//1000+pow(10,10))
        self.assertEqual(max, (pow(2,10)-1)//1000)

    def test_miller_rabin_identifies_small_primes(self):
        result = random_prime_gen_1000._miller_rabin(1,40)
        self.assertTrue(result)
        result = random_prime_gen_1000._miller_rabin(2,40)
        self.assertTrue(result)
        result = random_prime_gen_1000._miller_rabin(3,40)
        self.assertTrue(result)

    def test_miller_rabin_identifies_known_primes(self):
        result = random_prime_gen_1000._miller_rabin(4027,40)
        self.assertTrue(result)
        result = random_prime_gen_1000._miller_rabin(11587,40)
        self.assertTrue(result)
        result = random_prime_gen_1000._miller_rabin(905427552554206322123313831641,40)
        self.assertTrue(result)

    def test_miller_rabin_identifies_composite_numbers(self):
        result = random_prime_gen_1000._miller_rabin(16,40)
        self.assertFalse(result)
        result = random_prime_gen_1000._miller_rabin(8469,40)
        self.assertFalse(result)
        result = random_prime_gen_1000._miller_rabin(9943,40)
        self.assertFalse(result)