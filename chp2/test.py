import unittest
from collections import Counter

import ex1
import ex2
import ex3
import ex4
import ex5
import linked_list


class Testing(unittest.TestCase):
    def test_ex1(self):
        expected = [1, 2, 3, 4, 5]
        result = linked_list.to_list(
            ex1.remove_dups(linked_list.from_list([1, 2, 3, 4, 5]))
        )
        self.assertEqual(result, expected)
        expected = [1, 2, 4, 5]
        result = ex1.linked_list.to_list(
            ex1.remove_dups(linked_list.from_list([1, 2, 1, 4, 5]))
        )
        self.assertEqual(result, expected)

    def test_ex2(self):
        self.assertEqual(
            ex2.k_last_element(linked_list.from_list([1, 2, 3, 4, 5]), 1), 5
        )
        self.assertEqual(
            ex2.k_last_element(linked_list.from_list([1, 2, 1, 4, 5]), 3), 1
        )

    def test_ex3(self):
        expected = [1, 2, 3, 5]
        L = linked_list.from_list([1, 2, 3, 4, 5])
        ex3.delete_value(L, 4)
        self.assertEqual(linked_list.to_list(L), expected)
        expected = [1, 2, 3, 4, 5]
        L = linked_list.from_list([1, 2, 3, 4, 5])
        ex3.delete_value(L, 6)
        self.assertEqual(linked_list.to_list(L), expected)

    def test_ex4(self):
        expected_low = Counter([1, 3, 4])
        expected_high = Counter([5, 6, 10])
        L = linked_list.from_list([1, 5, 10, 3, 4, 6])
        low, high = ex4.partition(L, 5)
        self.assertEqual(expected_low, Counter(linked_list.to_list(low)))
        self.assertEqual(expected_high, Counter(linked_list.to_list(high)))

    def test_ex5(self):
        x1 = linked_list.from_list([7, 1, 6])
        x2 = linked_list.from_list([5, 9, 2])
        expected = linked_list.from_list([2, 1, 9])
        self.assertEqual(ex5.sum_lists(x1, x2), expected)
