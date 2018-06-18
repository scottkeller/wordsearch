"""
MODULE: core.main
DESCRIPTION: Creates and solves a wordsearch game given the words and grid from an input file
"""
import codecs
import os
import sys
from .wordsearch import WordSearch

def solve_wordsearch(path):
    try:
        my_file = read_file(path)

    except IOError:
        print('File not found at {}'.format(path))
        sys.exit(-1)
    file_data = my_file.readlines()
    words = file_data.pop(0).strip().split(',')
    my_wordsearch = WordSearch(file_data)
    solution = []
    for word in words:
        coords = my_wordsearch.search(word)
        if coords is not None:
            solution.append('{}: {}'.format(word, ','.join([str(c).replace(' ', '') for c in coords])))
        else:
            solution.append('{}: Not found!'.format(word))
    return solution

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