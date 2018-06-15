"""
MODULE: test_main
DESCRIPTION: Runs unit tests on the main module
"""

import unittest
from ..core import main

class TestWordSearch(unittest.TestCase):
    """Unit tests for the min module"""

    def test_solve_wordsearch_exists(self):
        """Test the solve_wordsearch function exists"""
        self.assertIsNotNone(main.solve_wordsearch)
        self.assertTrue(callable(main.solve_wordsearch))