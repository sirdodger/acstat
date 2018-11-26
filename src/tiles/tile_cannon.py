#!/usr/bin/env python3

"""Cannon tile.

"""

from __future__ import annotations

import colors
import typing

import tiles.ship_square
from tiles.ship_square import (
    ActionSquare,
    BlankSquare,
    DecorativeSquare,
)
from .tile import Tile


class CannonTile(Tile):
    """The cannon can fire in any direction in which it has unobstructed line of sight.  It can be configured in salvo,
    sniper or flak modes.

    Salvo mode deals high damage against targets.  Sniper mode sacrifices half damage for double range.  Flak mode
    deals minimal damage, but fires rapidly.

    """

    ABBREVIATION: str = 'ca'

    COLOR: int = colors.RED_BACKGROUND

    DEFINITION: typing.List[typing.List[typing.Type[tiles.ship_square.ShipSquare]]] = [
        [BlankSquare, BlankSquare,      DecorativeSquare, BlankSquare,      BlankSquare, ],
        [BlankSquare, BlankSquare,      DecorativeSquare, BlankSquare,      BlankSquare, ],
        [BlankSquare, DecorativeSquare, DecorativeSquare, DecorativeSquare, BlankSquare, ],
        [BlankSquare, DecorativeSquare, ActionSquare,     DecorativeSquare, BlankSquare, ],
        [BlankSquare, BlankSquare,      BlankSquare,      BlankSquare,      BlankSquare, ],
    ]

    # Top, right, bottom, left
    DOORS: typing.List[bool] = [False, True, True, True]
