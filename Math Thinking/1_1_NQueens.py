import itertools as it
import time

def is_solution(perm):
    
    for(i1, i2) in it.combinations(range(len(perm)), 2):
        #print(i1, i2)
        if abs(i1 - i2) == abs(perm[i1] - perm[i2]):
            return False
    return True

#print(is_solution([3, 1, 0, 2]))
startTime = time.time()
for perm in it.permutations(range(10)):
    #print(perm)
    if is_solution(perm):
        print(perm)
    #exit()
print(time.time() - startTime)