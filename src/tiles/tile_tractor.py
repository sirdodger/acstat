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

    DOORS: typing.Dict[str, bool] = {
        'n': False,
        's': True,
        'e': True,
        'w': True,
    }

    # The (x, y) coordinates targeted by a die roll.
    TARGETS: typing.Dict[int, typing.Tuple[int, int]] = {
        1: (0, 1, ),
        2: (4, 0, ),
        3: (2, 1, ),
        4: (4, 4, ),
        5: (4, 2, ),
        6: (2, 2, ),
    }
