#!/usr/bin/python3
"""Module that computes the perimeter of an island in a grid."""


def island_perimeter(grid):
    """Return the perimeter of the island described in grid.

    Each land cell adds 4 sides; every pair of adjacent land
    cells (horizontal or vertical) removes 2 shared sides.
    """
    perimeter = 0
    rows = len(grid)
    for i in range(rows):
        cols = len(grid[i])
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
