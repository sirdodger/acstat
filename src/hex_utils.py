#!/usr/bin/env python3

"""Classes and algorithms for managing hex items and their relation to each other.

"""

import typing


def lerp(
    start: typing.Union[int, float],
    end: typing.Union[int, float],
    weight: float
) -> float:
    """Return a weighted distance between two numbers.

    :param start: The start number.
    :param end: The end number.
    :param weight: The distance between the start number and end number.  Must be a float between [0.0, 1.0].
    :return: The interpolated number.
    """
    return (end - start) * weight + start


class Hex:
    """A hex coordinate.

    """

    def __init__(
        self,
        x: typing.Union[int, float],
        y: typing.Union[int, float],
        z: typing.Optional[typing.Union[int, float]]=None
    ) -> None:
        """Create a hex coordinate by passing in the axial coordinates; the third cubic coordinate is automatically
        calculated.

        :param x: The x-axis runs bottom left, to top right.
        :param y: The y-axis runs bottom right to top left.
        :param z: The z-axis runs top to bottom.

        The constructor may be called with 2-3 integers, or 2-3 floats.

        All movement between hexes thus keeps one coordinate the same, while incrementing and decrementing the other
        two coordinates.

           +y-z  +x-z
              \ /
        -x+y - * - +x-y
              / \
           -x+z  -y+z

        """
        # Calculate z if it is not provided.
        z = z if z is not None else -1 * x - y

        # Round float coordinates if necessary.
        self.x = x if isinstance(x, int) else round(x)
        self.y = y if isinstance(y, int) else round(y)
        self.z = z if isinstance(z, int) else round(z)

        # Naively rounding three float coordinates may not yield a valid hex.  Correct the coordinate that had the
        # largest rounding error.  It will also force-set z if an invalid z was passed in.
        if self.x + self.y + self.z != 0:
            x_diff = abs(self.x - x)
            y_diff = abs(self.y - y)
            z_diff = abs(self.z - z)

            # Only round float coordinates, though.
            if x_diff > y_diff and x_diff > z_diff:
                self.x = -self.y - self.z
            elif y_diff > z_diff:
                self.y = -self.x - self.z
            else:
                self.z = -self.x - self.y

    def __add__(self, other: object) -> 'Hex':
        """Add two Hexes together.

        :param other: The other hex.

        :return: The new sum Hex.

        """
        if not isinstance(other, Hex):
            raise TypeError('unsupported operand type(s) for +: \'Hex\' and \'{}\''.format(type(other)))
        return Hex(self.x + other.x, self.y + other.y, self.z + other.z)

    def __eq__(self, other: object) -> bool:
        """Hexes with the same coordinates are equal.  Ignore z value, since it is derived.

        :param other: The other Hex to test.
        :return: True if equal, False otherwise.

        """
        return isinstance(other, Hex) and self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        """Unique hash for a hex.  Ignore z value, since it is derived.

        :return: Hash value.

        """
        return hash((self.x, self.y, ))

    def __repr__(self) -> str:
        """Return a string representation of a hex.

        :return: String
        """
        return 'Hex({}, {}, {})'.format(self.x, self.y, self.z)

    def __sub__(self, other: object) -> 'Hex':
        """Subtract another hex from this hex.

        :param other: The other hex.

        :return: The new Hex.

        """
        if not isinstance(other, Hex):
            raise TypeError('unsupported operand type(s) for -: \'Hex\' and \'{}\''.format(type(other)))
        return Hex(self.x - other.x, self.y - other.y, self.z - other.z)

    def distance(self, other: 'Hex') -> int:
        """The distance from this hex to another hex.

        :param other: The other hex.

        :return: Positive integer distance.

        """
        return max(abs(self.x - other.x), abs(self.y - other.y), abs(self.z - other.z))

    def lerp(self, other: 'Hex', weight: float) -> 'Hex':
        """Return the hex interpolated between this hex and another hex.

        :param other: The other hex.
        :param weight: How far between the two hexes the interpolated hex should be.
        :return: A hex equal to or between the two hexes.

        """
        return Hex(lerp(self.x, other.x, weight), lerp(self.y, other.y, weight), lerp(self.z, other.z, weight))

    def line(self, other: 'Hex') -> typing.Generator['Hex', None, None]:
        """Return a straight line of hexes from the current hex to another hex.  Does not include the start hex, but
        does include the end hex.

        :param other: The hex to which to draw a line.

        :return: A generator of Hexes in a line.

        """
        distance = self.distance(other)
        for i in range(1, distance):
            weight = 1.0 / distance * i
            yield self.lerp(other, weight)
        yield other


# Arbitrarily set the -z direction to be north, and base the six directions an object can move off that.
DIRECTIONS: typing.Dict[str, Hex] = {
    'NW': Hex(x=0,  y=1,  z=-1),
    'NE': Hex(x=1,  y=0,  z=-1),
    'E':  Hex(x=1,  y=-1, z=0),
    'SE': Hex(x=0,  y=-1, z=1),
    'SW': Hex(x=-1, y=0,  z=1),
    'W':  Hex(x=-1, y=1,  z=0),
}
