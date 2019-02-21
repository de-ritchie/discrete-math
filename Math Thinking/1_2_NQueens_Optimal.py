import time
def can_be_extended(perm):
    i = len(perm) - 1
    for j in range(i):
        if abs(i-j) == abs(perm[i] - perm[j]):
            return False
    return True

def extend(perm, n, result):
    if(len(perm) == n):
        result.append(perm)
        print('-----', perm)
    
    for k in range(n):
        if k not in perm:
            perm.append(k)
            #print('b4 ext', perm)
            if can_be_extended(perm):
                extend(perm, n, result)
            #print('a4 ext', perm)
            perm.pop()
            #print('pop', perm)

startTime = time.time()
result=[]
extend(perm=[], n=8, result=result)
print(time.time() - startTime, len(result))