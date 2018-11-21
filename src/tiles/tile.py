#!/usr/bin/env python3

"""The base class for all tiles that comprise a ship.

"""

from __future__ import annotations

import collections
import contextlib
import functools
import typing

import colors
import ship  # Circular import for typing only
import tiles.ship_square
import utils


class Tile(object):
    """A single room on a ship.

    """

    ABBREVIATION: str = ''
    COLOR: int = colors.WHITE
    DEFINITION: typing.List[typing.List[typing.Type[tiles.ship_square.ShipSquare]]] = []

    # Top, right, bottom, left
    DOORS: typing.List[bool] = [True, True, True, True]

    SIZE: int = 5
    TARGETS: typing.Dict[int, typing.Tuple[int, int]] = {}
    WALL_CHAR: str = '#'

    def __init__(self, parent_ship: ship.Ship, location_x: int, location_y: int, rotation: int = 0) -> None:
        """Create a ship from a 2D array of tile abbreviations.

        :param parent_ship: The parent ship containing this tile.

        :param location_x: The x value of the tile in the ship's structure.

        :param location_y: The y value of the tile in the ship's structure.

        :param rotation: Thu number of clockwise 90-degree rotations.

        """
        self.parent_ship: ship.Ship = parent_ship
        self.location_x: int = location_x
        self.location_y: int = location_y
        self.rotation: int = rotation

        squares = []

        rotated_definition = utils.rotate_2d_array(self.DEFINITION, rotation)

        _definition_row: typing.List[typing.Type[tiles.ship_square.ShipSquare]]
        for y, _definition_row in enumerate(rotated_definition):
            square_row = []
            for x, square_class in enumerate(_definition_row):

                if square_class:
                    square_row.append(square_class(color=self.COLOR))
                else:
                    square_row.append(None)

            squares.append(square_row)

        rotated_doors = collections.deque(self.DOORS)
        rotated_doors.rotate(rotation)
        self._doors = {'n': rotated_doors[0], 'e': rotated_doors[1], 's': rotated_doors[2], 'w': rotated_doors[3], }
        self._squares: typing.Sequence[typing.Sequence[tiles.ship_square.ShipSquare]] = squares

    @functools.lru_cache(maxsize=8)
    def corner_extends(self, corner: str, direction: str) -> bool:
        """Determine if a corner wall extends in a direction (because it neighbors another tile).

        :param corner: The intercardinal corner to check.  (e.g., 'ne', 'sw', etc.)

        :param direction: The direction in which to check for the extending wall.  (e.g., 'n', 's', etc.)

        :return: True if the wall extends in that direction, False otherwise.

        """
        if corner not in ('ne', 'nw', 'se', 'sw', ):
            raise ValueError('Bad corner: {}'.format(corner))
        if direction not in {'n', 's', 'e', 'w', }:
            raise ValueError('Bad direction: {}'.format(direction))

        return self.has_neighbor(corner) or self.has_neighbor(direction)

    def draw(self, screen: typing.Any, offset_x: int, offset_y: int) -> None:
        """Enumerate through the tile squares and draw them on the screen.

        :param screen: The curses screen.

        :param offset_x: The absolute x value of the top-left of the tile.

        :param offset_y: The absolute y value of the top-left of the tile.

        """
        for y, square_row in enumerate(self._squares):
            for x, active_square in enumerate(square_row):
                active_square.draw(screen, offset_x + x, offset_y + y, self.COLOR)

    def has_door(self, direction: str) -> bool:
        """Does the tile have a door in a particular direction.

        :param direction: The string defining the direction in which to check for a door.  (e.g., 'n', 'sw', etc.)

        :return: True if door exists, False otherwise.

        """
        return self._doors[direction] and self.has_neighbor(direction)

    def has_neighbor(self, direction: str) -> bool:
        """Does the tile have a neighbor in a particular direction?

        :param direction: The string defining the direction in which to check for a neighbor.  (e.g., 'n', 'sw', etc.)

        :return: True if neighbor exists, False otherwise.

        """
        return self.neighbor(direction) is not None

    @functools.lru_cache(maxsize=8)
    def neighbor(self, direction: str) -> typing.Optional[Tile]:
        """Retrieve the neighbor in any cardinal/intercardinal direction.

        Memoize results for performance, so changing tiles can yield incorrect results.

        :param direction: The string defining the direction in which to check for a neighbor.  (e.g., 'n', 'sw', etc.)

        :return: The Tile instance or None if no neighbor exists.

        """

        if direction not in {'n', 's', 'e', 'w', 'ne', 'nw', 'se', 'sw', }:
            raise ValueError('Bad direction: {}'.format(direction))

        x = self.location_x
        y = self.location_y

        if 'n' in direction:
            y -= 1
        elif 's' in direction:
            y += 1

        if 'e' in direction:
            x += 1
        elif 'w' in direction:
            x -= 1

        # Variable is used if suppress() catches an exception.
        # noinspection PyUnusedLocal
        neighbor = None
        with contextlib.suppress(IndexError):
            # Indexes of -1 will return the rightmost element instead of raising an exception, so force-raise one
            if x < 0 or y < 0:
                raise IndexError
            neighbor = self.parent_ship.get_tile_by_position(x, y)

        return neighbor
