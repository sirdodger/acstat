#!/usr/bin/env python3

"""Tiles that comprise a ship.

"""

import utils

from .tile import Tile
from .tile_cannon import CannonTile
from .tile_cargo import CargoTile
from .tile_engine import EngineTile
from .tile_helm import HelmTile
from .tile_hyperdrive import HyperdriveTile
from .tile_lifesupport import LifeSupportTile
from .tile_missile import MissileTile
from .tile_science import ScienceTile
from .tile_teleporter import TeleporterTile
from .tile_tractor import TractorTile


TILES = {t.ABBREVIATION: t for t in utils.subclasses(Tile)}
