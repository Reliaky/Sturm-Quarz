import unittest
import Decimal2binary

class Testdecimal(unittest.TestCase):
    def test_dec_to_bin(self):
        self.assertEqual(Decimal2binary.decimal2binary(-1), [])
        self.assertEqual(Decimal2binary.decimal2binary(0), [0])
        self.assertEqual(Decimal2binary.decimal2binary(2), [1, 0])
        self.assertEqual(Decimal2binary.decimal2binary(3), [1, 1])

