import unittest
import graph
import ex1
import ex2

class Testing(unittest.TestCase):
    def test_path(self):
        g = graph.Graph([(4, [1]), (5, [0]), (1, [3]), (2, [2])])
        self.assertTrue(ex1.root_between(g, 0, 1))
        self.assertFalse(ex1.root_between(g, 0, 2))
        self.assertTrue(ex1.root_between(g, 3, 2))

    def test_build_search_tree(self):
        t = ex2.build_search_tree([1, 2, 4, 5, 9, 10])
        print(t)
        self.assertTrue(t.left.value <= t.value)
        self.assertTrue(t.value <= t.right.value)

if __name__ == "__main__":
    unittest.main()
