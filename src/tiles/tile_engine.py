#!/usr/bin/env python3

"""Engine tile.

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


class EngineTile(Tile):
    """Engines provide power for ship systems.

    It is required on all ships and must have exterior, aft facing.
    """

    ABBREVIATION: str = 'en'

    COLOR = colors.BLUE_BACKGROUND

    DEFINITION: typing.List[typing.List[typing.Type[tiles.ship_square.ShipSquare]]] = [
        [BlankSquare,   BlankSquare,   BlankSquare,   BlankSquare,   BlankSquare,   ],
        [BlankSquare,   MachineSquare, MachineSquare, MachineSquare, BlankSquare,   ],
        [BlankSquare,   MachineSquare, MachineSquare, MachineSquare, BlankSquare,   ],
        [BlankSquare,   ActionSquare,  MachineSquare, ActionSquare,  BlankSquare,   ],
        [MachineSquare, MachineSquare, MachineSquare, MachineSquare, MachineSquare, ],
    ]

    # Top, right, bottom, left
    DOORS: typing.List[bool] = [True, True, False, True]
