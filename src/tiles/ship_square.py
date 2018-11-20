#!/usr/bin/env python3

"""Squares that comprise a tile.

"""

from __future__ import annotations

import curses
import typing


class ShipSquare(object):
    """An individual square on a ship tile.

    """

    ATTRIBUTES = curses.A_DIM
    CHARACTER = ''
    COLOR = curses.COLOR_WHITE

    def __init__(self, color: int) -> None:
        self.color = color

    def draw(self, screen: typing.Any, offset_x: int, offset_y: int, color: int) -> None:
        """Draw a single square in a ship tile.

        :param screen: The curses window.

        :param offset_x: The absolute x value of the square.

        :param offset_y: The absolute y value of the square.

        :param color: The curses foreground color index to color the square.

        """
        screen.addstr(offset_y, offset_x, self.CHARACTER, curses.color_pair(color))


class DecorativeSquare(ShipSquare):
    """A decorative square that cannot be interacted with in any way.

    """
    CHARACTER = '█'


class InteractiveSquare(ShipSquare):
    """Abstract base class for squares that characters can walk on, interact with, etc.

    """


class ActionSquare(InteractiveSquare):
    """A computer terminal interaction square.

    """
    CHARACTER = '©'


class BlankSquare(InteractiveSquare):
    """A square with no permanent features.

    """
    CHARACTER = ' '


class TractorSquare(BlankSquare):
    """The tractor beam pulls objects into this otherwise featureless square.

    """
    CHARACTER = '▀'
