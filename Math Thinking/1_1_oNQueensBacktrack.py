def bound(arr, i, j) :
    # print('bound', arr, i, j)
    for k in range(len(arr)) :
        # print('===', k)
        if abs(k-i) == abs(arr[k] - j) :
            return False
    return True

def backtrack(k, n, res) :
    
    if k >= n :
        print('res', res)
        return

    for i in range(n) :
        if not i in res :
            # print(i)
            boolean = bound(res, len(res), i)
            # print('bool', bool)
            if boolean :
                res.append(i)
                backtrack(k+1, n, res)
                res.pop()

n = 4
backtrack(0, n, [])