import unittest

from fractions import Fraction
from sheetgoodcuts import Mixed


class MixedConstructorTest(unittest.TestCase):
    """Performs constructor unit testing for the Mixed class."""
    def test_whole_only(self):
        measure = Mixed("    40  ")
        self.assertEqual(measure.whole, 40)
        self.assertEqual(measure.fraction, Fraction("0"))
        self.assertEqual(str(measure), "40")
        self.assertEqual(repr(measure), 'Mixed("40")')

    def test_invalid_string_for_whole(self):
        with self.assertRaises(ValueError):
            Mixed("abc")

    def test_fraction_only(self):
        measure = Mixed(" 3/4  ")
        self.assertEqual(measure.whole, 0)
        self.assertEqual(measure.fraction, Fraction("3/4"))
        self.assertEqual(str(measure), "3/4")
        self.assertEqual(repr(measure), 'Mixed("3/4")')

    def test_whole_and_fraction(self):
        measure = Mixed(" 48 1/16 ")
        self.assertEqual(measure.whole, 48)
        self.assertEqual(measure.fraction, Fraction("1/16"))
        self.assertEqual(str(measure), "48 1/16")
        self.assertEqual(repr(measure), 'Mixed("48 1/16")')

    def test_zero(self):
        measure = Mixed("0")
        self.assertEqual(measure.whole, 0)
        self.assertEqual(measure.fraction, Fraction("0"))
        self.assertEqual(str(measure), "0")
        self.assertEqual(repr(measure), 'Mixed("0")')

    def test_immutable(self):
        measure = Mixed("3 1/2")
        with self.assertRaises(AttributeError):
            measure.whole = 1
        with self.assertRaises(AttributeError):
            measure.fraction = Fraction("1/2")

    def test_copy_constructor(self):
        measure = Mixed("6 7/8")
        measure2 = Mixed(measure)
        self.assertEqual(str(measure), "6 7/8")


class MixedComparisonTest(unittest.TestCase):
    """Performs comparision unit testing for the Mixed class.

    Note that the comparison are not exhaustively tested.
    This is because they simply call Fraction.
    """
    def setUp(self):
        self.a = Mixed("10 3/4")
        self.b = Mixed("5 1/2")

    def test_equal(self):
        self.assertTrue(self.a == self.a)

    def test_not_equal(self):
        self.assertTrue(self.a != self.b)

    def test_greater_than(self):
        self.assertTrue(self.a > self.b)

    def test_less_than(self):
        self.assertTrue(self.b < self.a)

    def test_greater_equal(self):
        self.assertTrue(self.a >= self.a)

    def test_less_equal(self):
        self.assertTrue(self.a <= self.a)


class MixedArithmeticTest(unittest.TestCase):
    """Tests arithmetic unit testing on the Mixed class.

    Note that these tests are not exhaustive because they
    simply call Fraction.
    """
    def setUp(self):
        self.a = Mixed("10 3/4")
        self.b = Mixed("5 1/2")

    def test_add(self):
        self.assertEqual(self.a + self.b, Mixed("16 1/4"))

    def test_sub(self):
        self.assertEqual(self.a - self.b, Mixed("5 1/4"))

    def test_mul(self):
        self.assertEqual(self.a * self.b, Mixed("59 1/8"))

    def test_div(self):
        self.assertEqual(self.a / self.b, Mixed("1 21/22"))

if __name__ == '__main__':
    unittest.main()
