"""
MODULE: test_main
DESCRIPTION: Runs unit tests on the main module
"""

import unittest
import os
from ..core import main



# Constants
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

class TestMain(unittest.TestCase):
    """Unit tests for the min module"""

    def test_solve_wordsearch_exists(self):
        """Test the solve_wordsearch function exists"""
        self.assertIsNotNone(main.solve_wordsearch)
        self.assertTrue(callable(main.solve_wordsearch))

    def test_read_file(self):
        """Tests reading a file"""
        self.assertIsNotNone(main.read_file(os.path.join(DIR_PATH, 'test_input.txt')))

    def test_cannot_read_file(self):
        """Tests that exception is thrown if the file is not found"""
        with self.assertRaises(SystemExit) as cm:
            main.solve_wordsearch('file/not/found')
        self.assertEqual(cm.exception.code, -1)