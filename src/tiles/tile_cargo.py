#!/usr/bin/env python3

"""Cargo tile.

"""

from __future__ import annotations

import typing

import colors

import tiles.ship_square
from .ship_square import BlankSquare
from .tile import Tile


class CargoTile(Tile):
    """Cargo bays store three pieces of 2x2 mission equipment, four if upgraded.

    """

    ABBREVIATION: str = 'cr'

    COLOR: int = colors.WHITE

    DEFINITION: typing.List[typing.List[typing.Type[tiles.ship_square.ShipSquare]]] = [
        [BlankSquare, BlankSquare, BlankSquare, BlankSquare, BlankSquare, ],
        [BlankSquare, BlankSquare, BlankSquare, BlankSquare, BlankSquare, ],
        [BlankSquare, BlankSquare, BlankSquare, BlankSquare, BlankSquare, ],
        [BlankSquare, BlankSquare, BlankSquare, BlankSquare, BlankSquare, ],
        [BlankSquare, BlankSquare, BlankSquare, BlankSquare, BlankSquare, ],
    ]

    DOORS: typing.Dict[str, bool] = {
        'n': True,
        's': True,
        'e': True,
        'w': True,
    }

    # The (x, y) coordinates targeted by a die roll.
    TARGETS: typing.Dict[int, typing.Tuple[int, int]] = {
        1: (0, 2, ),
        2: (1, 4, ),
        3: (1, 0, ),
        4: (0, 4, ),
        5: (3, 4, ),
    }
