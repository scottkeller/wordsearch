"""
MODULE: test_grid
DESCRIPTION: Runs unit tests on the grid module
"""

import unittest
import os
from ..core import grid

class TestGrid(unittest.TestCase):
    """Unit tests for the min module"""

    def setUp(self):
        self.grid = grid.Grid
        self.cell = grid.Cell

    def test_grid_exists(self):
        """Tests grid object exists"""
        self.assertIsNotNone(self.grid)
        self.assertEqual(self.grid, grid.Grid)

    def test_cell_exists(self):
        """Tests cell objext exists"""
        self.assertIsNotNone(self.cell)
        self.assertEqual(self.cell, grid.Cell)

    def test_cell_attributes(self):
        """Tests setting of cell attributes"""
        my_cell = self.cell(0, 1, 'foo')
        self.assertEqual(my_cell.coordinates, (0, 1))
        self.assertEqual(my_cell.value, 'foo')

    def test_grid_cells(self):
        """Tests creating the cells of a grid"""
        my_grid = self.grid(['a,b,c,d\n', 'e,f,g,h\n', 'i,j,k,l'], x_seperator=',')
        self.assertEqual(len(my_grid.cells), 12)
