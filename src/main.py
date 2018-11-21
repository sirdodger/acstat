#!/usr/bin/env python3

"""Simple entry point to drive sample code.

"""

from __future__ import annotations

import curses

import ship
import ships_predefined


def start_main_loop(screen):
    """Run the main draw/wait for keypress loop.

    :param screen: The curses screen.

    """
    curses.noecho()
    curses.cbreak()
    screen.keypad(True)

    k = 0
    cursor_x = 0
    cursor_y = 0

    # Start colors in curses
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, 255):
        curses.init_pair(i + 1, i, -1)

    while k != ord('q'):

        screen.clear()

        if k == ord('p'):
            screen.clear()
            for i in range(0, 255):
                screen.addstr(str(i) + ' ', curses.color_pair(i))

        else:

            height, width = screen.getmaxyx()

            if k == curses.KEY_DOWN:
                cursor_y += 1
            elif k == curses.KEY_UP:
                cursor_y -= 1
            elif k == curses.KEY_RIGHT:
                cursor_x += 1
            elif k == curses.KEY_LEFT:
                cursor_x -= 1

            cursor_x = max(0, cursor_x)
            cursor_x = min(width - 1, cursor_x)

            cursor_y = max(0, cursor_y)
            cursor_y = min(height - 1, cursor_y)

            s = ship.Ship(ships_predefined.chuck_torus_ii, ships_predefined.chuck_torus_ii_rotation)
            s.draw(screen)

            # s2 = ship.Ship(ships_predefined.roach_9, ships_predefined.roach_9_rotation)
            # s2.draw(screen)

        # Refresh the screen
        screen.refresh()

        # Wait for next input
        k = screen.getch()

    curses.nocbreak()
    screen.keypad(False)
    curses.echo()


if __name__ == '__main__':
    curses.initscr()
    curses.wrapper(start_main_loop)
