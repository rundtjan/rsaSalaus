import unittest
from algorithms.encrypt import rsa_encrypt, byte_to_bin_string, string_to_bin, mgf1, xor, oaep, bit_length_of, create_random_seed, bin_string_to_int

class TestEncrypt(unittest.TestCase):
    
    def test_byte_to_bin_string(self):
        string = '$'
        string = string.encode('utf-8')
        bits = byte_to_bin_string(string)
        self.assertEqual(bits, '00100100')
        string = '£$'
        string = string.encode('utf-8')
        bits = byte_to_bin_string(string)
        self.assertEqual(bits, '110000101010001100100100')

    def test_string_to_bin(self):
        bits = string_to_bin('£$')
        self.assertEqual(bits, '110000101010001100100100')

    def test_mgf1_returns_result_of_correct_length(self):
        result = mgf1('10101001111000101010', 24)
        self.assertEqual(len(result), 24)

    def test_mgf1_returns_same_result_everytime_with_same_input(self):
        result = mgf1('10101001111000101010', 24)
        result2 = mgf1('10101001111000101010', 24)
        self.assertEqual(result, result2)
        result3 = mgf1('10101001111000101010', 24)
        self.assertEqual(result2, result3)
        result4 = mgf1('10101001111000101010', 24)
        self.assertEqual(result3, result4)

    def test_xor_returns_correct_xor_result(self):
        bits1 = '1001'
        bits2 = '1001'
        res = xor(bits1, bits2)
        self.assertEqual('0000', res)
        bits1 = '1110'
        bits2 = '1001'
        res = xor(bits1, bits2)
        self.assertEqual('0111', res)

    def test_xor_raises_error_if_different_length_parameters(self):
        bits1 = '1001'
        bits2 = '10001'
        self.assertRaises(AssertionError, xor, bits1, bits2)

    def test_oaep_returns_result_of_correct_length(self):
        result = oaep('10110011001100111100', '11000011', 24)
        self.assertEqual(len(result), 32)

    def test_oaep_returns_same_result_with_same_parameters_everytime(self):
        result = oaep('10110011001100111100', '11000011', 24)
        result2 = oaep('10110011001100111100', '11000011', 24)
        self.assertEqual(result, result2)
        result3 = oaep('10110011001100111100', '11000011', 24)
        self.assertEqual(result2, result3)

    def test_bit_length_of_returns_correct_bit_length(self):
        res = bit_length_of(1)
        self.assertEqual(res, 1)
        res = bit_length_of(8)
        self.assertEqual(res, 4)
        res = bit_length_of(128)
        self.assertEqual(res, 8)

    def test_create_random_seed_creates_seed_of_correct_length(self):
        seed = create_random_seed(12)
        self.assertEqual(len(seed), 12)
        seed = create_random_seed(124)
        self.assertEqual(len(seed), 124)
    
    def test_create_random_seed_creates_different_seed_everytime(self):
        seed = create_random_seed(124)
        seed2 = create_random_seed(124)
        self.assertNotEqual(seed, seed2)
        seed3 = create_random_seed(124)
        self.assertNotEqual(seed, seed3)
        self.assertNotEqual(seed2, seed3)
        seed4 = create_random_seed(124)
        self.assertNotEqual(seed, seed4)
        self.assertNotEqual(seed2, seed4)
        self.assertNotEqual(seed3, seed4)

    def test_bin_string_to_int_creates_correct_result(self):
        res = bin_string_to_int('1001')
        self.assertEqual(res, 9)

    def test_rsa_encrypt_fails_if_seed_is_incorrect_length(self):
        self.assertRaises(AssertionError, rsa_encrypt, 'hello', pow(2,1022), 3)

    def test_rsa_encrypt_fails_if_message_is_too_long(self):
        self.assertRaises(AssertionError, rsa_encrypt, 'hello what a pleasant day to be alive, would you not say, dear Watson', pow(2,127)+1, 3)

    def test_rsa_encrypt_returns_a_string_consisting_of_binary_data(self):
      pass