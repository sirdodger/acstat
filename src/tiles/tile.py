#!/usr/bin/env python3


import contextlib
import functools


class Tile(object):
    """A single room on a ship.

    """

    SIZE = 5
    WALL_CHAR = '#'

    def __init__(self, ship, location_x, location_y):
        self.ship = ship
        self.location_x = location_x
        self.location_y = location_y

    @functools.lru_cache(maxsize=8)
    def corner_extends(self, corner, direction):
        if corner not in ('ne', 'nw', 'se', 'sw', ):
            raise ValueError('Bad corner: {}'.format(corner))
        if direction not in {'n', 's', 'e', 'w', }:
            raise ValueError('Bad direction: {}'.format(direction))

        return self.has_neighbor(corner) or self.has_neighbor(direction)

    def has_neighbor(self, direction):
        return self.neighbor(direction) is not None

    @functools.lru_cache(maxsize=8)
    def neighbor(self, direction):

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
            neighbor = self.ship.get_tile_by_position(x, y)

        return neighbor
