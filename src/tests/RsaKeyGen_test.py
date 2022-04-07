import random as rand
import unittest
from rsa_service.RsaKeyGenerator import RsaKeyGenerator
from rsa_service.LambdaNGenerator import LambdaNGenerator

rsa_key_gen = RsaKeyGenerator(1024)
lambda_n_gen = LambdaNGenerator()

class TestRsaKeyGenerator(unittest.TestCase):
    
    def test_find_e_returns_correct_integer(self):
        p = 1699
        q = 2018
        l_n = lambda_n_gen.create(p,q)
        e = rsa_key_gen._find_e(l_n)
        self.assertEqual(lambda_n_gen.gcd(l_n, e), 1)
        rand_int = rand.randint(1234134134,123412341241234)
        e = rsa_key_gen._find_e(rand_int)
        self.assertEqual(lambda_n_gen.gcd(rand_int,e), 1)
        rand_int = rand.randint(123,1234)
        e = rsa_key_gen._find_e(rand_int)
        self.assertEqual(lambda_n_gen.gcd(rand_int, e), 1)

    def test_that_ext_euclidean_returns_correct_result(self):
        res_a = rsa_key_gen._ext_euclidean(81,57)
        res_b = rsa_key_gen._ext_euclidean(46,240)
        res_c = rsa_key_gen._ext_euclidean(61142807745645472107166599236498665523095742862759734512743290005394961942862310160864170140184161856100082346225825540866500367436669761385246038695881247776671814474742882946314936863860935651037249742036466937206505539297480207250386210036736123192885143784058218340707408139396601094952305007978709891160, 65537)
        self.assertEqual(res_a, 10)
        self.assertEqual(res_b, 37)
        self.assertEqual(res_c, 56617995539313468205252291192233311176894141433271281999097487534635458678707982006078457868034182683997523495817731580611949094383770660988242158633091921873489515922741677790607055151397357246356982698246289409314603989553171206149262064612347301649550951688712347169423539035286350163256946976810106766633)       

    def test_create_key_returns_n_of_correct_magnitude(self):
        (n,e,d) = rsa_key_gen.create()
        length = len(bin(n)[2:])
        self.assertEqual(length, 1024)
