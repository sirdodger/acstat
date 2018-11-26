#!/usr/bin/env python3

"""Cloaking device tile.

"""

from __future__ import annotations

import typing

import colors
import tiles.ship_square
from .ship_square import (
    ActionSquare,
    BlankSquare,
    MachineSquare,
)
from .tile import Tile


class CloakingTile(Tile):
    """The cloaking tile makes it harder to detect a ship.
    """

    ABBREVIATION: str = 'cl'

    COLOR = colors.GREEN_BACKGROUND

    DEFINITION: typing.List[typing.List[typing.Type[tiles.ship_square.ShipSquare]]] = [
        [MachineSquare, MachineSquare, MachineSquare, MachineSquare, MachineSquare, ],
        [MachineSquare, MachineSquare, ActionSquare,  BlankSquare,   MachineSquare, ],
        [BlankSquare,   MachineSquare, BlankSquare,   BlankSquare,   BlankSquare,   ],
        [BlankSquare,   MachineSquare, MachineSquare, BlankSquare,   MachineSquare, ],
        [BlankSquare,   BlankSquare,   BlankSquare,   BlankSquare,   MachineSquare, ],
    ]

    # Top, right, bottom, left
    DOORS: typing.List[bool] = [False, True, True, True]
