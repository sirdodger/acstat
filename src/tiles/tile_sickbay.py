#!/usr/bin/env python3

"""Sick bay tile.

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


class SickBayTile(Tile):
    """The sick bay diagnoses diseases and heals injured or dying characters.

    """

    ABBREVIATION: str = 'sc'

    COLOR = colors.GREEN_BACKGROUND

    DEFINITION: typing.List[typing.List[typing.Type[tiles.ship_square.ShipSquare]]] = [
        [MachineSquare, BlankSquare,   BlankSquare,   BlankSquare,   MachineSquare, ],
        [BlankSquare,   ActionSquare,  MachineSquare, BlankSquare,   BlankSquare,   ],
        [BlankSquare,   MachineSquare, MachineSquare, MachineSquare, BlankSquare,   ],
        [BlankSquare,   BlankSquare,   MachineSquare, ActionSquare,  BlankSquare,   ],
        [MachineSquare, BlankSquare,   BlankSquare,   BlankSquare,   MachineSquare, ],
    ]

    # Top, right, bottom, left
    DOORS: typing.List[bool] = [True, True, True, True]
