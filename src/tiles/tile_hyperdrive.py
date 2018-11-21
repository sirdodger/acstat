#!/usr/bin/env python3

"""Hyperdrive tile.

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


class HyperdriveTile(Tile):
    """The hyperdrive warps the ship in and out of missions.  The hyperdrive cannot warp the ship within 12 hexes of
    a celestial body, and passing within that radius clears all programming from the hyperdrive.

    It is required on all ships.

    """

    ABBREVIATION: str = 'hy'

    COLOR = colors.GREEN_BACKGROUND

    DEFINITION: typing.List[typing.List[typing.Type[tiles.ship_square.ShipSquare]]] = [
        [BlankSquare,      BlankSquare,      BlankSquare,      BlankSquare,      BlankSquare,      ],
        [BlankSquare,      DecorativeSquare, DecorativeSquare, DecorativeSquare, BlankSquare,      ],
        [BlankSquare,      DecorativeSquare, ActionSquare,     DecorativeSquare, BlankSquare,      ],
        [BlankSquare,      DecorativeSquare, BlankSquare,      DecorativeSquare, BlankSquare,      ],
        [BlankSquare,      BlankSquare,      BlankSquare,      BlankSquare,      BlankSquare,      ],
    ]

    # The (x, y) coordinates targeted by a die roll.
    TARGETS: typing.Dict[int, typing.Tuple[int, int]] = {
        1: (4, 3, ),
        2: (3, 0, ),
        3: (2, 4, ),
        4: (0, 0, ),
        5: (0, 2, ),
        6: (2, 2, ),
    }
