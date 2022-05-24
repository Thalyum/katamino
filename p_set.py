#!/usr/bin/env python3

# Each piece will fit in a 4x4 square (meaning will be at most 4-unit wide
# and/or 4-unit tall)
# Each piece will be at least 1-unit wide or tall

import numpy as np

P_MAX_SIZE = 4
P_MIN_SIZE = 1


def generate_rotation_set(piece_geo):
    """From one basic piece, generate all the possible position of the piece:

    (4 rotation + rotation of the symmetric). Omit any repetitive pattern
    """
    rot_set = []
    p = piece_geo
    rot_set.append(p)
    for i in range(3):
        p = np.rot90(p)
        # align piece with 'top'
        while not p[0, :].any():
            p = np.roll(p, (-1, 0), axis=(0, 1))
        # align piece with 'left'
        while not p[:, 0].any():
            p = np.roll(p, (0, -1), axis=(0, 1))
        if not np.any([np.array_equal(p, x) for x in rot_set]):
            rot_set.append(p)
    p = piece_geo.T
    if not np.any([np.array_equal(p, x) for x in rot_set]):
        rot_set.append(p)
    for i in range(3):
        p = np.rot90(p)
        # align piece with 'top'
        while not p[0, :].any():
            p = np.roll(p, (-1, 0), axis=(0, 1))
        # align piece with 'left'
        while not p[:, 0].any():
            p = np.roll(p, (0, -1), axis=(0, 1))
        if not np.any([np.array_equal(p, x) for x in rot_set]):
            rot_set.append(p)
    return rot_set


green_p = {
    "id": 1,
    "geo": generate_rotation_set(
        np.array([[1, 1, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]])
    ),
    "color": "green",
    "tried": 0,
    "coord": (0, -1),
}
orange_p = {
    "id": 2,
    "geo": generate_rotation_set(
        np.array([[1, 1, 1, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    ),
    "color": "orange",
    "tried": 0,
    "coord": (0, -1),
}
red_p = {
    "id": 3,
    "geo": generate_rotation_set(
        np.array([[1, 1, 1, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    ),
    "color": "red",
    "tried": 0,
    "coord": (0, -1),
}
cyan_p = {
    "id": 4,
    "geo": generate_rotation_set(
        np.array([[1, 1, 1, 0], [1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]])
    ),
    "color": "cyan",
    "tried": 0,
    "coord": (0, -1),
}
gray_p = {
    "id": 5,
    "geo": generate_rotation_set(
        np.array([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]])
    ),
    "color": "gray",
    "tried": 0,
    "coord": (0, -1),
}
blue_p = {
    "id": 6,
    "geo": generate_rotation_set(
        np.array([[1, 1, 1, 1], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    ),
    "color": "blue",
    "tried": 0,
    "coord": (0, -1),
}
white_p = {
    "id": 7,
    "geo": generate_rotation_set(
        np.array([[1, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    ),
    "color": "white",
    "tried": 0,
    "coord": (0, -1),
}
pink_p = {
    "id": 8,
    "geo": generate_rotation_set(
        np.array([[0, 1, 1, 0], [1, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]])
    ),
    "color": "pink",
    "tried": 0,
    "coord": (0, -1),
}
purple_p = {
    "id": 9,
    "geo": generate_rotation_set(
        np.array([[1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    ),
    "color": "purple",
    "tried": 0,
    "coord": (0, -1),
}
beige_p = {
    "id": 10,
    "geo": generate_rotation_set(
        np.array([[1, 1, 1, 1], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    ),
    "color": "beige",
    "tried": 0,
    "coord": (0, -1),
}
light_green_p = {
    "id": 11,
    "geo": generate_rotation_set(
        np.array([[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    ),
    "color": "l_green",
    "tried": 0,
    "coord": (0, -1),
}
yellow_p = {
    "id": 12,
    "geo": generate_rotation_set(
        np.array([[1, 1, 1, 0], [1, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    ),
    "color": "yellow",
    "tried": 0,
    "coord": (0, -1),
}

full_set = [
    green_p,
    orange_p,
    red_p,
    cyan_p,
    gray_p,
    blue_p,
    white_p,
    pink_p,
    purple_p,
    beige_p,
    light_green_p,
    yellow_p,
]


def get_color_by_id(p_id):
    for piece in full_set:
        if p_id == piece["id"]:
            return piece["color"]
    return "black"


def check_piece_fit_in_place(p_geo, coord, grid):
    """Check if the given piece can fit in the given location"""
    x = coord[0]
    y = coord[1]
    (height, width) = p_geo.shape
    for i in range(height):
        for j in range(width):
            if p_geo[i, j] != 0 and grid[x + i, y + j] != 0:
                return False
    return True


def put_piece_in_grid(p_geo, coord, grid, p_id):
    """Add given piece into the grid"""
    x = coord[0]
    y = coord[1]
    (height, width) = p_geo.shape
    for i in range(height):
        for j in range(width):
            if p_geo[i, j] != 0:
                grid[x + i, y + j] = p_id


def check_piece(piece, grid):
    """Check if this piece can fit anywhere in the grid

    Return first place available
    """
    (height, width) = grid.shape
    rot_set = piece["geo"]
    already_tried = piece["tried"]
    (prev_x, prev_y) = piece["coord"]
    # first, iterate over the rotation set of the piece
    # skip the piece position we already tried
    for (index, p) in enumerate(rot_set[already_tried:]):
        # second, iterate over the all grid
        # remove last 3 lines and 3 last columns
        for i in range(height - (P_MAX_SIZE - P_MIN_SIZE) - prev_x):
            for j in range(width - (P_MAX_SIZE - P_MIN_SIZE)):
                # get to previous position
                if i == 0 and j <= prev_y:
                    continue
                coord = (prev_x + i, j)
                # TODO: let's say we tried a position, and then we try the
                # position right to its right. Depending on the piece geometry
                # and grid fulfillment, some matrix element may be checked
                # multiple times. Maybe we can add some kind of 'memory'
                # for the places that are OK. Or maybe it is not worth it.
                if check_piece_fit_in_place(p, coord, grid):
                    put_piece_in_grid(p, coord, grid, piece["id"])
                    # register the new position we validated to avoid
                    # trying the same things over and over again
                    validated_try = already_tried + index
                    piece["tried"] = validated_try
                    piece["coord"] = coord
                    return True
        # changing piece rotation: reset coordinate
        (prev_x, prev_y) = (0, 0)
    return False


def remove_piece_from_grid(piece, grid):
    """remove the given piece from the grid

    Remove all pieces with the matching id
    """
    p_id = piece["id"]
    (height, width) = grid.shape
    for i in range(height):
        for j in range(width):
            if grid[i, j] == p_id:
                grid[i, j] = 0
