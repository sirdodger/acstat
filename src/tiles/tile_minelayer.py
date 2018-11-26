#!/usr/bin/env python3

"""Mine layer tile.

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


class MineLayerTile(Tile):
    """Mine layers launch mines into empty space hexes.

    It must have exterior facing.
    """

    ABBREVIATION: str = 'ml'

    COLOR = colors.BLUE_BACKGROUND

    DEFINITION: typing.List[typing.List[typing.Type[tiles.ship_square.ShipSquare]]] = [
        [DecorativeSquare, BlankSquare,      BlankSquare,      BlankSquare,      BlankSquare,      ],
        [DecorativeSquare, DecorativeSquare, DecorativeSquare, DecorativeSquare, BlankSquare,      ],
        [DecorativeSquare, DecorativeSquare, DecorativeSquare, DecorativeSquare, BlankSquare,      ],
        [DecorativeSquare, ActionSquare,     BlankSquare,      BlankSquare,      BlankSquare,      ],
        [DecorativeSquare, DecorativeSquare, BlankSquare,      BlankSquare,      DecorativeSquare, ],
    ]

    # Top, right, bottom, left
    DOORS: typing.List[bool] = [True, True, True, False]
