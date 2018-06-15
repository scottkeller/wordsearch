"""
MODULE: test_wordsearch
DESCRIPTION: Runs unit tests on the wordsearch module
"""

import unittest
from ..core import wordsearch

class TestWordSearch(unittest.TestCase):
    """Unit tests for the word search module"""

    def setUp(self):
        self.wordsearch = wordsearch.WordSearch

    def test_wordsearch_exists(self):
        """Test the WordSearch oject exists"""
        self.assertIsNotNone(self.wordsearch)
        self.assertEqual(self.wordsearch, wordsearch.WordSearch)

    def test_wordsearch_words(self):
        """Test wordsearch can have words added"""
        my_wordsearch = self.wordsearch(words=['SCOTT', 'KELLER'], grid='SCOTTKELLER')
        self.assertEqual(my_wordsearch.words, ['SCOTT', 'KELLER'])

    def test_wordsearch_grid(self):
        """"Test the wordsearch has a grid property"""
        my_wordsearch = self.wordsearch(['SCOTT', 'KELLER'], 'SCOTTKELLER')
        self.assertEqual(my_wordsearch.grid, 'SCOTTKELLER')
