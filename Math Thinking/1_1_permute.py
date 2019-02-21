def extend(perm, n):
    if(len(perm) == n):
        print('-----', perm)
    
    for k in range(n):
        if k not in perm:
            perm.append(k)
            #print('b4 ext', perm)
            extend(perm, n)
            #print('a4 ext', perm)
            perm.pop()
            #print('pop', perm)

extend(perm=[], n=4)