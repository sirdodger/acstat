#!/usr/bin/env python3

"""Teleporter tile.

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


class TeleporterTile(Tile):
    """The teleporter transports people or bombs to another ship.  It cannot transport to celestial bodies, deep
    space, or the same ship.

    """

    ABBREVIATION: str = 'tp'

    COLOR = colors.GREEN_BACKGROUND

    DEFINITION: typing.List[typing.List[typing.Type[tiles.ship_square.ShipSquare]]] = [
        [MachineSquare, MachineSquare, BlankSquare, MachineSquare, MachineSquare, ],
        [MachineSquare, ActionSquare,  BlankSquare, BlankSquare,   MachineSquare, ],
        [BlankSquare,   BlankSquare,   BlankSquare, BlankSquare,   BlankSquare,   ],
        [MachineSquare, BlankSquare,   BlankSquare, ActionSquare,  MachineSquare, ],
        [MachineSquare, MachineSquare, BlankSquare, MachineSquare, MachineSquare, ],
    ]
