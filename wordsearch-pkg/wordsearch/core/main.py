"""
MODULE: core.main
DESCRIPTION: Creates and solves a wordsearch game given the words and grid from an input file
"""
import codecs
import os

def solve_wordsearch(path):
    pass

def read_file(path):
    """Reads a file from a given path"""
    return codecs.open(filename=resolve_path(path), mode='r', encoding='utf-8')

def resolve_path(path):
    """Resolves relative paths and returns the absolute path"""
    if path.startswith('~'):
        path = os.path.expanduser(path)

    elif os.path.isabs(path) is False:
        path = os.path.join(os.path.abspath(os.getcwd()), path)

    return os.path.realpath(path)