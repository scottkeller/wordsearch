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