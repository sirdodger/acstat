#!/usr/bin/env python3

"""Teleporter tile.

"""

from __future__ import annotations

import typing

import colors
import tiles.ship_square
from .ship_square import (
    ActionSquare,
    BlankSquare,
    DecorativeSquare,
)
from .tile import Tile


class TeleporterTile(Tile):
    """The teleporter transports people or bombs to another ship.  It cannot transport to celestial bodies, deep
    space, or the same ship.

    """

    ABBREVIATION: str = 'tp'

    COLOR = colors.GREEN_BACKGROUND

    DEFINITION: typing.List[typing.List[typing.Type[tiles.ship_square.ShipSquare]]] = [
        [DecorativeSquare, DecorativeSquare, BlankSquare,      DecorativeSquare, DecorativeSquare, ],
        [DecorativeSquare, ActionSquare,     BlankSquare,      BlankSquare,      DecorativeSquare, ],
        [BlankSquare,      BlankSquare,      BlankSquare,      BlankSquare,      BlankSquare,      ],
        [DecorativeSquare, BlankSquare,      BlankSquare,      ActionSquare,     DecorativeSquare, ],
        [DecorativeSquare, DecorativeSquare, BlankSquare,      DecorativeSquare, DecorativeSquare, ],
    ]
