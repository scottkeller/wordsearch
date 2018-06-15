"""
MODULE: core.wordsearch
DESCRIPTION: Creates a word search game capable of creating a word search
             grid and searching for words hidden in it
"""

class WordSearch(object):
    """
    Word search class to store grid and functions for searching

    PROPERTIES:

    """

    def __init__(self, words, grid):
        self.words = words
        self.grid = grid