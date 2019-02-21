def clearMatrix (matrix, n):

    for i in range(n):
        for j in range(n):
            matrix[i][j] = -1
            #print(i, j)
    return matrix

def isValid(matrix, i, j, type):
    n = len(matrix)
    toggleType = 0
    if type == 1 :
        toggleType = 2
    else:
        toggleType = 1

        
    return True

n = 3
matrix = [[0 for x in range(n)] for y in range(n)]
matrix = clearMatrix(matrix, n)

matrix[1][1] = 1

print(matrix)

print(isValid(matrix, 0, 2, 1))