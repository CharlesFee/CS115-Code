def intersect(L,M):
    res = []
    i = 0
    j = 0
    while i < len(L) and j< len(M):
        if L[i] == M[j]:
            res+=[L[i]]
            i+=1
            j +=1
        elif L[i] > M[j]:
            j+=1
        else:
            i+=1    
    return res

def coolIntersect(L,M):
    return filter(lambda x: x in M, L)

def ncommon(L,M):
    res = 0
    i = 0
    j = 0
    while i < len(L) and j< len(M):
        if L[i] == M[j]:
            res+=1
            i+=1
            j +=1
        elif L[i] > M[j]:
            j+=1
        else:
            i+=1
    return res


