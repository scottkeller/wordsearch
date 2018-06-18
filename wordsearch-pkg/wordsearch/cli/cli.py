"""
MODULE: cli.cli.py
DESCRIPTION: CLI wrapper using Google's fire module
"""
from __future__ import absolute_import
import fire
from ..core import main

class Pipeline(object):
    """Solves a word search given an input file"""
    def solve(self, path):
       for word in main.solve_wordsearch(path):
           print(word)

def _main():
    """Wrapper for main fire cli caller"""
    fire.Fire(Pipeline)

if __name__ == '__main__':
    _main()