import unittest
import graph
import tree
import ex1
import ex2
import ex3
import ex4
import ex5
import ex6
import ex7
import ex8
import ex9
import ex10
import ex11
import ex12

class Testing(unittest.TestCase):
    def test_path(self):
        g = graph.Graph([(4, [1]), (5, [0]), (1, [3]), (2, [2])])
        self.assertTrue(ex1.root_between(g, 0, 1))
        self.assertFalse(ex1.root_between(g, 0, 2))
        self.assertTrue(ex1.root_between(g, 3, 2))

    def test_build_search_tree(self):
        t = ex2.build_search_tree([1, 2, 4, 5, 9, 10])
        # print(t)
        self.assertTrue(t.left.value <= t.value)
        self.assertTrue(t.value <= t.right.value)

    def test_list_of_depths(self):
        t = tree.Node(0, tree.Node(1, tree.Node(2)), tree.Node(1))
        l = ex3.values_by_depth(t)
        self.assertEqual([0], l[0])
        self.assertEqual([1, 1], l[1])
        self.assertEqual([2], l[2])

    def test_is_balanced(self):
        t_balanced = tree.Node(0, tree.Node(1, tree.Node(2)), tree.Node(1))
        t_not_balanced = tree.Node(0, tree.Node(1, tree.Node(2, tree.Node(3))), tree.Node(1))
        self.assertTrue(ex4.is_balanced(t_balanced))
        self.assertFalse(ex4.is_balanced(t_not_balanced))

    def test_is_binary_search_tree(self):
        t = ex2.build_search_tree([1, 2, 4, 5, 9, 10])
        t2 = tree.Node(0, tree.Node(1, tree.Node(2)), tree.Node(1))
        self.assertTrue(ex5.check_binary_search_tree(t))
        self.assertFalse(ex5.check_binary_search_tree(t2))

    def test_successor(self):
        numbers = [1, 2, 4, 5, 9, 10, 15, 18, 22]
        t = ex2.build_search_tree(numbers)
        t.build_parents()
        for i,x in enumerate(numbers):
            n = t.find_in_search_tree(x)
            self.assertIsNotNone(n)
            if i == len(numbers) - 1:
                self.assertIsNone(ex6.find_successor(n))
            else:
                self.assertEqual(ex6.find_successor(n).value, numbers[i+1])

    def test_build_order(self):
        order = ex7.build_order(["a", "b", "c", "d", "e", "f"], [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")])
        self.assertEqual(6, len(order))
        self.assertTrue(order[0] == "e" or order[0] == "f")


    def test_first_common_ancestor(self):
        n1 = tree.Node(2)
        n2 = tree.Node(2)
        t = tree.Node(0, tree.Node(1, n1), n2)
        t.build_parents()
        self.assertEqual(t, ex8.first_common_ancestor(n1, n2))

    def test_bst_sequence(self):
        t = tree.Node(2, tree.Node(1), tree.Node(3))
        arrays = ex9.bst_sequence(t)
        self.assertEqual(2, len(arrays))
        self.assertSequenceEqual([2, 1, 3], arrays[0])

    
    def test_is_sub_tree(self):
        n1 = tree.Node(2)
        n2 = tree.Node(2)
        n3 = tree.Node(2)
        t = tree.Node(0, tree.Node(1, n1), n2)
        t.build_parents()
        n3.build_parents()
        self.assertTrue(ex10.is_sub_tree(t, n1))
        self.assertTrue(ex10.is_sub_tree(t, n2))
        self.assertFalse(ex10.is_sub_tree(t, n3))

    def test_random_node(self):
        t = ex11.RandomNode(0)
        t.insert(1)
        t.insert(2)
        d = {0: 0, 1: 0, 2: 0}
        for i in range(1000):
            d[ex11.random_node(t).value] += 1
        for v in d:
            self.assertGreater(d[v], 300)
            self.assertLess(d[v], 400)


    #        0
    #      1   1
    #    -1
    #   3
    def test_path_with_sums(self):
        t = tree.Node(0, tree.Node(1, tree.Node(-1, tree.Node(3))), tree.Node(1))
        self.assertEqual(3, ex12.paths_with_sum(t, 0))


if __name__ == "__main__":
    unittest.main()
