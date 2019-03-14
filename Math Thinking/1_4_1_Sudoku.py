import time
import copy

def clearMatrix (matrix, val):

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = val
            #print(i, j)
    return matrix

# def isBound(i, j, element, sudoku) :

#     # is it in the row or col
#     for p in range(9) :
#         if j != p and sudoku[i][p] == element :
#             print('it is in the row', i, j, p)
#             return False
#         if i != p and sudoku[p][j] == element :
#             print('it is in the col', i, j, p)
#             return False
#     # is it in the cell
#     row = -1
#     col = -1

#     if i > 5 and i < 9 :
#         row = 6
#     if i % 6 > 2 and i % 6 <= 5 :
#         row = 3
#     else :
#         row = 0

#     if j > 5 and j < 9 :
#         col = 6
#     if j % 6 > 2 and j % 6 <= 5 :
#         col = 3
#     else :
#         col = 0

#     for r in range(row, row + 3) :
#         for c in range(col, col + 3) :
#             if r != i and c != col and sudoku[r][c] == element :
#                 print('it is in the cell', i, j, r, c, row, col, element, sudoku)
#                 return False
    
#     print('it is in the cell', i, j, row, col, element, sudoku)
#     return True
    
def isBound(i, j, val, sudoku) :
    
    moduloList = [9, 6, 3]
    m = n = -1
    # for k in moduloList :
    #     if m > -1 and n > -1 :
    #         break
    #     if m == -1 and i % k > 3 and i % k >= 6 :
    #         m = 6
    #     if m == -1 and i % k >= 3 and i % k < 6 :
    #         m = 3
    #     if m == -1 and i % k < 3 :
    #         m = 0
    #     if n == -1 and j % k > 3 and j % k >= 6 :
    #         n = 6
    #     if n == -1 and j % k >= 3 and j % k < 6 :
    #         n = 3
    #     if n == -1 and j % k < 3 :
    #         n = 0

    if i > 5 and i < 9 :
        m = 6
    elif i % 6 > 2 and i % 6 <= 5 :
        m = 3
    else :
        m = 0

    if j > 5 and j < 9 :
        n = 6
    elif j % 6 > 2 and j % 6 <= 5 :
        n = 3
    else :
        n = 0
    
    if m > -1 and n > -1 :

        for p in range(9) :
            if p != i and sudoku[p][j] == val :
                print('it is in the col', i, j, p, sudoku[p][j], val)
                return False
            if p != j and sudoku[i][p] == val :
                print('it is in the row', i, j, p, sudoku[i][p], val)
                return False
        for p in range(m, m+3) :
            for q in range(n, n+3) :
                if i != p and j != q and sudoku[p][q] == val :
                    print('it is in the cell', i, j, p, q, sudoku[p][q], val, m, n)
                    return False
    else :
        print('danger', i, j, p, q, val, m, n)
        return False
    print('bound is true', i, j, p, q, val, m, n)
    return True


def backtrack(i, j, n, sudoku, result, isSolution) :

    if i >= n :
        print('base case', sudoku)
        result['result'].append(copy.deepcopy(sudoku))
        # raise Exception('Base case reached')
        return True

    if sudoku[i][j] != 0 :
        if j < n-1 :
            if(backtrack (i, j+1, n, sudoku, result, isSolution)):
                return True
        if j >= n-1 :
            if(backtrack (i+1, 0, n, sudoku, result, isSolution)) :
                return True
        return 
                
    for p in range(1, 10) :
        print(p, i, j, sudoku)
        if sudoku[i][j] == 0 and isBound(i, j, p, sudoku) :
            print('valid', p, i, j, sudoku)
            print(i, j)
            sudoku[i][j] = p
            if j < n-1 :
                if(backtrack (i, j+1, n, sudoku, result, isSolution)) :
                    return True
            if j >= n-1 :
                if(backtrack (i+1, 0, n, sudoku, result, isSolution)) :
                    return True
            sudoku[i][j] = 0
    if isSolution :
        return True
    return False


sudoku = [[0 for i in range(9)] for j in range(9)]
# matrix = [[[0  for x in range(3)] for y in range(3)] for z in range(3)]

clearMatrix(sudoku, 0)

# clearMatrix(sudoku, [])
# for i in range(len(sudoku)) :
#     for j in range(len(sudoku[i])) :
#         for k in range(len(sudoku[j])) :
#             sudoku[i][j][k] = matrix
# print(matrix)
# sudoku[0][0][0][0][0][0] = 1

# for i in range(9) :
#     for j in range(9) :
#         print("sudoku["+str(i)+"]["+str(j)+"] = 0")

