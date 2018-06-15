"""
MODULE: core.main
DESCRIPTION: Creates and solves a wordsearch game given the words and grid from an input file
"""
import codecs
import os
import sys

def solve_wordsearch(path):
    try:
        my_file = read_file(path)

    except IOError:
        print('File not found at {}'.format(path))
        sys.exit(-1)

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