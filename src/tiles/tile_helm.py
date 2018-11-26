#!/usr/bin/env python3

"""Helm tile.

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


class HelmTile(Tile):
    """The helm steers and stabilizes the ship. It must have a forward facing, except for Tentacle ships.

    It is required on all ships.

    """

    ABBREVIATION: str = 'hl'

    COLOR = colors.YELLOW_BACKGROUND

    DEFINITION: typing.List[typing.List[typing.Type[tiles.ship_square.ShipSquare]]] = [
        [DecorativeSquare, DecorativeSquare, DecorativeSquare, DecorativeSquare, DecorativeSquare, ],
        [DecorativeSquare, BlankSquare,      ActionSquare,     BlankSquare,      DecorativeSquare, ],
        [BlankSquare,      BlankSquare,      BlankSquare,      BlankSquare,      BlankSquare,      ],
        [DecorativeSquare, ActionSquare,     BlankSquare,      ActionSquare,     DecorativeSquare, ],
        [DecorativeSquare, DecorativeSquare, BlankSquare,      DecorativeSquare, DecorativeSquare, ],
    ]

    # Top, right, bottom, left
    DOORS: typing.List[bool] = [False, True, True, True]
