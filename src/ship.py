#!/usr/bin/env python3

"""A ship structure and interior layout.

"""

from __future__ import annotations

import math
import typing

import tiles


class Ship(object):
    """A spaceship comprised of tiles.

    """

    # The line to draw depending on how it connects to (top, right, bottom, left) neighbors.
    LINES: typing.Mapping[typing.Tuple, str] = {
        (True, False, True, False, ): '║',  # ASCII 186
        (False, True, False, True, ): '═',  # ASCII 205

        (False, True, True, False, ): '╔',  # ASCII 201
        (False, False, True, True, ): '╗',  # ASCII 187
        (True, False, False, True,):  '╝',  # ASCII 188
        (True, True, False, False,):  '╚',  # ASCII 200

        (False, True, True, True, ):  '╦',  # ASCII 203
        (True, False, True, True,):   '╣',  # ASCII 185
        (True, True, False, True, ):  '╩',  # ASCII 202
        (True, True, True, False,):   '╠',  # ASCII 204

        (True, True, True, True, ):   '╬',  # ASCII 206
    }

    def __init__(
            self,
            definition: typing.Sequence[typing.Sequence[typing.Optional[str]]],
            rotation: typing.Sequence[typing.Sequence[int]]
    ) -> None:
        """Create a ship from a 2D array of string tile abbreviations.

        :param definition: 2D array of tile abbreviations.
        """
        tile_count = 0
        structure = []

        center_x = 0.0
        center_y = 0.0
        for y, definition_row in enumerate(definition):
            ship_row = []
            for x, tile_abbreviation in enumerate(definition_row):
                tile_class = tiles.TILES.get(tile_abbreviation)
                if tile_class:
                    center_x += x
                    center_y += y
                    ship_row.append(tile_class(self, x, y, rotation[y][x]))
                    tile_count += 1
                else:
                    ship_row.append(None)

            structure.append(ship_row)

        # Find the coordinates of the tile containing the center of mass.
        self.center = int(center_x / tile_count), int(center_y / tile_count)

        # The size of a ship determines difficulty numbers, targeting silhouette, etc.
        self.size = int(math.ceil(((tile_count - 6) / 3.0 ) + 4))
        self._structure: typing.Sequence[typing.Sequence[typing.Optional[tiles.Tile]]] = structure

    def get_tile_by_position(self, x: int, y: int) -> tiles.Tile:
        """Retrieve a tile by coordinates.

        :param x: The horizontal position.

        :param y: The vertical position.

        :return: The tile, or None if no tile exists at that position.

        """
        return self._structure[y][x]

    def draw(self, screen: typing.Any, offset_x: int = 0, offset_y: int = 0) -> None:
        """Draw a ship to ASCII.

        :param screen: The curses window.
        :type screen: The curses window as returned from curses.initscr() et al.

        :param offset_x: The x offset at which to start drawing the ship.

        :param offset_y: The y offset at which to start drawing the ship.

        """

        horizontal_line: str = self.LINES[(False, True, False, True, )]
        vertical_line: str = self.LINES[(True, False, True, False, )]

        for y, structure_row in enumerate(self._structure):
            for x, active_tile in enumerate(structure_row):

                if active_tile is not None:

                    half_wall = horizontal_line * int(active_tile.SIZE / 2)
                    top_wall = '{top_left}{half_wall}{door}{half_wall}{top_right}'.format(
                        top_left=self.LINES[
                            (active_tile.corner_extends('nw', 'n'), True, True, active_tile.corner_extends('nw', 'w'), )
                        ],
                        half_wall=half_wall,
                        door=' ' if active_tile.has_door('n') else horizontal_line,
                        top_right=self.LINES[
                            (active_tile.corner_extends('ne', 'n'), active_tile.corner_extends('ne', 'e'), True, True, )
                        ]
                    )

                    side_wall = '{vertical}{tile}{vertical}'.format(
                        vertical=vertical_line,
                        tile='x' * active_tile.SIZE
                    )

                    door_wall = '{vertical_left}{tile}{vertical_right}'.format(
                        vertical_left=' ' if active_tile.has_door('w') else vertical_line,
                        vertical_right=' ' if active_tile.has_door('e') else vertical_line,
                        tile='x' * active_tile.SIZE
                    )

                    bottom_wall = '{bottom_left}{half_wall}{door}{half_wall}{bottom_right}'.format(
                        bottom_left=self.LINES[
                            (True, True, active_tile.corner_extends('sw', 's'), active_tile.corner_extends('sw', 'w'), )
                        ],
                        half_wall=half_wall,
                        door=' ' if active_tile.has_door('s') else horizontal_line,
                        bottom_right=self.LINES[
                            (True, active_tile.corner_extends('se', 'e'), active_tile.corner_extends('se', 's'), True,)
                        ]
                    )

                    # Calculate offsets to currently drawing tile, add border widths
                    offset_left = offset_x + x * (active_tile.SIZE + 1)
                    offset_top = offset_y + y * (active_tile.SIZE + 1)

                    # Draw top wall
                    screen.addstr(offset_top, offset_left, top_wall)

                    # Draw top of middle walls
                    middle = int(active_tile.SIZE / 2) + 1
                    for i in range(1, middle):
                        screen.addstr(offset_top + i, offset_left, side_wall)
                    # Draw door wall
                    screen.addstr(offset_top + middle, offset_left, door_wall)
                    # Draw bottom of middle walls
                    for i in range(middle + 1, active_tile.SIZE + 1):
                        screen.addstr(offset_top + i, offset_left, side_wall)

                    # Draw bottom wall
                    screen.addstr(offset_top + active_tile.SIZE + 1, offset_left, bottom_wall)

                    active_tile.draw(screen, offset_left + 1, offset_top + 1)
