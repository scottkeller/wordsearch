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

    def test_solve_wordsearch(self):
        """Tests correctly solving a wordsearch puzzle"""
        self.assertEqual(main.solve_wordsearch(os.path.join(DIR_PATH, 'test_input.txt')),
                         ['BONES: (0,6),(0,7),(0,8),(0,9),(0,10)',
                          'KHAN: (5,9),(5,8),(5,7),(5,6)',
                          'KIRK: (4,7),(3,7),(2,7),(1,7)',
                          'SCOTTY: (0,5),(1,5),(2,5),(3,5),(4,5),(5,5)',
                          'SPOCK: (2,1),(3,2),(4,3),(5,4),(6,5)',
                          'SULU: (3,3),(2,2),(1,1),(0,0)',
                          'UHURA: (4,0),(3,1),(2,2),(1,3),(0,4)'
                          ])

if __name__ == '__main__':
    unittest.main()