#!/usr/bin/env python3

"""Mine layer tile.

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


class MineLayerTile(Tile):
    """Mine layers launch mines into empty space hexes.

    It must have exterior facing.
    """

    ABBREVIATION: str = 'ml'

    COLOR = colors.BLUE_BACKGROUND

    DEFINITION: typing.List[typing.List[typing.Type[tiles.ship_square.ShipSquare]]] = [
        [MachineSquare, BlankSquare,   BlankSquare,   BlankSquare,   BlankSquare,   ],
        [MachineSquare, MachineSquare, MachineSquare, MachineSquare, BlankSquare,   ],
        [MachineSquare, MachineSquare, MachineSquare, MachineSquare, BlankSquare,   ],
        [MachineSquare, ActionSquare,  BlankSquare,   BlankSquare,   BlankSquare,   ],
        [MachineSquare, MachineSquare, BlankSquare,   BlankSquare,   MachineSquare, ],
    ]

    # Top, right, bottom, left
    DOORS: typing.List[bool] = [True, True, True, False]
