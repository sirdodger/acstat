#!/usr/bin/env python3

"""Missile tile.

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


class MissileTile(Tile):
    """The missile bay launches explosive torpedoes, science probes and boarding craft.

    It must have exterior facing.

    """

    ABBREVIATION: str = 'mi'

    COLOR = colors.RED_BACKGROUND

    DEFINITION: typing.List[typing.List[typing.Type[tiles.ship_square.ShipSquare]]] = [

        [DecorativeSquare, DecorativeSquare, DecorativeSquare, DecorativeSquare, DecorativeSquare, ],
        [DecorativeSquare, DecorativeSquare, DecorativeSquare, DecorativeSquare, DecorativeSquare, ],
        [BlankSquare,      BlankSquare,      BlankSquare,      BlankSquare,      BlankSquare,      ],
        [BlankSquare,      DecorativeSquare, DecorativeSquare, DecorativeSquare, BlankSquare,      ],
        [BlankSquare,      BlankSquare,      ActionSquare,     BlankSquare,      BlankSquare,      ],
    ]

    DOORS: typing.Dict[str, bool] = {
        'n': False,
        's': True,
        'e': True,
        'w': True,
    }

    # The (x, y) coordinates targeted by a die roll.
    TARGETS: typing.Dict[int, typing.Tuple[int, int]] = {
        1: (0, 2, ),
        2: (4, 2, ),
        3: (4, 4, ),
        4: (0, 4, ),
        5: (3, 4, ),
        6: (2, 4, ),
    }
