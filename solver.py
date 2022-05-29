#!/usr/bin/env python3

# This game requires the player to fill a 11x5 grid with predefined geometric
# pieces

import sys

import numpy as np

import color
import p_set

GRID_WIDTH = 11
GRID_HEIGHT = 5
grid = np.ones((GRID_HEIGHT, GRID_WIDTH), int) * 0

remaining_set = [
    p_set.green_p,
    p_set.orange_p,
    p_set.red_p,
    p_set.cyan_p,
    p_set.gray_p,
    p_set.blue_p,
    p_set.white_p,
    p_set.pink_p,
    p_set.purple_p,
    p_set.beige_p,
    p_set.light_green_p,
    p_set.yellow_p,
]

# prepare the grid n°62
for i in range(5):
    for j in range(3):
        grid[i, j] = 42
grid[0, 3] = 42
grid[0, 4] = 42
grid[0, 5] = 42
grid[1, 3] = 42
grid[1, 4] = 42
remaining_set.remove(p_set.gray_p)
remaining_set.remove(p_set.green_p)
remaining_set.remove(p_set.blue_p)
remaining_set.remove(p_set.yellow_p)

color.print_colored_grid(grid)

placed_set = []
while remaining_set:
    piece = remaining_set.pop()
    if p_set.check_piece(piece, grid):
        # color.print_colored_grid(grid)
        places_left = p_set.nb_holes_in_grid(grid)
        if places_left > len(remaining_set):
            p_set.remove_piece_from_grid(piece, grid)
            # put the piece back into the list
            remaining_set.append(piece)
        else:
            # remember the piece we just put
            placed_set.append(piece)
    else:
        # reset the piece try counter and position
        piece["tried"] = 0
        piece["coord"] = (0, -1)
        # put the piece into the list
        remaining_set.append(piece)
        # go back to the previous state
        if placed_set:
            previous_piece = placed_set.pop()
            p_set.remove_piece_from_grid(previous_piece, grid)
            remaining_set.append(previous_piece)
        else:
            sys.exit("Puzzle cannot be solved")

color.print_colored_grid(grid)
