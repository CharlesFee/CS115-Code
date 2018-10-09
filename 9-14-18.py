from cs115 import *

def add(x,y):
    return x+y

def myreduce(op, L):
    
    if L == []:
        return None
    elif len(L) ==1:
        return L[0]
    else:
        return op(L[0], myreduce(op,L[1:]))
    
def sieve(L):
    if L == []: return []
    else: return [L[0]] + sieve( filter(lambda x: x%L[0]!=0,L[1:]))

def primes(n):

    return sieve(range(2,n+1))
