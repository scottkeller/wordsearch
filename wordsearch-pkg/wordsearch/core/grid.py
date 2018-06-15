"""
MODULE: core.grid
DESCRIPTION: Creates a grid of cells based on a string with optional delimiters
"""

class Grid(object):
    """Grid object containing cells of data"""
    def __init__(self):
        pass

class Cell(object):
    """Cell object containg x,y coordinates and value"""
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value