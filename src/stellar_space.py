#!/usr/bin/env python3

"""The known hex space for a stellar system (or other mission scenario area).

"Space is big. Really big. You just won't believe how vastly, hugely, mind-bogglingly big it is. I mean, you may
think it's a long way down the road to the chemist, but that's just peanuts to space."  - Douglas Adams

The corollary to space being big is that it is sparsely populated.  Rather than storing an entire map of space, store
a list of objects in space and their position.  When it comes time to render the viewport of what is visible, check
items to see if they are in range.

"""

import collections
import typing

import hex_utils


class StellarObject:
    """A single object on the hex map, represented in cubic coordinates.

    """

    # Bidirectional lookups of stellar objects <--> positions.  Note that more than one stellar object can be in a hex,
    # and in rare cases, a stellar object can encompass more than one hex.
    hex_to_instance: typing.Dict[hex_utils.Hex, typing.Set['StellarObject']] = {}
    instance_to_hex: typing.Dict['StellarObject', typing.Set[hex_utils.Hex]] = {}

    def __init__(self, instance, symbol):
        """Associate an object with a location.

        :param instance: The object on the map.

        :param symbol: The map symbol.

        """
        self.instance = instance
        self._hex = set()
        self._symbol = symbol

    @property
    def hex(self) -> typing.Set[hex_utils.Hex]:
        """Get the hex position of the object.

        :return: The Hex coordinates.

        """
        return self._hex

    @hex.setter
    def hex(self, position: typing.Union[hex_utils.Hex, typing.Iterable[hex_utils.Hex]]) -> None:
        """Set the hex position of the object and update the global position dictionaries.

        :param position: The new hex of the object, or a list of hexes the object occupies.

        """
        position = {position} if not isinstance(position, collections.Iterable) else set(position)

        for h in self._hex:
            self.hex_to_instance[h].remove(self)
            self.instance_to_hex[self].remove(h)

        for h in position:
            self.hex_to_instance[h].add(self)
            self.instance_to_hex[self].add(h)

        self._hex = position


class StellarView:
    """A viewport into space.  Currently the map is squarish, should it have a center and radius?

    """

    def __init__(self, center: hex_utils.Hex, radius: int):
        """Create a new viewport of variable size.

        :param center:  The center of the view.
        :param radius: The distance in hexes from the center to the edge.

        """
        self._center: hex_utils.Hex = center
        self._radius: int = radius

    def items(self) -> typing.Iterable[typing.Tuple[hex_utils.Hex, StellarObject]]:
        """Get all items present in the view.

        TODO: Make the items yield in map iteration order.

        :return: Iterator of positions and stellar objects.

        """
        for position, things in StellarObject.hex_to_instance.items():
            if self._center.distance(position) <= self._radius:
                for thing in things:
                    yield position, thing
