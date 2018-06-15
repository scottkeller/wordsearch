"""
MODULE: core.grid
DESCRIPTION: Creates a grid of cells based on a string with optional delimiters
"""

class Grid(object):
    """Grid object containing cells of data"""
    def __init__(self, text, x_seperator=None):
        self.text = text
        self.cells = self.create_cells(text, x_seperator)

    @staticmethod
    def create_cells(text, x_seperator=None):
        cells = set()
        y = 0
        for line in text:
            print line
            x = 0
            line = line.strip()
            if x_seperator is not None:
                line = line.split(x_seperator)
            for value in line:
                cells.add(Cell(x, y, value))
                x+=1
            y+=1
        return cells




class Cell(object):
    """Cell object containg x,y coordinates and value"""
    def __init__(self, x, y, value):
        self.coordinates = (x, y)
        self.value = value