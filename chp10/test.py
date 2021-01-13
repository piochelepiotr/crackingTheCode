import unittest
import ex1
from ex2 import sort_anagram
from ex3 import search_in_rotated_array
from ex4 import search_no_size
from ex5 import sparse_search
from ex9 import search_matrix

class Testing(unittest.TestCase):
    def test_ex1(self):
        b = [0, 3, 8]
        a = [1, 2, 4, 6, 7] + len(b) * [0]
        ex1.merge_sorted(a, b, 5)
        self.assertEqual([0, 1, 2, 3, 4, 6, 7, 8], a)

    def test_ex2(self):
        b = ["hello", "aha", "holle"]
        self.assertEqual(["hello", "holle", "aha"], sort_anagram(b))

    def test_ex3(self):
        array = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
        self.assertEqual(8, search_in_rotated_array(array, 5))

    def test_ex4(self):
        listy = [1, 2, 3, 5, 10, 12, 34]
        self.assertEqual(4, search_no_size(listy, 10))

    def test_ex5(self):
        array = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
        self.assertEqual(4, sparse_search(array, "ball"))

    def test_ex9(self):
        matrix = [
                [4, 5, 11, 15],
                [6, 83, 83, 100],
                [10, 84, 89, 100],
                ]
        self.assertEqual((0, 3), search_matrix(matrix, 15))
                
