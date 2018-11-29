#!/usr/bin/env python3

"""Cargo tile.

"Thirty spokes converge upon a single hub
 It is the hole in the centre that the purpose of the axle depends.
 We make a vessel from a lump of clay
 It is the empty space within the vessel that makes it useful.
 We make doors and windows for a room.
 But it is the those empty spaces that make the room habitable.
 Thus while the tangible has advantages
 It is the intangible that makes it useful."
   - Laozi / Steven Groak

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
