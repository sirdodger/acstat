#!/usr/bin/env python3

"""The known hex space for a stellar system (or other mission scenario area).

"Space is big. Really big. You just won't believe how vastly, hugely, mind-bogglingly big it is. I mean, you may
think it's a long way down the road to the chemist, but that's just peanuts to space."  - Douglas Adams

The corollary to space being big is that it is sparsely populated.  Rather than storing an entire map of space, store
a list of objects in space and their position.  When it comes time to render the viewport of what is visible, check
items to see if they are in range.

"""

import typing

import hex_utils


class StellarObject(object):
    """A single object on the hex map, represented in cubic coordinates.

    """


class StellarSpace(object):
    """Store the coordinates for all objects in system.

    """

    coordinates_to_objects: typing.Dict[hex_utils.Hex, StellarObject] = {}

