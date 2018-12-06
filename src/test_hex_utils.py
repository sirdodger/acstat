#!/usr/bin/env python3

"""Tests for the Hex class.

"""

import unittest

import hex_utils


class HexTests(unittest.TestCase):
    """Test the Hex class.

    """

    def test_init__integers(self):
        """An absent z value is calculated.

        """
        h = hex_utils.Hex(1, 3)
        self.assertEqual(-4, h.z)
        self.assertEqual(1, h.x)
        self.assertEqual(3, h.y)
        self.assertEqual(-4, h.z)

    def test_init__integers_with_z(self):
        """A provided z value is set.

        """
        h = hex_utils.Hex(2, -4, 2)
        self.assertEqual(2, h.x)
        self.assertEqual(-4, h.y)
        self.assertEqual(2, h.z)

    def test_init__integers_with_invalid_z(self):
        """Invalid z is overwritten.

        """
        h = hex_utils.Hex(-1, -7, 17)
        self.assertEqual(-1, h.x)
        self.assertEqual(-7, h.y)
        self.assertEqual(8, h.z)

    def test_init__floats(self):
        """A Hex created from floats has the highest value trimmed as necessary to land on valid coordinates.

        """
        h = hex_utils.Hex(1.3, 3.4, -4.9)
        self.assertEqual(1, h.x)
        self.assertEqual(4, h.y)
        self.assertEqual(-5, h.z)

    def test_eq(self):
        """Two hexes with the same coordinates are equal.

        """
        h = hex_utils.Hex(1, 4)
        h2 = hex_utils.Hex(1, 4)
        self.assertEqual(h, h2)

    def test_repr(self):
        """Hexes have a reasonable print value.

        """
        h = hex_utils.Hex(1, -4, 3)
        s = repr(h)
        self.assertEqual('Hex(1, -4, 3)', s)

    def test_direction(self):
        """Take a step in each direction.

        """
        h = hex_utils.Hex(0, 0)
        self.assertEqual(hex_utils.Hex(0, 1, -1), h + hex_utils.DIRECTIONS['NW'])
        self.assertEqual(hex_utils.Hex(1, 0, -1), h + hex_utils.DIRECTIONS['NE'])
        self.assertEqual(hex_utils.Hex(1, -1, 0), h + hex_utils.DIRECTIONS['E'])
        self.assertEqual(hex_utils.Hex(0, -1, 1), h + hex_utils.DIRECTIONS['SE'])
        self.assertEqual(hex_utils.Hex(-1, 0, 1), h + hex_utils.DIRECTIONS['SW'])
        self.assertEqual(hex_utils.Hex(-1, 1, 0), h + hex_utils.DIRECTIONS['W'])

    def test_distance(self):
        """Distance between hexes.

        """
        h = hex_utils.Hex(-1, -2)
        h2 = hex_utils.Hex(2, 2)
        self.assertEqual(7, h.distance(h2))

    def test_line(self):
        """Distance between hexes.

        """
        h = hex_utils.Hex(-3, 2)
        h2 = hex_utils.Hex(1, 1)

        line = [x for x in h.line(h2)]

        self.assertEqual([hex_utils.Hex(-2, 2), hex_utils.Hex(-1, 2), hex_utils.Hex(0, 1), hex_utils.Hex(1, 1)], line)


class LerpTests(unittest.TestCase):
    """Test linear interpolation.

    """

    def test_lerp(self):
        self.assertEqual(2.0, hex_utils.lerp(1, 3, 0.5))


if __name__ == '__main__':
    unittest.main()
