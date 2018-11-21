#!/usr/bin/env python3

"""Engine tile.

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


class EngineTile(Tile):
    """Engines provide power for ship systems.

    It is required on all ships and must have exterior, aft facing.
    """

    ABBREVIATION: str = 'en'

    COLOR = colors.BLUE_BACKGROUND

    DEFINITION: typing.List[typing.List[typing.Type[tiles.ship_square.ShipSquare]]] = [
        [BlankSquare,      BlankSquare,      BlankSquare,      BlankSquare,      BlankSquare,      ],
        [BlankSquare,      DecorativeSquare, DecorativeSquare, DecorativeSquare, BlankSquare,      ],
        [BlankSquare,      DecorativeSquare, DecorativeSquare, DecorativeSquare, BlankSquare,      ],
        [BlankSquare,      ActionSquare,     DecorativeSquare, ActionSquare,     BlankSquare,      ],
        [DecorativeSquare, DecorativeSquare, DecorativeSquare, DecorativeSquare, DecorativeSquare, ],
    ]

    # Top, right, bottom, left
    DOORS: typing.List[bool] = [True, True, False, True]

    # The (x, y) coordinates targeted by a die roll.
    TARGETS: typing.Dict[int, typing.Tuple[int, int]] = {
        1: (3, 0, ),
        2: (0, 1, ),
        3: (4, 2, ),
        4: (4, 0, ),
        5: (4, 3, ),
        6: (1, 3, ),
    }
