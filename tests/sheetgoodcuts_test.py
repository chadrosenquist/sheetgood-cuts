import unittest

from sheetgoodcuts import Board
from sheetgoodcuts import sheetgoodcuts


class ResultTest(unittest.TestCase):
    """Tests Result."""
    def test_one(self):
        # This class is not implemented!!!
        pass


class SheetGoodCutsTest(unittest.TestCase):
    """Tests the main sheet good cuts functionality."""
    def test_one(self):
        desired_cuts = [
            Board("A", "3/4", "15 1/2", "23"),
            Board("A", "3/4", "15 1/2", "23")
        ]
        plywood = [
            Board("Birch", "3/4", "24", "48")
        ]
        results = sheetgoodcuts(desired_cuts=desired_cuts,
                                sheets=plywood)
        #print(results)

if __name__ == '__main__':
    unittest.main()
