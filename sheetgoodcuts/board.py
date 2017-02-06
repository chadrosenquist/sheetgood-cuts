from sheetgoodcuts import Mixed


class Board(object):
    """Represents a board.

    All measurements must be of type Mixed or a string.

    This class is immutable.
    """
    def __init__(self, name, depth, width, length):
        """Creates a new Board object.

        :param name: Name of this board.  String.
        :param depth: Length of the board.  String or Mixed.
        :param width: Width of the board.  String or Mixed.
        :param length: Depth of the board.  String or Mixed.

        :raises ValueError: If length, width, or depth are invalid.
        """
        # Note:  The constructor to Mixed will check if a string or
        # a mixed and throw ValueError if not.
        self._name = name
        self._length = Mixed(length)
        self._width = Mixed(width)
        self._depth = Mixed(depth)

    @property
    def name(self):
        """Name"""
        return self._name

    @property
    def length(self):
        """Returns the length, as a Mixed."""
        return self._length

    @property
    def width(self):
        """Returns the width, as a Mixed."""
        return self._width

    @property
    def depth(self):
        """Returns the depth, as a Mixed."""
        return self._depth

    def __str__(self):
        """Returns Board as a human readable string.

        Example: 3/4" by 2 1/2" by 48
        """
        return '{0}: {1}" by {2}" by {3}"'.format(self.name, self.depth, self.width, self.length)

    def __repr__(self):
        """Returns Board with more debug info.

        Example: Board(depth="3/4", width="2 1/2", length="48")
        """
        return '{0}(name="{1}", depth="{2}", width="{3}", length="{4}")'.format(self.__class__.__name__,
                                                                                self.name,
                                                                                self.depth,
                                                                                self.width,
                                                                                self.length)


class QuantityBoard(object):
    """This class represents a quantity and a board.  Immutable."""
    def __init__(self, quantity, board):
        """
        :param quantity: Number of boards.
        :param board: Board object.
        """
        self._quantity = quantity
        self._board = board

    @property
    def quantity(self):
        return self._quantity

    @property
    def board(self):
        return self._board

    def __str__(self):
        """Returns QuantityBoard as a human readable string.

        Example: 3 x 'A: 3/4" by 2 1/2" by 48"'"""
        return "{0} x '{1}'".format(self.quantity, self.board)

    def __repr__(self):
        """Returns QuantityBoard with more debug info.

        Example: QuantityBoard(3, Board(name="A", depth="3/4", width="2 1/2", length="48"))
        """
        return '{0}({1}, {2})'.format(self.__class__.__name__,
                                      self.quantity,
                                      repr(self.board))


class BoardResult(object):
    """This class represents a board and the cuts on that board.  Immutable."""
    def __init__(self, board, cuts):
        """
        :param board: The Board that will be cut up.
        :param cuts: The list of cuts, as Boards.
        """
        self._board = board
        self._cuts = tuple(cuts)  # Make immutable.

    @property
    def board(self):
        return self._board

    @property
    def cuts(self):
        return self._cuts

    def __str__(self):
        """Returns BoardResult as a string."""
        return_value = ""
        return_value += "board = {0}".format(str(self.board))
        for cut in self.cuts:
            return_value += "\ncut = {0}".format(str(cut))
        return return_value

    def __repr__(self):
        """Returns BoardResult with more debug info."""
        return_value = ""
        return_value += "board = {0}".format(repr(self.board))
        for cut in self.cuts:
            return_value += "\ncut = {0}".format(repr(cut))
        return return_value
