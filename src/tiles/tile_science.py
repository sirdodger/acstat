#!/usr/bin/env python3

"""Science bay tile.

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


class ScienceTile(Tile):
    """The science bay shields the ship, collects mission data, broadcasts missile countermeasures, acquires targeting
    locks on enemy vessels, scans nearby space hexes, and answers yes/no questions about the area.

    It is required on all ships.

    """

    ABBREVIATION: str = 'sc'

    COLOR = colors.GREEN_BACKGROUND

    DEFINITION: typing.List[typing.List[typing.Type[tiles.ship_square.ShipSquare]]] = [
        [BlankSquare, BlankSquare,   BlankSquare,   MachineSquare, MachineSquare, ],
        [BlankSquare, MachineSquare, BlankSquare,   ActionSquare,  MachineSquare, ],
        [BlankSquare, MachineSquare, MachineSquare, MachineSquare, MachineSquare, ],
        [BlankSquare, MachineSquare, BlankSquare,   ActionSquare,  MachineSquare, ],
        [BlankSquare, BlankSquare,   BlankSquare,   MachineSquare, MachineSquare, ],
    ]

    # Top, right, bottom, left
    DOORS: typing.List[bool] = [True, False, True, True]
