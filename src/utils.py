#!/usr/bin/env python3


"""General utilities.

"""


def subclasses(cls):
    """Retrieve all subclasses to to add to a global map.

    :param cls: The base class.

    :return: A set of subclasses.

    """
    return set(cls.__subclasses__()).union([s for c in cls.__subclasses__() for s in subclasses(c)])
