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