#! /usr/local/bin/python3

import unittest
import ex1
import ex2
import ex3
import ex4
import ex6
import ex7

class Testing(unittest.TestCase):
    def test_insertion(self):
        self.assertEqual(1024 + 19*4, ex1.insertion(1024, 19, 2, 6))

    def test_bit_to_string(self):
        self.assertEqual("01" + 30*"0", ex2.bit_to_string(0.5))
        self.assertEqual("0011" + 28*"0", ex2.bit_to_string(0.375))
        self.assertEqual("ERROR", ex2.bit_to_string(0.3))

    def test_flip_bit(self):
        self.assertEqual(1, ex3.flip_bit("000000000"))
        self.assertEqual(12, ex3.flip_bit("001110110111111111"))
        self.assertEqual(2, ex3.flip_bit("000010000"))

    def test_next_higher(self):
        self.assertEqual(2, ex4.next_higher(1))
        self.assertEqual(3, ex4.next_lower(5))

    def test_conversion(self):
        self.assertEqual(3, ex6.conversion(0b1001101, 0b0111101))

    def test_bit_swap(self):
        self.assertEqual(0b101, ex7.bit_swap_32(0b1010))

if __name__ == "__main__":
    unittest.main()
