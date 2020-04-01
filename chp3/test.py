import unittest
import ex2
import ex3
import ex4
import ex5
import ex6
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

    def test_queue(self):
        q = ex4.MyQueue()
        q.push(1)
        q.push(2)
        q.push(3)
        self.assertEqual(1, q.pull())
        self.assertEqual(2, q.pull())
        self.assertEqual(3, q.pull())

    def test_sort_stack(self):
        s = stack.Stack()
        s.push(2)
        s.push(1)
        s.push(3)
        s.push(5)
        sorted_stack = ex5.sort_stack(s)
        self.assertEqual(4, sorted_stack.size())
        self.assertEqual(5, sorted_stack.pop())
        self.assertEqual(3, sorted_stack.pop())
        self.assertEqual(2, sorted_stack.pop())
        self.assertEqual(1, sorted_stack.pop())

    def test_shelter(self):
        shelter = ex6.Shelter()
        shelter.enqueue(ex6.Cat('Garfield'))
        shelter.enqueue(ex6.Dog('Sirius'))
        shelter.enqueue(ex6.Dog('Rantanplan'))
        shelter.enqueue(ex6.Cat('Crookshanks'))
        self.assertEqual('Sirius', shelter.dequeue_dog().name)
        self.assertEqual('Garfield', shelter.dequeue_any().name)
        self.assertEqual('Crookshanks', shelter.dequeue_cat().name)



if __name__ == "__main__":
    unittest.main()
