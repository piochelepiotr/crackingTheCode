#! /usr/local/bin/python3

import unittest
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
import ex13
import ex14

class Testing(unittest.TestCase):
    def test_stairs(self):
        self.assertEqual(7, ex1.stairs_possibilities(4))
        self.assertEqual(1, ex1.stairs_possibilities(1))
        self.assertEqual(2, ex1.stairs_possibilities(2))

    def test_robot_path(self):
        grid = [
                [False, True,  False, False, False],
                [False, True,  False, False, False],
                [False, True,  False, False, False],
                [False, True,  False, True,  False],
                [False, False, False, True,  False],
               ]
        self.assertListEqual(["START", "DOWN", "DOWN", "DOWN", "DOWN", "RIGHT", "RIGHT", "UP", "UP", "RIGHT", "RIGHT", "DOWN", "DOWN"], ex2.robot_path(grid))

    def test_magic_index(self):
        a = [-5, -3, 0, 1, 4, 6, 10]
        self.assertEqual(4, ex3.magic_index(a))
        self.assertIsNone(ex3.magic_index([-5, -3, 5, 10]))

    def test_power_sets(self):
        sets = ex4.power_set(set([0, 1]))
        self.assertEqual(4, len(sets))
        for s in [set([0, 1]), set([]), set([0]), set([1])]:
            self.assertTrue(s in sets)

    def test_rec_multiply(self):
        self.assertEqual(345*23132, ex5.rec_multiply(345, 23132))

    def test_hanoi(self):
        self.assertEqual((0, 0, 10), ex6.hanoi(10))

    def test_permutations(self):
        self.assertSetEqual(set(["heo", "hoe", "eoh", "eho", "oeh", "ohe"]), ex7.permutations("heo"))

    def test_permutations(self):
        self.assertSetEqual(set(["hho", "hoh", "ohh"]), ex8.permutations("hho"))

    def test_parenthesis(self):
        self.assertSetEqual(set(["(())", "()()"]), set(ex9.parenthesis(2)))

    def test_paint_fill(self):
        screen = [
                [0, 0, 1, 0],
                [0, 0, 1, 1],
                [0, 0, 0, 0],
                [0, 3, 1, 1],
                ]
        expected = [
                [4, 4, 1, 0],
                [4, 4, 1, 1],
                [4, 4, 4, 4],
                [4, 3, 1, 1],
                ]
        ex10.paint_fill(screen, (1,1), 4)
        self.assertEqual(expected, screen)

    def test_coins(self):
        # 25
        # 10
        # 10 10
        # 10 10 5
        # 10 5
        # 10 5 5
        # 10 5 5 5
        # 5
        # 5 5
        # 5 5 5
        # 5 5 5 5
        # 5 5 5 5 5
        # 1 1 1 
        self.assertEqual(13, ex11.coins(25))

    def test_queens(self):
        results = ex12.queens()
        # ex12.print_board(results[0])

    def test_highest_stack(self):
        # width, height, depth
        boxes = [(1, 2, 1), (1, 5, 1), (5, 6, 5), (2, 4, 3)]
        self.assertEqual(12, ex13.highest_stack(boxes))

    def test_bool_exp(self):
        self.assertEqual(2, ex14.bool_exp("1^0|0|1", False))
        self.assertEqual(10, ex14.bool_exp("0&0&0&1^1|0", True))



if __name__ == "__main__":
    unittest.main()
