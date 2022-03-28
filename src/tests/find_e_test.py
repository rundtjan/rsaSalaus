import random as rand
import unittest
from algorithms.find_e import find_e
from algorithms.lambda_n import lambda_n, gcd

class TestFindE(unittest.TestCase):
    
    def test_find_e_returns_correct_integer(self):
        p = 1699
        q = 2018
        l_n = lambda_n(p,q)
        e = find_e(l_n)
        self.assertEqual(gcd(l_n, e), 1)
        rand_int = rand.randint(1234134134,123412341241234)
        e = find_e(rand_int)
        self.assertEqual(gcd(rand_int,e), 1)
        rand_int = rand.randint(123,1234)
        e = find_e(rand_int)
        self.assertEqual(gcd(rand_int, e), 1)
