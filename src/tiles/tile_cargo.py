#!/usr/bin/env python3

from __future__ import annotations

from .tile import Tile


class CargoTile(Tile):
    """Stores supplemental mission equipment.

    """

    ABBREVIATION = 'cr'

    # Top, right, bottom, left
    DOORS = {
        'n': True,
        's': True,
        'e': True,
        'w': True,
    }
