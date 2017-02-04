import unittest

from sheetgoodcuts.sheetgoodcuts import Board
from sheetgoodcuts import Mixed
from fractions import Fraction


class BoardTest(unittest.TestCase):
    """Tests Board."""
    def test_string(self):
        test = Fraction("3/4")
        board = Board(depth="3/4", width="2 1/2", length="48")
        self.assertEqual('3/4" by 2 1/2" by 48"', str(board))
        self.assertEqual('Board(depth="3/4", width="2 1/2", length="48")', repr(board))

    def test_immutable(self):
        board = Board(depth="3/4", width="2 1/2", length="48")
        with self.assertRaises(AttributeError):
            board.length = Mixed("1")
        with self.assertRaises(AttributeError):
            board.width = Mixed("1")
        with self.assertRaises(AttributeError):
            board.depth = Mixed("1")


if __name__ == '__main__':
    unittest.main()
