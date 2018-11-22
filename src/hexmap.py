#!/usr/bin/env python3

"""An even-r hex map.

"""

import typing


class HexMap(object):
    """A map of explorable space.

    """
    # The size of a single "hex".  Must be odd.
    _SPACE_HEIGHT: int = 3
    _SPACE_WIDTH: int = 3

    # Offset the short hex rows by half the width of a hex.
    _OFFSET_SHORT_ROW: int = int((_SPACE_WIDTH + 1) / 2)

    # Shift the map by three spaces to allow room for the axes' labels.
    _OFFSET_AXES_LABEL: int = 3

    _SYMBOLS: typing.Dict[str, str] = {
        'blank': ' ' * _SPACE_WIDTH,

        'full': '─' * _SPACE_WIDTH,
        'half': '─' * int((_SPACE_WIDTH - 1) / 2),

        'up_t': '┴',
        'down_t': '┬',

        'dr': '┌',
        'dl': '┐',

        'ur': '└',
        'ul': '┘',

        'v': '│',
    }

    def __init__(self, horizontal_count: int, vertical_count: int) -> None:
        """Initialize a hex map of a given size.

        Pre-render the strings for drawing the hexes, so they do not need to be computed in the inner draw loop.  It
        would be faster still to replace and then horizontally expand the string, but it is easier to read and debug
        if the template string is fully formed.  Performance impact is negligible, since it is only done once per
        hex map, not per draw.

        :param horizontal_count: The number of hex columns on a long row.  (A short row will have one less column.)

        :param vertical_count: The number of vertical hex rows.  The hex map always starts and ends on a short row, so
            even numbers will have an extra row automatically added.

        """

        if horizontal_count < 2:
            raise ValueError('Must build hex grid with at least two horizontal hexes')
        if vertical_count < 3:
            raise ValueError('Must build hex grid with at least three vertical rows')

        self.horizontal_count: int = horizontal_count
        self.vertical_count: int = vertical_count

        # The top and bottom caps are on a short row.
        remaining_long_row_count = self.horizontal_count - 1
        remaining_short_row_count = self.horizontal_count - 2

        # First (short) row, has no up_t since there is nothing above it.
        top_template = '{dr}' + '{full}{down_t}' * remaining_short_row_count + '{full}{dl}'
        self.top: str = top_template.format(**self._SYMBOLS)

        # The middle rows always have long horizontals.  The middle top row is followed by a long vertical row, and
        # the middle bottom row is followed by a short vertical row.
        middle_top_loop = '{half}{up_t}{half}{down_t}'
        middle_top_template = '{dr}' + middle_top_loop * remaining_long_row_count + '{half}{up_t}{half}{dl}'
        self.middle_top: str = middle_top_template.format(**self._SYMBOLS)

        middle_bottom_loop = '{half}{down_t}{half}{up_t}'
        middle_bottom_template = '{ur}' + middle_bottom_loop * remaining_long_row_count + '{half}{down_t}{half}{ul}'
        self.middle_bottom: str = middle_bottom_template.format(**self._SYMBOLS)

        # Last (short) row, has no down_t since there is nothing below it.
        bottom_template = '{ur}' + '{full}{up_t}' * remaining_short_row_count + '{full}{ul}'
        self.bottom: str = bottom_template.format(**self._SYMBOLS)

        # Vertical rows, both short and long hex row variants.
        self.short_vertical: str = ('{v}' + ('{blank}{v}' * remaining_long_row_count)).format(**self._SYMBOLS)
        self.long_vertical: str = self.short_vertical + '{blank}{v}'.format(**self._SYMBOLS)

    def draw(self, screen: typing.Any, offset_x: int, offset_y: int) -> None:
        """Draw the hex grid outline.  Note that any cell contents are erased and must be redrawn.

        :param screen: The curses window.
        :type screen: The curses window as returned from curses.initscr() et al.

        :param offset_x: The x offset at which to start drawing the ship.  Note that the first, last, and every other
            intermediate row are all shifted right slightly to make a hex grid instead of a square grid.

        :param offset_y: The y offset at which to start drawing the ship.  The variable is updated as each line is
            drawn to provide a running reference where the next line should be drawn.

        """

        # Shift all calculations down and right to make room for labels.
        offset_x += self._OFFSET_AXES_LABEL
        offset_y += self._OFFSET_AXES_LABEL

        # Draw the top line right shifted by two characters since the top hex row is offset and short.
        screen.addstr(offset_y, offset_x + self._OFFSET_SHORT_ROW, self.top)

        # The next three lines are the vertical sides for the first row, also shifted right two characters.
        for offset_y in range(offset_y + 1, offset_y + self._SPACE_HEIGHT + 1):
            screen.addstr(offset_y, offset_x + self._OFFSET_SHORT_ROW, self.short_vertical)

        vertical_rows_drawn = 1

        # Loop through the middle section two hex rows at a time, long->short->long->short->etc.  Always end on a short
        # row, even if that means an extra row is printed.  It just makes the map look nicer.
        while vertical_rows_drawn < self.vertical_count:
            offset_y += 1
            screen.addstr(offset_y, offset_x, self.middle_top)
            for offset_y in range(offset_y + 1, offset_y + self._SPACE_HEIGHT + 1):
                screen.addstr(offset_y, offset_x, self.long_vertical)

            offset_y += 1
            screen.addstr(offset_y, offset_x, self.middle_bottom)

            # The next three lines are the vertical sides for the short row, shifted right two characters.
            for offset_y in range(offset_y + 1, offset_y + self._SPACE_HEIGHT + 1):
                screen.addstr(offset_y, offset_x + self._OFFSET_SHORT_ROW, self.short_vertical)

            vertical_rows_drawn += 2

        # The bottom line.
        offset_y += 1
        screen.addstr(offset_y, offset_x + self._OFFSET_SHORT_ROW, self.bottom)
