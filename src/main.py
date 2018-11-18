#!/usr/bin/env python3

"""Simple entry point to drive sample code.

"""

import curses

import ship


def start_main_loop(screen):
    curses.noecho()
    curses.cbreak()
    screen.keypad(True)

    k = 0
    cursor_x = 0
    cursor_y = 0

    # Clear and refresh the screen for a blank canvas
    screen.clear()
    screen.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    while k != ord('q'):
        # Initialization
        screen.clear()
        height, width = screen.getmaxyx()

        if k == curses.KEY_DOWN:
            cursor_y = cursor_y + 1
        elif k == curses.KEY_UP:
            cursor_y = cursor_y - 1
        elif k == curses.KEY_RIGHT:
            cursor_x = cursor_x + 1
        elif k == curses.KEY_LEFT:
            cursor_x = cursor_x - 1

        cursor_x = max(0, cursor_x)
        cursor_x = min(width - 1, cursor_x)

        cursor_y = max(0, cursor_y)
        cursor_y = min(height - 1, cursor_y)

        s = ship.Ship([
            [None, 'cr', None, ],
            ['cr', 'cr', 'cr', ],
            [None, 'cr', None, ],
        ])
        s.render(screen)

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
