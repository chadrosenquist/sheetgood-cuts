"""Provides APIs to best make cuts in sheetgoods."""

from fractions import Fraction
from sheetgoodcuts import Mixed


class Board(object):
    """Represents a board.

    All measurements must be of type Mixed or a string.

    This class is immutable.
    """
    def __init__(self, depth, width, length):
        """Creates a new Board object.

        Args:
            length: Length of the board.  String or Mixed.
            width: Width of the board.  String or Mixed.
            depth: Depth of the board.  String or Mixed.

        Returns:
            Board object

        Raises:
            ValueError: If length, width, or depth are invalid.
        """
        self._length = Mixed(length)
        self._width = Mixed(width)
        self._depth = Mixed(depth)

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
        return '{0}" by {1}" by {2}"'.format(self.depth, self.width, self.length)

    def __repr__(self):
        """Returns Board with more debug info.
        Example: Board(depth="3/4", width="2 1/2", length="48")
        """
        return '{0}(depth="{1}", width="{2}", length="{3}")'.format(self.__class__.__name__,
                                                                    self.depth,
                                                                    self.width,
                                                                    self.length)