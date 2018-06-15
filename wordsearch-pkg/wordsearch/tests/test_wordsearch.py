"""
MODULE: test_wordsearch.py
DESCRIPTION: Runs unit tests on the wordsearch module
"""

import unittest
from ..core import wordsearch

class TestWordSearch(unittest.TestCase):
    """Unit tests for the word search module"""

    def setUp(self):
        self. wordsearch = wordsearch.WordSearch

    def test_wordsearch_exists(self):
        """Test the WordSearch oject exists"""
        self.assertIsNotNone(self.wordsearch)
        self.assertEqual(self.wordsearch, wordsearch.WordSearch)
