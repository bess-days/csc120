"""
File: word_search.py
Author: Sydney Bess Greenspun
Purpose: Computes every legal (official English term/word) in a grid of letters,
resembling a word search, this programs finds and returns the words/

"""


def read_words():
    """
    Reads a text file which lists a word considered official english (technically the Google-Corpus
    as somee aren't from the official espana view [ask any linguist like me: what is english]
    , then it turns int a list)
    Paramaters: null - but input is given that initiallizes what file to read
    Returns: a list of all the words in the word file - specifically, each line
    being an item in the list
    """
    word_list = []
    all_words = input()
    words = open(all_words)
    for word in words:
        word = word.lower()
        word_list.append(word.strip("\n"))
    return word_list


def read_grid():
    """
    Reads a text file with a N by N grid of characters,saving the grid
    and transforming it into a list of the rows
    Paramaters: null - but input is given that initiallizes what file
    to read (grid_file)
    Returns: a list of all the words in the word file - specifically, each line
    being an item in the list
    """
    grid = []
    grid_file = input()
    grids = open(grid_file, "r")
    for g in grids:
        grid.append(g.split())
    return grid


def horizontal(grid, word_list, possible):
    """
    Reads a grid (lists of lists takin from read_grid()) and
    sees if within the row (incrementing across te x axis),
    any word from word_list could be found
    Paramaters:  a grid called from the return of read_grid,
    a list of words called from the
    return of read_words(), possible is the list legal words
    found in the row are addded
    Returns: null
    """

    for i in range(len(grid)):
        horizontal_rl = "".join(grid[i])
        horizontal_lr = "".join(grid[i][::-1])

        for i in range(len(word_list)):
            if word_list[i] in horizontal_rl and len(word_list[i]) >= 3:
                possible.append(word_list[i])
            if word_list[i] in horizontal_lr and len(word_list[i]) >= 3:
                possible.append(word_list[i])


def verticle(grid, word_list, possible):
    """
    Reads a grid (lists of lists takin from read_grid())
    and and sees if within the column
    goes through each column (meaning it incriments across y axis )
    any word from word_list could be found
    Paramaters:  a grid called from the return of read_grid
    a list of words called from the return of read_words()
    possible is the list legal words found in the row are addded
    Returns: null
    """

    column = []
    columns = []
    c = 0
    while c < len(grid):
        for i in range(len(grid)):
            column.append(grid[i][c])
            if len(column) == len(grid):
                col = "".join(column)
                columns.append(col)
                column = []
        c += 1
        for verticle in columns:
            verticle_ud = verticle
            verticle_du = verticle[::-1]
        for i in range(len(word_list)):
            if word_list[i] in verticle_ud and len(word_list[i]) >= 3:
                possible.append(word_list[i])
            if word_list[i] in verticle_du and len(word_list[i]) >= 3:
                possible.append(word_list[i])


def diagnol(grid, word_list, possible):
    """
    Reads a grid (lists of lists takin from read_grid()) and
    sees if within the column
    goes through each diagnol combination (meaning it incriments
    across x and y axis)
    any word from word_list could be found
    Paramaters:  a grid called from the return of read_grid,
    a list of words called from the return of read_words(),
    possible is the list legal words  found in the row are addded
    Returns: null
    """
    diagnol = []
    diagnols = []
    d = 0
    diagnol_front = ""
    diagnol_back = ""
    while d < len(grid):
        for i in range(len(grid)):
            diagnol.append("".join(grid[i][i - d]))
            if i == 0:
                diagnol = ["".join([grid[i][i - d]])]
        d += 1
        diagnol_front = "".join(diagnol)
        diagnol_back = "".join(diagnol[::-1])
        for i in range(len(word_list)):
            if word_list[i] in diagnol_front and len(word_list[i]) >= 3:
                possible.append(word_list[i])
            if word_list[i] in diagnol_back and len(word_list[i]) >= 3:
                possible.append(word_list[i])


def main():
    """
    This function puts everything together, mainly establishing the list of legal
    found words ("possible"), establshing the word list from read_words() to be used
    as arguments for inner-functions, establishes the list of lists of the grid rows
    returns: null, but does print all each word found from possible in alphabetical order
    """
    possible = []
    word_list = read_words()
    grid = read_grid()
    horizontal(grid, word_list, possible)
    verticle(grid, word_list, possible)
    diagnol(grid, word_list, possible)
    possible.sort()
    for legal in possible:
        print(legal)


main()