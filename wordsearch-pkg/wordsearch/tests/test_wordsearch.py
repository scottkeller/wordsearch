"""
MODULE: test_wordsearch
DESCRIPTION: Runs unit tests on the wordsearch module
"""

import unittest
from ..core import wordsearch, grid

class TestWordSearch(unittest.TestCase):
    """Unit tests for the word search module"""

    def setUp(self):
        self.wordsearch = wordsearch.WordSearch

    def test_wordsearch_exists(self):
        """Test the WordSearch oject exists"""
        self.assertIsNotNone(self.wordsearch)
        self.assertEqual(self.wordsearch, wordsearch.WordSearch)

    def test_wordsearch_grid(self):
        """"Test the wordsearch has a grid property"""
        my_wordsearch = self.wordsearch('SCOTTKELLER')
        self.assertIsInstance(my_wordsearch, grid.Grid)

    def test_find_adjacent_cells(self):
        """test adjacent cell coordinates are correctly found"""
        my_wordsearch = self.wordsearch(['a,b,c\n', 'd,e,f\n', 'g,h,i'])
        # test origin
        self.assertEqual(my_wordsearch.find_adjacent_cells(0,0), {(0, 1), (1, 0), (1, 1)})
        # test last cell
        self.assertEqual(my_wordsearch.find_adjacent_cells(2, 2), {(1, 2), (1, 1), (2, 1)})
        # test center
        self.assertEqual(my_wordsearch.find_adjacent_cells(1, 1),
                         {(0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2)})
    def test_search_invalid_word_length(self):
        """tests words less than 2 characters are rejected"""
        my_wordsearch = self.wordsearch(['a,b,c\n', 'd,e,f\n', 'g,h,i'])
        self.assertRaises(ValueError, my_wordsearch.search, 'a')

    def test_search_horizontal_right(self):
        """Test finding a word horizontally to the right """
        my_wordsearch = self.wordsearch(['w,o,r,d\n', 'x,x,x,x\n', 'w,r,o,d'])
        self.assertEqual(my_wordsearch.search('word'), [(0,0), (1,0), (2,0), (3,0)])

    def test_search_horizontal_left(self):
        """Test finding a word horizontally to the left """
        my_wordsearch = self.wordsearch(['w,o,r,l\n', 'x,x,x,x\n', 'd,r,o,w'])
        self.assertEqual(my_wordsearch.search('word'), [(3,2), (2,2), (1,2), (0,2)])

    def test_vertical_down(self):
        """Test finding a word vertically down"""
        my_wordsearch = self.wordsearch(['w,x,x,x\n', 'o,x,x,x\n', 'r,x,x,x\n', 'd,x,x,x'])
        self.assertEqual(my_wordsearch.search('word'), [(0,0), (0,1), (0,2), (0,3)])

    def test_vertical_up(self):
        """Test finding a word vertically up"""
        my_wordsearch = self.wordsearch(['d,x,x,x\n', 'r,x,x,x\n', 'o,x,x,x\n', 'w,x,x,x'])
        self.assertEqual(my_wordsearch.search('word'), [(0,3), (0,2), (0,1), (0,0)])

    def test_diagonal_ascending_right(self):
        """Test finding a word diagonally ascending to the right"""
        my_wordsearch = self.wordsearch(['x,x,x,d\n', 'x,x,r,x\n', 'x,o,x,x\n', 'w,x,x,x'])
        self.assertEqual(my_wordsearch.search('word'), [(0,3), (1,2), (2,1), (3,0)])

    def test_diagonal_ascending_left(self):
        """Test finding a word diagonally ascending to the left"""
        my_wordsearch = self.wordsearch(['d,x,x,x\n', 'x,r,x,x\n', 'x,x,o,x\n', 'x,x,x,w'])
        self.assertEqual(my_wordsearch.search('word'), [(3,3), (2,2), (1,1), (0,0)])

    def test_diagonal_descending_right(self):
        """Test finding a word diagonally descending to the right"""
        my_wordsearch = self.wordsearch(['w,x,x,x\n', 'x,o,x,x\n', 'x,x,r,x\n', 'x,x,x,d'])
        self.assertEqual(my_wordsearch.search('word'), [(0,0), (1,1), (2,2), (3,3)])

    def test_diagonal_descending_left(self):
        """Test finding a word diagonally descending to the left"""
        my_wordsearch = self.wordsearch(['x,x,x,w\n', 'x,x,o,x\n', 'x,r,x,x\n', 'd,x,x,x'])
        self.assertEqual(my_wordsearch.search('word'), [(3,0), (2,1), (1,2), (0,3)])

    def test_not_found(self):
        """Test finding a word not in the grid"""
        my_wordsearch = self.wordsearch(['x,x,x,w\n', 'x,x,o,x\n', 'x,r,x,x\n', 'd,x,x,x'])
        self.assertEqual(my_wordsearch.search('notfound'), None)

