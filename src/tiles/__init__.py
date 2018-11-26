#!/usr/bin/env python3

"""Tiles that comprise a ship.

"""

import utils

from .tile import Tile
from .tile_cannon import CannonTile
from .tile_cargo import CargoTile
from .tile_cloak import CloakingTile
from .tile_engine import EngineTile
from .tile_helm import HelmTile
from .tile_hyperdrive import HyperdriveTile
from .tile_lifesupport import LifeSupportTile
from .tile_minelayer import MineLayerTile
from .tile_missile import MissileTile
from .tile_science import ScienceTile
from .tile_sickbay import SickBayTile
from .tile_teleporter import TeleporterTile


TILES = {t.ABBREVIATION: t for t in utils.subclasses(Tile)}
