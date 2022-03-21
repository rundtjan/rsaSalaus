import unittest
from algorithms.miller_rabin import miller_rabin

class TestMillerRabin(unittest.TestCase):

    def test_miller_rabin_identifies_known_primes(self):
        result = miller_rabin(4027,40)
        self.assertTrue(result)
        result = miller_rabin(11587,40)
        self.assertTrue(result)
        result = miller_rabin(905427552554206322123313831641,40)
        self.assertTrue(result)

    def test_miller_rabin_identifies_composite_numbers(self):
        result = miller_rabin(16,40)
        self.assertFalse(result)
        result = miller_rabin(8469,40)
        self.assertFalse(result)
        result = miller_rabin(9943,40)
        self.assertFalse(result)