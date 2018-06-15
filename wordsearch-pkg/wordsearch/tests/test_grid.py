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

    def test_grid_cell_creation(self):
        """Tests creating the cells of a grid"""
        my_grid = self.grid(['a,b,c,d\n', 'e,f,g,h\n', 'i,j,k,l'], x_seperator=',')
        self.assertEqual(len(my_grid.cells), 12)

    def test_find_grid_cell(self):
        """Tests finding a cell in a grid"""
        my_grid = self.grid(['a,b,c,d\n', 'e,f,g,h\n', 'i,j,k,l'], x_seperator=',')
        self.assertEqual(my_grid.find(0 ,0).value, 'a')
        self.assertEqual(my_grid.find(1, 0).value, 'b')
        self.assertEqual(my_grid.find(2, 0).value, 'c')
        self.assertEqual(my_grid.find(3, 0).value, 'd')
        self.assertEqual(my_grid.find(0, 1).value, 'e')
        self.assertEqual(my_grid.find(1, 1).value, 'f')
        self.assertEqual(my_grid.find(2, 1).value, 'g')
        self.assertEqual(my_grid.find(3, 1).value, 'h')
        self.assertEqual(my_grid.find(0, 2).value, 'i')
        self.assertEqual(my_grid.find(1, 2).value, 'j')
        self.assertEqual(my_grid.find(2, 2).value, 'k')
        self.assertEqual(my_grid.find(3, 2).value, 'l')
