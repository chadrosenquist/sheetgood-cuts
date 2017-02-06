import unittest

from sheetgoodcuts import Board, ChopSawCuts, QuantityBoard


class ChopSawCutsTest(unittest.TestCase):
    """Tests ChopSawCuts."""
    def test_one(self):
        desired_cuts = [
            QuantityBoard(2, Board(name="A", depth="3/4", width="1 1/2", length="24")),
            QuantityBoard(3, Board(name="C", depth="3/4", width="1 1/2", length="6")),
            Board(name="C", depth="3/4", width="1 1/2", length="18 1/2"),
        ]
        available_boards = [
            QuantityBoard(3, Board(name="8 foot", depth="3/4", width="1 1/2", length="96")),
        ]
        cuts = ChopSawCuts(desired_cuts=desired_cuts,
                           available_boards=available_boards)

    def test_invalid_desired_cut(self):
        self.assertRaisesRegex(TypeError,
                               "Parameter 'desired_cuts, value = 'desired_cuts' and type '12', "
                               + "should be QuantityBoard or Board.",
                               ChopSawCuts,
                               desired_cuts=[12],
                               available_boards=None)

    def test_invalid_available_boards(self):
        self.assertRaisesRegex(TypeError,
                               "Parameter 'available_boards, value = 'available_boards' and type 'True', "
                               + "should be QuantityBoard or Board.",
                               ChopSawCuts,
                               desired_cuts=[Board(name="C", depth="3/4", width="1 1/2", length="18 1/2")],
                               available_boards=[True])

if __name__ == '__main__':
    unittest.main()
