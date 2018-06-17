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
        # find all adjacent cell coordinates that exist in the grid
        return {(x+ox, y+oy) for (ox, oy) in offset if (x+ox, y+oy) in {c.coordinates for c in self.cells}}

    def search(self, word):
        """searches for a word in the wordsearch grid"""
        if len(word) < 2:
            raise ValueError('Invalid word {}: must be at least 2 characters'.format(word))
        # set letter index
        index = 0
        # get all coordinates of first letter
        coords = self.find_coordinates(word[0])
        # Return None if the first letter was not found in the grid
        if coords is None:
            return None
        #check each coordinate
        for coord in coords:
            x, y = coord
            # Find the direction of any matching second letters
            direction = {(ax - x, ay -y) for ax, ay in self.find_adjacent_cells(x, y) if self.find_value(ax, ay) == word[1]}
            for dir in direction:
                dx, dy = dir
                # add the current first letter coordinates to the matches list
                matches = [coord]
                # check the letters after the first letter
                for i in range(len(word) -1 ):
                    # move in the direction
                    x = x+dx
                    y = y+dy
                    # add the coordinates to the matches list if the letter at those coordinates matches
                    # the letter in the word
                    if self.find_value(x,y) == word[i+1]:
                        matches.append((x,y))
                    # if it doesn't match move on and try the next direction if any
                    else:
                        break
                # return the matches coordinates if the string representation is an exact match of the word
                if ''.join([self.find_value(mx, my) for mx, my in matches]) == word:
                    return matches

        return None
