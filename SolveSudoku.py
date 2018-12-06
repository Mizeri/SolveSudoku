import numpy as np

Sudoku = np.array([0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9,
                  [0] * 9, [0] * 9, [0] * 9)


def findNextCell(sudoku):
    for i in range(0, 9):
        for j in range(0, 9):
            if sudoku[i][j] == 0:
                return i, j
    return -1, -1


def isValid(sudoku, x, y, e):
    row_isValid = all([e != sudoku[x][p] for p in range(0, 9)])
    col_isValid = all([e != sudoku[q][y] for q in range(0, 9)])
    sec_isValid = all([e != sudoku[q][p]
                       for q in range(x // 3 * 3, x // 3 * 3 + 3)
                       for p in range(y // 3 * 3, y // 3 * 3 + 3)])
    return (row_isValid and col_isValid and sec_isValid)


def solveSudoku(sudoku, i=0, j=0):

    global times

    i, j = findNextCell(sudoku)
    if i == -1 and j == -1:
        return True

    for e in range(1, 10):
        if isValid(sudoku, i, j, e):
            sudoku[i][j] = e
            if solveSudoku(sudoku, i, j):
                return True
            sudoku[i][j] = 0
            times += 1
    return False


if __name__ == '__main__':
    solveSudoku()
