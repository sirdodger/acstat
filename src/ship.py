#!/usr/bin/env python3

from __future__ import annotations

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

    def __init__(self, definition: typing.Sequence[typing.Sequence[typing.Optional[str]]]) -> None:
        """Create a ship from a 2D array of string tile abbreviations.

        :param definition: 2D array of tile abbreviations.
        """
        structure = []

        for y, definition_row in enumerate(definition):
            ship_row = []
            for x, tile_abbreviation in enumerate(definition_row):

                tile_class = tiles.TILES.get(tile_abbreviation)
                if tile_class:
                    ship_row.append(tile_class(self, x, y))
                else:
                    ship_row.append(None)

            structure.append(ship_row)

        self._structure: typing.Sequence[typing.Sequence[typing.Optional[tiles.Tile]]] = structure

    def get_tile_by_position(self, x: int, y: int) -> tiles.Tile:
        """Retrieve a tile by coordinates.

        :param x: The horizontal position.

        :param y: The vertical position.

        :return: The tile, or None if no tile exists at that position.

        """
        return self._structure[y][x]

    def draw(self, screen: typing.Any) -> None:
        """Draw a ship to ASCII.

        :param screen: The curses window.
        :type screen: The curses window as returned from curses.initscr() et al.

        """

        horizontal_line: typing.Optional[str] = self.LINES.get((False, True, False, True, ))
        vertical_line: typing.Optional[str] = self.LINES.get((True, False, True, False, ))

        for y, structure_row in enumerate(self._structure):
            for x, active_tile in enumerate(structure_row):

                if active_tile is not None:

                    top_wall = '{top_left}{wall}{top_right}'.format(
                        top_left=self.LINES.get(
                            (active_tile.corner_extends('nw', 'n'), True, True, active_tile.corner_extends('nw', 'w'), )
                        ),
                        wall=horizontal_line * active_tile.SIZE,
                        top_right=self.LINES.get(
                            (active_tile.corner_extends('ne', 'n'), active_tile.corner_extends('ne', 'e'), True, True, )
                        )
                    )
                    side_wall = '{vertical}{tile}{vertical}'.format(
                        vertical=vertical_line,
                        tile='x' * active_tile.SIZE
                    )

                    bottom_wall = '{bottom_left}{wall}{bottom_right}'.format(
                        bottom_left=self.LINES.get(
                            (True, True, active_tile.corner_extends('sw', 's'), active_tile.corner_extends('sw', 'w'), )
                        ),
                        wall=horizontal_line * active_tile.SIZE,
                        bottom_right=self.LINES.get(
                            (True, active_tile.corner_extends('se', 'e'), active_tile.corner_extends('se', 's'), True,)
                        )
                    )

                    # Calculate offsets to currently drawing tile, add border widths
                    offset_left = x * (active_tile.SIZE + 1)
                    offset_top = y * (active_tile.SIZE + 1)

                    screen.addstr(offset_top, offset_left, top_wall)
                    for i in range(1, active_tile.SIZE + 1):
                        screen.addstr(offset_top + i, offset_left, side_wall)

                    screen.addstr(offset_top + active_tile.SIZE + 1, offset_left, bottom_wall)
