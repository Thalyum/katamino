#!/usr/bin/env python3

from copy import deepcopy

import p_set

Colors = {
    "green": 28,
    "orange": 202,
    "red": 196,
    "cyan": 81,
    "gray": 101,
    "blue": 20,
    "white": 15,
    "pink": 198,
    "purple": 89,
    "beige": 209,
    "l_green": 46,
    "yellow": 226,
    "black": 232,
}


def foreground(color, text):
    return f"\033[38;5;{color}m{text}\033[0;0m"


def background(color, text):
    return f"\033[48;5;{color}m{text}\033[0;0m"


def print_colored_grid(grid):
    print("---")
    for line in grid:
        for p_id in line:
            color = p_set.get_color_by_id(p_id)
            print(background(Colors[color], str(p_id).ljust(3, " ")), end="")
        print("")


def print_attempt(p_geo, coord, grid):
    attempt_grid = deepcopy(grid)
    x = coord[0]
    y = coord[1]
    (height, width) = p_geo.shape
    for i in range(height):
        for j in range(width):
            if p_geo[i, j] != 0:
                attempt_grid[x + i, y + j] = 2
    print_colored_grid(attempt_grid)
    input()
