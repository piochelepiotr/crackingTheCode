import unittest
import ex2
import ex3
import stack

class Testing(unittest.TestCase):
    def test_s(self):
        s = stack.Stack()
        s.push(3)
        s.push(4)
        self.assertEqual(4, s.pop())
        self.assertEqual(3, s.pop())

    def test_min_s(self):
        s = ex2.MinStack()
        s.add(3)
        s.add(4)
        s.add(2)
        self.assertEqual(2, s.min())
        self.assertEqual(2, s.pop())
        self.assertEqual(3, s.min())
        self.assertEqual(4, s.pop())

    def test_set_of_ss(self):
        s = ex3.SetOfStacks(2)
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(3, s.pop())
        self.assertEqual(2, s.pop())
        self.assertEqual(1, s.pop())

        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(2, s.pop_at(0))
        self.assertEqual(3, s.pop())
        self.assertEqual(1, s.pop())



if __name__ == "__main__":
    unittest.main()
