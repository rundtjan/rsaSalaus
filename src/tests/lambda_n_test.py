from random import random
import unittest
from algorithms.lambda_n import gcd, lcm, lambda_n

class TestLambdaNFunctions(unittest.TestCase):
    
    def test_that_lambda_n_returns_integer_within_correct_range(self):
        p = 1699
        q = 2018
        l_n = lambda_n(p,q)
        test_against = lcm(p-1,q-1)
        self.assertEqual(l_n, test_against)

    def test_that_lcm_returns_integer_correct_least_common_multiple(self):
        a = 12
        b = 16
        l = lcm(a,b)
        test_against2 = 12*16/4
        self.assertEqual(l, test_against2)

    def test_that_gcd_returns_correct_greatest_common_denominator(self):
        a = 12
        b = 16
        g = gcd(12,16)
        self.assertEqual(g, 4)
        a = 9
        b = 12
        g = gcd(9, 12)
        self.assertEqual(g, 3)