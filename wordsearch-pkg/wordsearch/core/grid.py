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
            x = 0
            line = line.strip()
            if x_seperator is not None:
                line = line.split(x_seperator)
            for value in line:
                cells.add(Cell(x, y, value))
                x+=1
            y+=1
        return cells

    def find_value(self, x, y):
        """find a cell value given its coordinates"""
        for cell in self.cells:
            if cell.coordinates == (x,y):
                return cell.value
        else:
            return None

    def find_coordinates(self, value):
        """find coordinates of all cells with a given value"""
        cells = {v.coordinates for v in self.cells if v.value == value}
        return cells if len(cells) > 0 else None




class Cell(object):
    """Cell object containg x,y coordinates and value"""
    def __init__(self, x, y, value):
        self.coordinates = (x, y)
        self.value = value