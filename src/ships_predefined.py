#!/usr/bin/env python3

"""Predefined layouts for ships.

"""

import typing


chuck_torus_ii: typing.List[typing.List[typing.Optional[str]]] = [
    [None, 'hy', None, ],
    ['hl', 'sc', 'ca', ],
    ['en', None, 'ca', ],
    ['en', 'en', 'ls', ],
]

chuck_torus_ii_rotation: typing.List[typing.List[int]] = [
    [0, 0, 0, ],
    [0, 1, 0, ],
    [1, 0, 1, ],
    [0, 0, 0, ],

]

roach_9: typing.List[typing.List[typing.Optional[str]]] = [
    [None, 'ca', 'hl', 'ca', None, ],
    ['mi', 'ls', 'cr', 'ls', 'mi', ],
    ['mi', 'ls', 'hy', 'ls', 'mi', ],
    [None, 'sc', 'tp', 'tr', None, ],
    ['en', 'en', 'en', 'en', 'ca', ],
]

roach_9_rotation: typing.List[typing.List[int]] = [
    [0, 0, 0, 0, 0, ],
    [3, 0, 0, 0, 1, ],
    [3, 0, 0, 0, 1, ],
    [0, 2, 0, 1, 0, ],
    [0, 0, 0, 0, 1, ],
]
