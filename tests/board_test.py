import unittest

from sheetgoodcuts import Board, Mixed, QuantityBoard, BoardResult


class BoardTest(unittest.TestCase):
    """Tests Board."""
    def test_string(self):
        board = Board(name="A", depth="3/4", width="2 1/2", length="48")
        self.assertEqual('A: 3/4" by 2 1/2" by 48"', str(board))
        self.assertEqual('Board(name="A", depth="3/4", width="2 1/2", length="48")', repr(board))

    def test_mixed(self):
        board = Board(name="B", depth=Mixed("3/4"), width=Mixed("2 1/2"), length=Mixed("48"))
        self.assertEqual('B: 3/4" by 2 1/2" by 48"', str(board))

    def test_immutable(self):
        board = Board(name="A", depth="3/4", width="2 1/2", length="48")
        with self.assertRaises(AttributeError):
            board.name = "B"
        with self.assertRaises(AttributeError):
            board.length = Mixed("1")
        with self.assertRaises(AttributeError):
            board.width = Mixed("1")
        with self.assertRaises(AttributeError):
            board.depth = Mixed("1")

    def test_value_error(self):
        with self.assertRaises(ValueError):
            Board(name="A", depth=123, width="2 1/2", length="48")


class QuantityBoardTest(unittest.TestCase):
    """Tests QuantityBoard."""
    def setUp(self):
        self.test_board = Board(name="A", depth="3/4", width="2 1/2", length="48")
        self.quantity_board = QuantityBoard(3, self.test_board)

    def test_constructor(self):
        self.assertEqual(3, self.quantity_board.quantity)
        self.assertEqual(str(self.test_board), str(self.quantity_board.board))

    def test_immutable(self):
        with self.assertRaises(AttributeError):
            self.quantity_board.quantity = 3
        with self.assertRaises(AttributeError):
            self.quantity_board.board = self.test_board

    def test_str(self):
        self.assertEqual('3 x \'A: 3/4" by 2 1/2" by 48"\'', str(self.quantity_board))

    def test_repr(self):
        self.assertEqual('QuantityBoard(3, Board(name="A", depth="3/4", width="2 1/2", length="48"))', repr(self.quantity_board))


class BoardResultTest(unittest.TestCase):
    """Tests BoardResult."""
    def setUp(self):
        self.board = Board(name="8 foot", depth="3/4", width="1 1/2", length="96")
        self.cuts = [
            Board(name="A", depth="3/4", width="1 1/2", length="24"),
            Board(name="A", depth="3/4", width="1 1/2", length="24"),
            Board(name="A", depth="3/4", width="1 1/2", length="12")
        ]
        self.board_result = BoardResult(board=self.board,
                                        cuts=self.cuts)

    def test_constructor(self):
        self.assertEqual(str(self.board), str(self.board_result.board))
        self.assertTupleEqual(self.board_result.cuts, self.board_result.cuts)

    def test_immutable(self):
        with self.assertRaises(AttributeError):
            self.board_result.board = self.board
        with self.assertRaises(AttributeError):
            self.board_result.cuts = self.cuts

    def test_str(self):
        self.assertEqual('board = 8 foot: 3/4" by 1 1/2" by 96"\n'
                         'cut = A: 3/4" by 1 1/2" by 24"\n'
                         'cut = A: 3/4" by 1 1/2" by 24"\n'
                         'cut = A: 3/4" by 1 1/2" by 12"',
                         str(self.board_result))

    def test_repr(self):
        self.assertEqual('board = Board(name="8 foot", depth="3/4", width="1 1/2", length="96")\n'
                         'cut = Board(name="A", depth="3/4", width="1 1/2", length="24")\n'
                         'cut = Board(name="A", depth="3/4", width="1 1/2", length="24")\n'
                         'cut = Board(name="A", depth="3/4", width="1 1/2", length="12")',
                         repr(self.board_result))

