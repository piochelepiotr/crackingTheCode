import unittest
import ex1
import ex2
import ex3
import ex4
import ex5
import ex6
import ex7
import ex8


class Testing(unittest.TestCase):
    def test_ex1(self):
        self.assertTrue(ex1.has_uniq_characters("World"))
        self.assertFalse(ex1.has_uniq_characters("Hello"))
        self.assertFalse(ex1.has_uniq_characters_without_datastructure("Hello"))
        self.assertTrue(ex1.has_uniq_characters_without_datastructure("World"))

    def test_ex2(self):
        self.assertTrue(ex2.is_permutation("Hello", "elloH"))
        self.assertFalse(ex2.is_permutation("Hella", "elloH"))

    def test_ex3(self):
        s = list("Mr John Smith    ")
        ex3.URLify(s, 13)
        self.assertEqual("".join(s), "Mr%20John%20Smith")

    def test_ex4(self):
        self.assertTrue(ex4.is_palindrome_permutation("kayak"))
        self.assertFalse(ex4.is_palindrome_permutation("ka"))
        self.assertTrue(ex4.is_palindrome_permutation("Tact Coa"))

    def test_ex5(self):
        self.assertTrue(ex5.is_one_operation_away("hey", "hay"))
        self.assertTrue(ex5.is_one_operation_away("heyo", "hey"))
        self.assertTrue(ex5.is_one_operation_away("hey", "heyo"))
        self.assertFalse(ex5.is_one_operation_away("heyo", "hay"))

    def test_ex6(self):
        self.assertEqual(ex6.get_compressed_word("aaaabbccc"), "4a2b3c")

    def test_ex7(self):
        src = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
        ex7.rotate_in_place(src)
        self.assertEqual(src, expected)

    def test_ex8(self):
        src = [[1, 2, 3], [4, 0, 6], [0, 8, 9], [1, 2, 9]]
        expected = [[0, 0, 3], [0, 0, 0], [0, 0, 0], [0, 0, 9]]
        ex8.set_to_0(src)
        self.assertEqual(src, expected)
