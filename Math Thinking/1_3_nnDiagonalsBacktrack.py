import copy
import time

def isValid(matrix, i, j, type):

    # print(matrix, i, j, type)
    n = len(matrix)
    if type == 1 :
        if i-1 >= 0 :
            if matrix[i-1][j] == 2 :
                return False
        if j+1 < n :
            if matrix[i][j+1] == 2 :
                return False
        if i-1 >= 0 and j-1 >= 0 :
            if matrix[i-1][j-1] == 1:
                return False
        if i+1 < n :
            if matrix[i+1][j] == 2 :
                return False
        if j-1 >= 0 :
            if matrix[i][j-1] == 2 :
                return False
        if i+1 < n and j+1 < n :
            if matrix[i+1][j+1] == 1 :
                return False
    if type == 2:
        if i-1 >= 0 :
            if matrix[i-1][j] == 1 :
                return False
        if j-1 >= 0 :
            if matrix[i][j-1] == 1 :
                return False
            
        if i-1 >= 0 and j+1 < n :
            if matrix[i-1][j+1] == 2 :
                return False
        
        if i+1 < n :
            if matrix[i+1][j] == 1 :
                return False
        if j+1 < n :
            if matrix[i][j+1] == 1 :
                return False
        if i+1 < n and j-1 >= 0 :
            if matrix[i+1][j-1] == 2 :
                return False
        
    return True

def clearMatrix (matrix, val = -1):

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = val
            #print(i, j)
    return matrix

def count(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1 or matrix[i][j] == 2 :
                count+=1
    # print('count', count)
    return count

def backtrack(i, j, n, matrix, countMap) :
    
    if i >= n :
        tmp = count(matrix)
        print('base case', matrix)
        if countMap['count'] <= tmp :
            if countMap['count'] == tmp :
                countMap['values'].append(copy.deepcopy(matrix))
            else :
                countMap['values'] = copy.deepcopy(matrix)
                countMap['count'] = tmp
        return
    for p in range(3) :
        if isValid(matrix, i, j, p) :
            matrix[i][j] = p
            if j < n-1 :
                backtrack(i, j+1, n, matrix, countMap)
            if j >= n-1 :
                backtrack(i+1, 0, n, matrix, countMap)
        matrix[i][j] = 0
        # print(matrix, p)


n = 5
countMap = {'count': 0, 'values': []}
matrix = [[0 for x in range(n)] for y in range(n)]
clearMatrix(matrix)
t1 = time.time()
backtrack(0, 0, n, matrix, countMap)
t2 = time.time()
print(countMap, t2 - t1)