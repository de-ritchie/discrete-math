import copy
import time

def bound(i, j, n, element, sudoku) :

    # is it in the row or col
    for p in range(n) :
        if j != p and sudoku[i][p] == element :
            print('is it in the row', i, j, p)
            return False
        if i != p and sudoku[p][j] == element :
            print('is it in the col', i, j, p)
            return False
    # is it in the cell
    row = -1
    col = -1

    if i > 5 and i < 9 :
        row = 6
    if i % 6 > 2 and i % 6 <= 5 :
        row = 3
    else :
        row = 0

    if j > 5 and j < 9 :
        col = 6
    if j % 6 > 2 and j % 6 <= 5 :
        col = 3
    else :
        col = 0

    for r in range(row, row + 3) :
        for c in range(col, col + 3) :
            if r != i and c != col and sudoku[r][c] == element :
                return False

    return True

def backtrack(i, j, n, sudoku, result, elements) :

    if i >= n :
        print('base case', sudoku)
        result['result'].append(copy.deepcopy(sudoku))
        return True

    if sudoku[i][j] != 0 :
        if j < n-1 :
            backtrack(i, j+1, n, sudoku, result, elements)
        if j >= n-1 :
            backtrack(i+1, 0, n, sudoku, result, elements)
        # raise Exception('Dangerous Dude')
        return

    for element in elements :
        if bound(i, j, n, element, sudoku) :
            sudoku[i][j] = element
            if j < n-1 :
                backtrack(i, j+1, n, sudoku, result, elements)
            if j >= n-1 :
                backtrack(i+1, 0, n, sudoku, result, elements)
        sudoku[i][j] = 0
            

n = 9
result = {'result': []}
sudoku = [[0 for i in range(n)] for j in range(n)]
t1 = time.time()

sudoku[0][0] = 1
sudoku[0][1] = 9
sudoku[0][2] = 4
sudoku[0][3] = 5
sudoku[0][4] = 0
sudoku[0][5] = 7
sudoku[0][6] = 6
sudoku[0][7] = 3
sudoku[0][8] = 8
sudoku[1][0] = 0
sudoku[1][1] = 0
sudoku[1][2] = 5
sudoku[1][3] = 0
sudoku[1][4] = 0
sudoku[1][5] = 0
sudoku[1][6] = 9
sudoku[1][7] = 0
sudoku[1][8] = 7
sudoku[2][0] = 3
sudoku[2][1] = 0
sudoku[2][2] = 0
sudoku[2][3] = 9
sudoku[2][4] = 0
sudoku[2][5] = 1
sudoku[2][6] = 0
sudoku[2][7] = 0
sudoku[2][8] = 0
sudoku[3][0] = 0
sudoku[3][1] = 1
sudoku[3][2] = 2
sudoku[3][3] = 0
sudoku[3][4] = 0
sudoku[3][5] = 0
sudoku[3][6] = 7
sudoku[3][7] = 8
sudoku[3][8] = 5
sudoku[4][0] = 0
sudoku[4][1] = 0
sudoku[4][2] = 0
sudoku[4][3] = 0
sudoku[4][4] = 0
sudoku[4][5] = 0
sudoku[4][6] = 0
sudoku[4][7] = 0
sudoku[4][8] = 0
sudoku[5][0] = 6
sudoku[5][1] = 8
sudoku[5][2] = 3
sudoku[5][3] = 0
sudoku[5][4] = 0
sudoku[5][5] = 0
sudoku[5][6] = 1
sudoku[5][7] = 2
sudoku[5][8] = 0
sudoku[6][0] = 0
sudoku[6][1] = 0
sudoku[6][2] = 0
sudoku[6][3] = 2
sudoku[6][4] = 0
sudoku[6][5] = 9
sudoku[6][6] = 0
sudoku[6][7] = 0
sudoku[6][8] = 3
sudoku[7][0] = 5
sudoku[7][1] = 0
sudoku[7][2] = 1
sudoku[7][3] = 0
sudoku[7][4] = 0
sudoku[7][5] = 0
sudoku[7][6] = 2
sudoku[7][7] = 0
sudoku[7][8] = 0
sudoku[8][0] = 9
sudoku[8][1] = 2
sudoku[8][2] = 6
sudoku[8][3] = 3
sudoku[8][4] = 0
sudoku[8][5] = 5
sudoku[8][6] = 0
sudoku[8][7] = 0
sudoku[8][8] = 0

backtrack(0, 0, n, sudoku, result, range(1, n+1))
t2 = time.time()
print(t2 - t1, result)