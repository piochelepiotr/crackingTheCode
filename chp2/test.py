import unittest
import ex1
import ex2
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
