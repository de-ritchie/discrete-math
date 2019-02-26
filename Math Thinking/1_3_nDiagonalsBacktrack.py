"""

0 0 0   0 0 1   0 0 2   0 1 0   0 1 1   0 1 2   0 2 0   0 2 1   0 2 2
1 0 0   1 0 1   1 0 2   1 1 0   1 1 1   1 1 2   1 2 0   1 2 1   1 2 2


-1 -1
-1 -1

0 0     0 1     0 2     1 0     1 1     2 0     2 2

0 0 0   0 0 1   0 0 2   0 1 0   0 1 1   0 1 2   0 2 0   0 2 1   0 2 2
1 0 0   1 0 1   1 0 2   1 1 0   1 1 1   1 1 2   1 2 0   1 2 1   1 2 2
2 0 0   2 0 1   2 0 2   2 1 0   2 1 1   2 1 2   2 2 0   2 2 1   2 2 2

0 0     0 0     0 0     0 0     0 0     0 0     0 0     0 0     0 0
0 0     0 1     0 2     1 0     1 1     1 2     2 0     2 1     2 2

0 1     0 1     0 1     0 1     0 1     0 1     0 1     0 1     0 1
0 0     0 1     0 2     1 0     1 1     1 2     2 0     2 1     2 2

0 2     0 2     0 2     0 2     0 2     0 2     0 2     0 2     0 2
0 0     0 1     0 2     1 0     1 1     1 2     2 0     2 1     2 2

1 0     1 0     1 0     1 0     1 0     1 0     1 0     1 0     1 0
0 0     0 1     0 2     1 0     1 1     1 2     2 0     2 1     2 2

1 1     1 1     1 1     1 1     1 1     1 1     1 1     1 1     1 1
0 0     0 1     0 2     1 0     1 1     1 2     2 0     2 1     2 2

1 2     1 2     1 2     1 2     1 2     1 2     1 2     1 2     1 2
0 0     0 1     0 2     1 0     1 1     1 2     2 0     2 1     2 2

2 0     2 0     2 0     2 0     2 0     2 0     2 0     2 0     2 0
0 0     0 1     0 2     1 0     1 1     1 2     2 0     2 1     2 2

2 1     2 1     2 1     2 1     2 1     2 1     2 1     2 1     2 1
0 0     0 1     0 2     1 0     1 1     1 2     2 0     2 1     2 2

2 2     2 2     2 2     2 2     2 2     2 2     2 2     2 2     2 2
0 0     0 1     0 2     1 0     1 1     1 2     2 0     2 1     2 2

"""

import copy

def clearMatrix (matrix, n, val):

    for i in range(n):
        for j in range(n):
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

def checkMatrix(matrix) :

    # print('check matrix', matrix)
    for i in range(len(matrix)) :
        for j in range(len(matrix[i])) :
            # print(matrix[i][j])
            if matrix[i][j] == 0 or isValid(matrix, i, j, matrix[i][j]) :
                pass
            else :
                return False
    return True

def permute(perm, i, n, result) :
    
    if i == n :
        print('===', perm)
        if checkMatrix([perm]):
            result.append(copy.deepcopy(perm))
    else :
        perm[i] = 0
        permute(perm, i+1, n, result)
        perm[i] = 1
        permute(perm, i+1, n, result)
        perm[i] = 2
        permute(perm, i+1, n, result)
        
def backtrack(i, n, list, tmp, countMap) :
    
    if i >= n :
        tmpCount = count(tmp)
        if countMap['count'] <= tmpCount :
            if countMap['count'] == tmpCount :
                countMap['values'].append(copy.deepcopy(tmp))
            else :
                countMap['values'] = copy.deepcopy(tmp)
            countMap['count'] = tmpCount
        # print('base case', tmp)
        print('base case', tmp, tmpCount)
        return
    for ele in list :

        # print(i, ele, tmp)
        tmp.append(ele)
        if checkMatrix(tmp) :
            backtrack(i+1, n, list, tmp, countMap)
        tmp.pop()

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
    else:
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

n = 2
matrix = [[0 for x in range(n)] for y in range(n)]
matrix = clearMatrix(matrix, n, -1)
result = []
perm = []

for i in range(n) :
    perm.append(0)

countMap = {'count': 0, 'values': []}
permute(perm, 0, n, result)

backtrack(0, n, result, [], countMap)
# for i in result :
#     for j in result :
#         # print('====', i, j, k)
#         if checkMatrix([i, j]) :
#             tmp = count([i, j])
#             if countMap['count'] <= tmp :
#                 if countMap['count'] == tmp :
#                     countMap['values'].append([i, j])
#                 else :
#                     countMap['values'] = [i, j]
#                     countMap['count'] = tmp

#             print('---====---', [i, j], tmp)

print(matrix, 'count Map', countMap, perm, len(result))
