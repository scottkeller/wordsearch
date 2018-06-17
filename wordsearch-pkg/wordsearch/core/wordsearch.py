"""
MODULE: core.wordsearch
DESCRIPTION: Creates a word search game capable of creating a word search
             grid and searching for words hidden in it
"""

from .grid import Grid
class WordSearch(Grid):
    """
    Word search class to store grid and functions for searching

    PROPERTIES:
    words - list of words to search for
    grid - the word search grid to search

    """

    def __init__(self, word_grid, x_seperator=','):
        Grid.__init__(self, word_grid, x_seperator=x_seperator)


    def find_adjacent_cells(self, x, y):
        """find cells adjacent to a given cell"""
        offset = {(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)}
        # find all possible adjacent cell coordinates that exist in the grid
        return {(x+ox, y+oy) for (ox, oy) in offset if x+ox >=0 and y+oy >= 0 and (x+ox, y+oy) in {c.coordinates for c in self.cells}}

