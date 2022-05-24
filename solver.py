#!/usr/bin/env python3

# This game requires the player to fill a 11x5 grid with predefined geometric
# pieces
# Each piece will fit in a 4x4 square (meaning will be at most 4-unit wide
# and/or 4-unit tall)
# Each piece will be at least 1-unit wide or tall

import numpy as np

import color
import p_set

GRID_WIDTH = 11
GRID_HEIGHT = 5
GRID_MARGIN = p_set.P_MAX_SIZE - p_set.P_MIN_SIZE
grid = np.ones((GRID_HEIGHT, GRID_WIDTH), int) * 0
# as each piece is at least 1-unit wide, we can add 3 lines and 3 columns that
# we can mark is 'filled' by some piece, to easy the checking of the piece
# placement (instead of doing some intricate computation over the array
# dimensions, indexes and content). As we align the piece in the top-left corner
# of our 'piece-matrix', we can have some issues with the far right and bottom
# checking.
columns_to_be_added = np.ones((GRID_HEIGHT, GRID_MARGIN), int) * 255
grid = np.column_stack((grid, columns_to_be_added))
rows_to_be_added = np.ones((GRID_MARGIN, GRID_WIDTH + GRID_MARGIN), int) * 255
grid = np.row_stack((grid, rows_to_be_added))

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
        # remember the piece we just put
        placed_set.append(piece)
    else:
        # reset the piece try counter and position
        piece["tried"] = 0
        piece["coord"] = (0, -1)
        remaining_set.append(piece)
        # and go back to the previous state
        if placed_set:
            previous_piece = placed_set.pop()
            p_set.remove_piece_from_grid(previous_piece, grid)
            remaining_set.append(previous_piece)

color.print_colored_grid(grid)
