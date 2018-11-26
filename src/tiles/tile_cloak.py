#!/usr/bin/env python3

"""Cloaking device tile.

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


class CloakingTile(Tile):
    """The cloaking tile makes it harder to detect a ship.
    """

    ABBREVIATION: str = 'cl'

    COLOR = colors.GREEN_BACKGROUND

    DEFINITION: typing.List[typing.List[typing.Type[tiles.ship_square.ShipSquare]]] = [
        [DecorativeSquare, DecorativeSquare, DecorativeSquare, DecorativeSquare, DecorativeSquare, ],
        [DecorativeSquare, DecorativeSquare, ActionSquare,     BlankSquare,      DecorativeSquare, ],
        [BlankSquare,      DecorativeSquare, BlankSquare,      BlankSquare,      BlankSquare,      ],
        [BlankSquare,      DecorativeSquare, DecorativeSquare, BlankSquare,      DecorativeSquare, ],
        [BlankSquare,      BlankSquare,      BlankSquare,      BlankSquare,      DecorativeSquare, ],
    ]

    # Top, right, bottom, left
    DOORS: typing.List[bool] = [False, True, True, True]
