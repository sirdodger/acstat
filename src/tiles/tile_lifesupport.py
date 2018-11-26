#!/usr/bin/env python3

"""Life support tile.

"""

from __future__ import annotations

import typing

import colors
import tiles.ship_square
from .ship_square import (
    BlankSquare,
    DecorativeSquare,
)
from .tile import Tile


class LifeSupportTile(Tile):
    """Life support can handle four crew members, five if upgraded.  It can temporarily support many more passengers,
    but extended overuse results in severe health consequences.

    """

    ABBREVIATION: str = 'ls'

    COLOR = colors.WHITE

    DEFINITION: typing.List[typing.List[typing.Type[tiles.ship_square.ShipSquare]]] = [
        [DecorativeSquare, DecorativeSquare, BlankSquare, DecorativeSquare, DecorativeSquare, ],
        [DecorativeSquare, DecorativeSquare, BlankSquare, DecorativeSquare, DecorativeSquare, ],
        [BlankSquare,      BlankSquare,      BlankSquare, BlankSquare,      BlankSquare,      ],
        [DecorativeSquare, DecorativeSquare, BlankSquare, DecorativeSquare, DecorativeSquare, ],
        [DecorativeSquare, DecorativeSquare, BlankSquare, DecorativeSquare, DecorativeSquare, ],
    ]
