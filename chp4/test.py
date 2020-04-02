import unittest
import graph
import ex1

class Testing(unittest.TestCase):
    def test_path(self):
        g = graph.Graph([(4, [1]), (5, [0]), (1, [3]), (2, [2])])
        self.assertTrue(ex1.root_between(g, 0, 1))
        self.assertFalse(ex1.root_between(g, 0, 2))
        self.assertTrue(ex1.root_between(g, 3, 2))

if __name__ == "__main__":
    unittest.main()
