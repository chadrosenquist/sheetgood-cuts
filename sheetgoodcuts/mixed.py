from fractions import Fraction
import re


class Mixed(object):
    """Represents a mixed number.

    There is whole number and a fraction.

    This class immutable.

    >>> x = Mixed("10 1/2")
    >>> x.whole
    10
    >>> x.fraction
    Fraction(1, 2)
    >>> x
    Mixed("10 1/2")

    """
    def __init__(self, number):
        """Creates a new mixed number.

        Args:
            number: Mixed number in whole, and fraction.  Can be a string or another Mixed.

        Returns:
            Mixed object.

        Raises:
            ValueError: If mixed_as_string is invalid.
        """
        # If another Mixed, copy and return.
        if isinstance(number, Mixed):
            self._mixed = number.mixed
            return

        number = number.strip()

        # Check for fraction only.
        match_object = re.match(r'(\d+)/(\d+)', number)
        if match_object:
            self._mixed = Fraction(number)
            return

        # Check for whole and fraction.
        match_object = re.match(r'(\d+) (\d+)/(\d+)', number)
        if match_object:
            self._mixed = int(match_object.group(1)) + Fraction(numerator=int(match_object.group(2)), denominator=int(match_object.group(3)))
            return

        # Whole only.  No fraction.
        self._mixed = Fraction(numerator=int(number))

    @property
    def whole(self):
        """Returns the whole number as an integer."""
        return int(self._mixed.numerator / self._mixed.denominator)

    @property
    def fraction(self):
        """Returns the fraction as a Fraction."""
        return self._mixed - self.whole

    @property
    def mixed(self):
        """Returns the mixed number as a Fraction."""
        return self._mixed

    def __str__(self):
        """Returns the mixed as a human readable string."""
        return_string = ""
        if self.whole != 0:
            return_string += "{0}".format(self.whole)
        if self.fraction != Fraction("0"):
            if return_string:
                return_string += " "         # Add space between inches and fraction.
            return_string += str(self.fraction)

        # Check for zero.
        if not return_string:
            return_string = "0"
        return return_string

    def __repr__(self):
        """Returns the measurement with more debug info.
        Example: Mixed("48 1/16")"""
        return '{0}("{1}")'.format(self.__class__.__name__, str(self))

    def __eq__(self, other):
        """Equal"""
        return self._mixed == other.mixed

    def __ne__(self, other):
        """Not equal"""
        return self._mixed != other.mixed

    def __gt__(self, other):
        """Greater than"""
        return self.mixed > other.mixed

    def __lt__(self, other):
        """Less than"""
        return self.mixed < other.mixed

    def __ge__(self, other):
        """Greater than or equal"""
        return self.mixed >= other.mixed

    def __le__(self, other):
        """Less than or equal"""
        return self.mixed <= other.mixed

    def __add__(self, lhs):
        """Add"""
        return Mixed(str(self.mixed + lhs.mixed))

    def __radd__(self, rhs):
        """Add"""
        return Mixed(str(rhs.mixed + self.mixed))

    def __sub__(self, lhs):
        """Subtract"""
        return Mixed(str(self.mixed - lhs.mixed))

    def __rsub__(self, rhs):
        """Subtract"""
        return Mixed(str(rhs.mixed - self.mixed))

    def __mul__(self, lhs):
        """Multiply"""
        return Mixed(str(self.mixed * lhs.mixed))

    def __rmul__(self, rhs):
        """Multiply"""
        return Mixed(str(rhs.mixed * self.mixed))

    def __floordiv__(self, lhs):
        """Divide"""
        return Mixed(str(self.mixed / lhs.mixed))

    def __truediv__(self, lhs):
        """Divide"""
        return Mixed(str(self.mixed / lhs.mixed))
