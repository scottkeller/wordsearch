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

    def test_find_grid_cell_value(self):
        """Tests finding a cell value in a grid"""
        my_grid = self.grid(['a,b,c,d\n', 'e,f,g,h\n', 'i,j,k,l'], x_seperator=',')
        self.assertEqual(my_grid.find_value(0 ,0), 'a')
        self.assertEqual(my_grid.find_value(1, 0), 'b')
        self.assertEqual(my_grid.find_value(2, 0), 'c')
        self.assertEqual(my_grid.find_value(3, 0), 'd')
        self.assertEqual(my_grid.find_value(0, 1), 'e')
        self.assertEqual(my_grid.find_value(1, 1), 'f')
        self.assertEqual(my_grid.find_value(2, 1), 'g')
        self.assertEqual(my_grid.find_value(3, 1), 'h')
        self.assertEqual(my_grid.find_value(0, 2), 'i')
        self.assertEqual(my_grid.find_value(1, 2), 'j')
        self.assertEqual(my_grid.find_value(2, 2), 'k')
        self.assertEqual(my_grid.find_value(3, 2), 'l')

    def test_find_grid_cell(self):
        """Tests finding a cell in a grid"""
        my_grid = self.grid(['g,o,o,d\n', 'n,i,g,h\n', 't,t,o,o'], x_seperator=',')
        self.assertEqual(my_grid.find_coordinates('o'), {(1,0), (2,0), (2,2), (3,2)})
        self.assertEqual(my_grid.find_coordinates('g'), {(0, 0), (2, 1)})
        self.assertEqual(my_grid.find_coordinates('t'), {(0, 2), (1, 2)})
        self.assertEqual(my_grid.find_coordinates('n'), {(0, 1)})
        self.assertEqual(my_grid.find_coordinates('i'), {(1, 1)})
        self.assertEqual(my_grid.find_coordinates('h'), {(3, 1)})
        self.assertEqual(my_grid.find_coordinates('x'), None)
    
