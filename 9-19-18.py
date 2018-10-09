from cs115 import *

def knapsack(capacity, L):
    '''if L==[] or capacity <= 0:
        return 0
    elif L[0][0] > target:
        return knapsack(capacity, L[1:])
    else:
        lose = knapsack(capacity, L[1:])
        use = knapsack(capacity - L[0][0], L[1:])'''
    return "incomplete you fool"

def coinNames(coinInfo):
    '''assume coinInfo is a non-empty list of pairs [value,name].
    Return the names, as a string. For example,
    coinNames([[1, 'penny'],[5, 'nickel']]
    Returns penny nickel'''
    return reduce(lambda st1, st2: st1 + ' ' + st2,
                  map(lambda pair: pair[1], coinInfo))
def exp(n,k):
    '''n**k'''
    if k== 0:
        return 1
    else:
        return n*exp(n,k-1)
def expfast(n,k):
    if k == 0:
        return 1
    elif k%2==0:
        t= expfast(n, k//2)
        return t*t
    else:
        return n* expfast(n,k-1)

def exptail(n, k):
    def ext(accumulator, n, k):
        if k == 0:
            return accumulator
        else:
            return ext(n * accumulator, n, k-1)
    return ext(1, n, k)

def reverse(L):
    if L== []:
        return []
    else:
        return reverse(L[1:])+[L[0]]

def reverse2(L):
    def rev(acc, L):
        if L == []:
            return acc
        else:
            return rev(acc.insert(0,L[0]),L[1:])



    return rev([[]],L)







