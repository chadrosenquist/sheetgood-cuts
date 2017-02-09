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
        board_results = cuts.compute()
        self.assertEqual('board = 8 foot: 3/4" by 1 1/2" by 96"\n'
                         'cut = A: 3/4" by 1 1/2" by 24"\n'
                         'cut = A: 3/4" by 1 1/2" by 24"\n'
                         'cut = C: 3/4" by 1 1/2" by 18 1/2"\n'
                         'cut = C: 3/4" by 1 1/2" by 6"\n'
                         'cut = C: 3/4" by 1 1/2" by 6"',
                         str(board_results[0]))
        self.assertEqual('board = 8 foot: 3/4" by 1 1/2" by 96"\n'
                         'cut = C: 3/4" by 1 1/2" by 6"',
                         str(board_results[1]))
        '''
        for board_result in board_results:
            print(board_result)
        '''

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

    # CHAD TO DO. Create some error scenarios.

if __name__ == '__main__':
    unittest.main()
