#!/usr/bin/env python3

"""Life support tile.

"""

from __future__ import annotations

import typing

import colors
import tiles.ship_square
from .ship_square import (
    BlankSquare,
    MachineSquare,
)
from .tile import Tile


class LifeSupportTile(Tile):
    """Life support can handle four crew members, five if upgraded.  It can temporarily support many more passengers,
    but extended overuse results in severe health consequences.

    """

    ABBREVIATION: str = 'ls'

    COLOR = colors.WHITE

    DEFINITION: typing.List[typing.List[typing.Type[tiles.ship_square.ShipSquare]]] = [
        [MachineSquare, MachineSquare, BlankSquare, MachineSquare, MachineSquare, ],
        [MachineSquare, MachineSquare, BlankSquare, MachineSquare, MachineSquare, ],
        [BlankSquare,   BlankSquare,   BlankSquare, BlankSquare,   BlankSquare,   ],
        [MachineSquare, MachineSquare, BlankSquare, MachineSquare, MachineSquare, ],
        [MachineSquare, MachineSquare, BlankSquare, MachineSquare, MachineSquare, ],
    ]
