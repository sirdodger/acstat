#!/usr/bin/env python3

"""Classes and algorithms for managing hex items and their relation to each other.

"""

import typing


class Hex(object):
    """A hex coordinate.

    """

    def __init__(self, x: int, y: int, z: typing.Optional[int]=None) -> None:
        """Create a hex coordinate by passing in the axial coordinates; the third cubic coordinate is automatically
        calculated.

        :param x: The x-axis runs bottom left, to top right.
        :param y: The y-axis runs bottom right to top left.
        :param z: The z-axis runs top to bottom.

        All movement between hexes thus keeps one coordinate the same, while incrementing and decrementing the other
        two coordinates.

           +y-z  +x-z
              \ /
        -x+y - * - +x-y
              / \
           -x+z  -y+z

        """
        self.x: int = x
        self.y: int = y
        self.z: int = z if z is not None else -1 * x - y

        # "+++Divide By Cucumber Error. Please Reinstall Universe And Reboot+++" - Terry Pratchett
        assert self.x + self.y + self.z == 0


# Arbitrarily set the -z direction to be north, and base the six directions an object can move off that.
DIRECTIONS: typing.Dict[str, Hex] = {
    'NW': Hex(x=0,  y=1,  z=-1),
    'NE': Hex(x=1,  y=0,  z=-1),
    'E':  Hex(x=1,  y=-1, z=0),
    'SE': Hex(x=0,  y=-1, z=1),
    'SW': Hex(x=-1, y=0,  z=1),
    'W':  Hex(x=-1, y=1,  z=0),
}
