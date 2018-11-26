#!/usr/bin/env python3

"""Sick bay tile.

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


class SickBayTile(Tile):
    """The sick bay diagnoses diseases and heals injured or dying characters.

    """

    ABBREVIATION: str = 'sc'

    COLOR = colors.GREEN_BACKGROUND

    DEFINITION: typing.List[typing.List[typing.Type[tiles.ship_square.ShipSquare]]] = [
        [DecorativeSquare, BlankSquare,      BlankSquare,      BlankSquare,      DecorativeSquare, ],
        [BlankSquare,      ActionSquare,     DecorativeSquare, BlankSquare,      BlankSquare,      ],
        [BlankSquare,      DecorativeSquare, DecorativeSquare, DecorativeSquare, BlankSquare,      ],
        [BlankSquare,      BlankSquare,      DecorativeSquare, ActionSquare,     BlankSquare,      ],
        [DecorativeSquare, BlankSquare,      BlankSquare,      BlankSquare,      DecorativeSquare, ],
    ]

    # Top, right, bottom, left
    DOORS: typing.List[bool] = [True, True, True, True]
