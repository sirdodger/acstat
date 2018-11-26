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