# sudoku[0][0] = 1
# sudoku[0][1] = 9
# sudoku[0][2] = 4
# sudoku[0][3] = 5
# sudoku[0][4] = 0
# sudoku[0][5] = 7
# sudoku[0][6] = 6
# sudoku[0][7] = 3
# sudoku[0][8] = 8
# sudoku[1][0] = 0
# sudoku[1][1] = 0
# sudoku[1][2] = 5
# sudoku[1][3] = 0
# sudoku[1][4] = 0
# sudoku[1][5] = 0
# sudoku[1][6] = 9
# sudoku[1][7] = 0
# sudoku[1][8] = 7
# sudoku[2][0] = 3
# sudoku[2][1] = 0
# sudoku[2][2] = 0
# sudoku[2][3] = 9
# sudoku[2][4] = 0
# sudoku[2][5] = 1
# sudoku[2][6] = 0
# sudoku[2][7] = 0
# sudoku[2][8] = 0
# sudoku[3][0] = 0
# sudoku[3][1] = 1
# sudoku[3][2] = 2
# sudoku[3][3] = 0
# sudoku[3][4] = 0
# sudoku[3][5] = 0
# sudoku[3][6] = 7
# sudoku[3][7] = 8
# sudoku[3][8] = 5
# sudoku[4][0] = 0
# sudoku[4][1] = 0
# sudoku[4][2] = 0
# sudoku[4][3] = 0
# sudoku[4][4] = 0
# sudoku[4][5] = 0
# sudoku[4][6] = 0
# sudoku[4][7] = 0
# sudoku[4][8] = 0
# sudoku[5][0] = 6
# sudoku[5][1] = 8
# sudoku[5][2] = 3
# sudoku[5][3] = 0
# sudoku[5][4] = 0
# sudoku[5][5] = 0
# sudoku[5][6] = 1
# sudoku[5][7] = 2
# sudoku[5][8] = 0
# sudoku[6][0] = 0
# sudoku[6][1] = 0
# sudoku[6][2] = 0
# sudoku[6][3] = 2
# sudoku[6][4] = 0
# sudoku[6][5] = 9
# sudoku[6][6] = 0
# sudoku[6][7] = 0
# sudoku[6][8] = 3
# sudoku[7][0] = 5
# sudoku[7][1] = 0
# sudoku[7][2] = 1
# sudoku[7][3] = 0
# sudoku[7][4] = 0
# sudoku[7][5] = 0
# sudoku[7][6] = 2
# sudoku[7][7] = 0
# sudoku[7][8] = 0
# sudoku[8][0] = 9
# sudoku[8][1] = 2
# sudoku[8][2] = 6
# sudoku[8][3] = 3
# sudoku[8][4] = 0
# sudoku[8][5] = 5
# sudoku[8][6] = 0
# sudoku[8][7] = 0
# sudoku[8][8] = 0

sudoku[0][0] = 0 
sudoku[0][1] = 0 
sudoku[0][2] = 0 
sudoku[0][3] = 3 
sudoku[0][4] = 0 
sudoku[0][5] = 0 
sudoku[0][6] = 0 
sudoku[0][7] = 8 
sudoku[0][8] = 0 
sudoku[1][0] = 0 
sudoku[1][1] = 0 
sudoku[1][2] = 0 
sudoku[1][3] = 0 
sudoku[1][4] = 0 
sudoku[1][5] = 0 
sudoku[1][6] = 0 
sudoku[1][7] = 0 
sudoku[1][8] = 7 
sudoku[2][0] = 5 
sudoku[2][1] = 0 
sudoku[2][2] = 7 
sudoku[2][3] = 1 
sudoku[2][4] = 0 
sudoku[2][5] = 0 
sudoku[2][6] = 9 
sudoku[2][7] = 6 
sudoku[2][8] = 0 
sudoku[3][0] = 9 
sudoku[3][1] = 0 
sudoku[3][2] = 0 
sudoku[3][3] = 0 
sudoku[3][4] = 1 
sudoku[3][5] = 3 
sudoku[3][6] = 0 
sudoku[3][7] = 0 
sudoku[3][8] = 0 
sudoku[4][0] = 0 
sudoku[4][1] = 5 
sudoku[4][2] = 0 
sudoku[4][3] = 0 
sudoku[4][4] = 0 
sudoku[4][5] = 0 
sudoku[4][6] = 0 
sudoku[4][7] = 4 
sudoku[4][8] = 0 
sudoku[5][0] = 0 
sudoku[5][1] = 0 
sudoku[5][2] = 0 
sudoku[5][3] = 5 
sudoku[5][4] = 2 
sudoku[5][5] = 0 
sudoku[5][6] = 0 
sudoku[5][7] = 0 
sudoku[5][8] = 1 
sudoku[6][0] = 0 
sudoku[6][1] = 4 
sudoku[6][2] = 5 
sudoku[6][3] = 0 
sudoku[6][4] = 0 
sudoku[6][5] = 6 
sudoku[6][6] = 3 
sudoku[6][7] = 0 
sudoku[6][8] = 2 
sudoku[7][0] = 8 
sudoku[7][1] = 0 
sudoku[7][2] = 0 
sudoku[7][3] = 0 
sudoku[7][4] = 0 
sudoku[7][5] = 0 
sudoku[7][6] = 0 
sudoku[7][7] = 0 
sudoku[7][8] = 0 
sudoku[8][0] = 0 
sudoku[8][1] = 2 
sudoku[8][2] = 0 
sudoku[8][3] = 0 
sudoku[8][4] = 0 
sudoku[8][5] = 7 
sudoku[8][6] = 0 
sudoku[8][7] = 0 
sudoku[8][8] = 0

result = {'result': []}
t1 = time.time()
backtrack(0, 0, 9, sudoku, result, False)
t2 = time.time()
print('Result', sudoku, result, t2 - t1)


# iterate(0, 0, 0, matrix)