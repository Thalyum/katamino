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

# prepare the grid n°65
for i in range(5):
    for j in range(2):
        grid[i, j] = 42
grid[2, 2] = 42
grid[2, 3] = 42
remaining_set.remove(p_set.white_p)
remaining_set.remove(p_set.orange_p)
remaining_set.remove(p_set.blue_p)

# compute the size of each piece we have to place,
# and keep the smaller one
min_size = None
for piece in remaining_set:
    piece_sz = np.sum(piece["geo"][0])
    piece["size"] = piece_sz
    if not min_size or piece_sz < min_size:
        min_size = piece_sz

color.print_colored_grid(grid)

placed_set = []
while remaining_set:
    piece = remaining_set.pop()
    if p_set.check_piece(piece, grid):
        # color.print_colored_grid(grid)
        # update min_size if needed (i.e. if we just placed the smaller piece)
        if piece["size"] == min_size and remaining_set:
            min_size = min([p["size"] for p in remaining_set])
        places_left = p_set.nb_holes_in_grid(grid, min_size)
        if places_left == p_set.ERR_TOO_SMALL or places_left > len(remaining_set):
            p_set.remove_piece_from_grid(piece, grid)
            # put the piece back into the list
            remaining_set.append(piece)
            # update min_size as we put the piece back in the list
            min_size = min(min_size, piece["size"])
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
