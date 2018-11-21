#!/usr/bin/env python3

"""General utilities.

"""

# noinspection Mypy
import numpy
import typing


def rotate_2d_array(array: typing.List[typing.List[typing.Any]], rotation: int) -> typing.List[typing.List[typing.Any]]:
    """Rotate the array clockwise a certain number of times.

    """
    rotation %= 4
    return [x for x in numpy.rot90(array, k=rotation, axes=(1, 0)).tolist()]


def subclasses(klass):
    """Retrieve all subclasses to to add to a global map.

    :param klass: The base class.

    :return: A set of subclasses.

    """
    return set(klass.__subclasses__()).union([s for c in klass.__subclasses__() for s in subclasses(c)])
