
from .tile import Tile
from .tile_cargo import CargoTile


def tile_subclasses(cls):
    return set(cls.__subclasses__()).union([s for c in cls.__subclasses__() for s in tile_subclasses(c)])


TILES = {t.ABBREVIATION: t for t in tile_subclasses(Tile)}
