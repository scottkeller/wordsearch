### wordsearch:0.0.1

### Description
**wordsearch** is a python utility for solving word search puzzles. Given a text file with
a comma separated list of words to find on the first line, and a "grid" of comma separated characters on
the subsequent lines, word search will print the x,y coordinates of each word.

### Installation
    # from the wordsearch repository root directory

    pip install -e ./wordsearch-pkg

### Input File
**wordsearch** accepts an input text file with a comma separated list of words
to find on the first line, and a "grid" of comma separated characters on
the subsequent lines. There are example input files located in the project root directory.

###### NOTE:
Words must be at least 2 characters long. Anything less will result in a
ValueError exception.

##### Sample Input:

    BONES,KHAN,KIRK,SCOTTY,SPOCK,SULU,UHURA
    U,M,K,H,U,L,K,I,N,V,J,O,C,W,E
    L,L,S,H,K,Z,Z,W,Z,C,G,J,U,Y,G
    H,S,U,P,J,P,R,J,D,H,S,B,X,T,G
    B,R,J,S,O,E,Q,E,T,I,K,K,G,L,E
    A,Y,O,A,G,C,I,R,D,Q,H,R,T,C,D
    S,C,O,T,T,Y,K,Z,R,E,P,P,X,P,F
    B,L,Q,S,L,N,E,E,E,V,U,L,F,M,Z
    O,K,R,I,K,A,M,M,R,M,F,B,A,P,P
    N,U,I,I,Y,H,Q,M,E,M,Q,R,Y,F,S
    E,Y,Z,Y,G,K,Q,J,P,C,Q,W,Y,A,K
    S,J,F,Z,M,Q,I,B,D,B,E,M,K,W,D
    T,G,L,B,H,C,B,E,C,H,T,O,Y,I,K
    O,J,Y,E,U,L,N,C,C,L,Y,B,Z,U,H
    W,Z,M,I,S,U,K,U,R,B,I,D,U,X,S
    K,Y,L,B,Q,Q,P,M,D,F,C,K,E,A,B

### Usage
    wordsearch solve /path/to/input/file.txt

##### Sample Output
    BONES: (0,6),(0,7),(0,8),(0,9),(0,10)
    KHAN: (5,9),(5,8),(5,7),(5,6)
    KIRK: (4,7),(3,7),(2,7),(1,7)
    SCOTTY: (0,5),(1,5),(2,5),(3,5),(4,5),(5,5)
    SPOCK: (2,1),(3,2),(4,3),(5,4),(6,5)
    SULU: (3,3),(2,2),(1,1),(0,0)
    UHURA: (4,0),(3,1),(2,2),(1,3),(0,4)


### Tests
Tests are located in the "wordsearch-pkg/wordsearch/tests" directory. To run tests:

    cd wordsearch-pkg/

    # And then run using setup.py

    python setup.py test

    # OR using unittest discovery

    python -m unittest discover -v

##### Sample Test Output:
    Tests setting of cell attributes ... ok
    test_cell_exists (wordsearch.tests.test_grid.TestGrid)
    Tests cell objext exists ... ok
    test_find_grid_cell (wordsearch.tests.test_grid.TestGrid)
    Tests finding a cell in a grid ... ok
    test_find_grid_cell_by_coordinates (wordsearch.tests.test_grid.TestGrid)
    Tests finding a cell in a grid by it's coordinates ... ok
    test_grid_cell_creation (wordsearch.tests.test_grid.TestGrid)
    Tests creating the cells of a grid ... ok
    test_grid_exists (wordsearch.tests.test_grid.TestGrid)
    Tests grid object exists ... ok
    test_diagonal_ascending_left (wordsearch.tests.test_wordsearch.TestWordSearch)
    Test finding a word diagonally ascending to the left ... ok
    test_diagonal_ascending_right (wordsearch.tests.test_wordsearch.TestWordSearch)
    Test finding a word diagonally ascending to the right ... ok
    test_diagonal_descending_left (wordsearch.tests.test_wordsearch.TestWordSearch)
    Test finding a word diagonally descending to the left ... ok
    test_diagonal_descending_right (wordsearch.tests.test_wordsearch.TestWordSearch)
    Test finding a word diagonally descending to the right ... ok
    test_find_adjacent_cells (wordsearch.tests.test_wordsearch.TestWordSearch)
    test adjacent cell coordinates are correctly found ... ok
    test_multiple_directions (wordsearch.tests.test_wordsearch.TestWordSearch)
    Test finding a word when there are multiple potentail directional matches ... ok
    test_not_found (wordsearch.tests.test_wordsearch.TestWordSearch)
    Test finding a word not in the grid ... ok
    test_search_horizontal_left (wordsearch.tests.test_wordsearch.TestWordSearch)
    Test finding a word horizontally to the left ... ok
    test_search_horizontal_right (wordsearch.tests.test_wordsearch.TestWordSearch)
    Test finding a word horizontally to the right ... ok
    test_search_invalid_word_length (wordsearch.tests.test_wordsearch.TestWordSearch)
    tests words less than 2 characters are rejected ... ok
    test_vertical_down (wordsearch.tests.test_wordsearch.TestWordSearch)
    Test finding a word vertically down ... ok
    test_vertical_up (wordsearch.tests.test_wordsearch.TestWordSearch)
    Test finding a word vertically up ... ok
    test_wordsearch_exists (wordsearch.tests.test_wordsearch.TestWordSearch)
    Test the WordSearch oject exists ... ok
    test_wordsearch_grid (wordsearch.tests.test_wordsearch.TestWordSearch)
    "Test the wordsearch has a grid property ... ok
    test_cannot_read_file (wordsearch.tests.test_main.TestMain)
    Tests that exception is thrown if the file is not found ... File not found at file/not/found
    ok
    test_read_file (wordsearch.tests.test_main.TestMain)
    Tests reading a file ... ok
    test_solve_wordsearch (wordsearch.tests.test_main.TestMain)
    Tests correctly solving a wordsearch puzzle ... ok
    test_solve_wordsearch_exists (wordsearch.tests.test_main.TestMain)
    Test the solve_wordsearch function exists ... ok

    ----------------------------------------------------------------------
    Ran 24 tests in 0.014s


