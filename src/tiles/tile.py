#!/usr/bin/env python3

from __future__ import annotations

import contextlib
import functools

import ship  # Circular import for typing only


class Tile(object):
    """A single room on a ship.

    """

    DOORS = {
        'n': True,
        's': True,
        'e': True,
        'w': True,
    }

    SIZE = 5
    WALL_CHAR = '#'

    def __init__(self, parent_ship: ship.Ship, location_x: int, location_y: int) -> None:
        """Create a ship from a 2D array of tile abbreviations.

        :param parent_ship: The parent ship containing this tile.

        :param location_x: The x value of the tile in the ship's structure.

        :param location_y: The y value of the tile in the ship's structure.
        """
        self.parent_ship = parent_ship
        self.location_x = location_x
        self.location_y = location_y

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

    def has_door(self, direction: str) -> bool:
        """Does the tile have a door in a particular direction.

        :param direction: The string defining the direction in which to check for a door.  (e.g., 'n', 'sw', etc.)

        :return: True if door exists, False otherwise.

        """
        return self.DOORS.get(direction) and self.has_neighbor(direction)

    def has_neighbor(self, direction: str) -> bool:
        """Does the tile have a neighbor in a particular direction?

        :param direction: The string defining the direction in which to check for a neighbor.  (e.g., 'n', 'sw', etc.)

        :return: True if neighbor exists, False otherwise.

        """
        return self.neighbor(direction) is not None

    @functools.lru_cache(maxsize=8)
    def neighbor(self, direction: str) -> Tile:
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
