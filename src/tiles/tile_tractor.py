#!/usr/bin/env python3

"""Engine tiles provide power to ship systems.

"""

from __future__ import annotations

import typing

import colors
import tiles.ship_square
from .ship_square import (
    ActionSquare,
    BlankSquare,
    DecorativeSquare,
    TractorSquare,
)
from .tile import Tile


class TractorTile(Tile):
    """Tractor modules pull and capture objects.

    """

    ABBREVIATION: str = 'tr'

    COLOR = colors.BLUE_BACKGROUND

    DEFINITION: typing.List[typing.List[typing.Type[tiles.ship_square.ShipSquare]]] = [
        [BlankSquare,      DecorativeSquare, TractorSquare,    DecorativeSquare, BlankSquare,      ],
        [BlankSquare,      DecorativeSquare, BlankSquare,      DecorativeSquare, BlankSquare,      ],
        [BlankSquare,      DecorativeSquare, ActionSquare,     DecorativeSquare, BlankSquare,      ],
        [BlankSquare,      DecorativeSquare, BlankSquare,      DecorativeSquare, BlankSquare,      ],
        [BlankSquare,      BlankSquare,      BlankSquare,      BlankSquare,      BlankSquare,      ],
    ]

    # Top, right, bottom, left
    DOORS: typing.List[bool] = [False, True, True, True]
