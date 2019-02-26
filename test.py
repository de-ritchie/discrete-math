import copy
def clearMatrix (matrix, n):

    for i in range(n):
        for j in range(n):
            matrix[i][j] = -1
            #print(i, j)
    return matrix

def isValid(matrix, i, j, type):
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

def count(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1 or matrix[i][j] == 2 :
                count+=1
    print('count', count)
    return count

def checkMatrix(matrix) :
    for i in range(len(matrix)) :
        for j in range(len(matrix[i])) :
            # print(matrix[i][j])
            if matrix[i][j] == 0 or isValid(matrix, i, j, matrix[i][j]) :
                pass
            else :
                return False
    return True

def permute(matrix, i, j, m, n, countMap) :
    
    # print(i, j)
    for p in range(3):
        if i >= n-1 and j >= n-1 :
            matrix[i][j] = p
            # print('base case', i, j, matrix)
            if checkMatrix(matrix):
                # print('Done', matrix)
                tmp = count(matrix)
                if countMap['count'] <= tmp :
                    if countMap['count'] == tmp :
                        countMap['values'].append(copy.deepcopy(matrix))
                    else :
                        countMap['values'] = [copy.deepcopy(matrix)]
                    countMap['count'] = tmp

        if i < n and j < n-1 :
            matrix[i][j] = p
            permute(matrix, i, j+1, m, n, countMap)

        if i < n-1 and j >= n-1 :
            matrix[i][j] = p
            permute(matrix, i+1, 0, m, n, countMap)

n = 5
matrix = [[0 for x in range(n)] for y in range(n)]
matrix = clearMatrix(matrix, n)
countMap = {'count': 0, 'values': []}
# permute(matrix, 0, 0, n, n, countMap)
print('result', countMap)
permuMap = {}
permuMap['asdads'] = 'asdasd'
print(permuMap.get('asds'))