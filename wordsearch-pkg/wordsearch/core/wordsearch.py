"""
MODULE: core.wordsearch
DESCRIPTION: Creates a word search game capable of creating a word search
             grid and searching for words hidden in it
"""

from .grid import Grid
class WordSearch(object):
    """
    Word search class to store grid and functions for searching

    PROPERTIES:

    """

    def __init__(self, words, word_grid):
        self.words = words
        self.grid = Grid(word_grid)