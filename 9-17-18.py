#powerset exercise
from cs115 import *

def powerset(L):
    'Create a bunch of sub lists from one master list'
    if L == []:
        return [[]]
    else:
        lose = powerset(L[1:])
        use = map(lambda M:[L[0]] + M, lose)
        return lose+use
def isSubset(L,M):

    if L == []:
        return True
    else:
        return L[0] in M and isSubset(L[1:], M)
    
def subset(target, L):
    if target == 0:
        return True
    elif L == []:
        return False
    elif L[0] > target:
        return subset(target, L[1:])
    else:
        lose = subset(target, L[1:])
        use = subset(target - L[0], L[1:])
        return use or lose
        
