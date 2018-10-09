from cs115 import *
#Charles Fee
def mylen(L):
    if L=="" or L==[]:
        return 0
    else:
        return 1+ mylen(L[1:])
    
def dot(L,K):
    'assume both L and K are lists and multiply L[0]*K[0]...'
    'and add them all up'
    if L==[] or K==[]:
        return 0
    else:
        return L[0]*K[0] + dot(L[1:],K[1:])

def explode(S):
    'since i had to instantiate L once i had to make an inner def'
    L=[None]*mylen(S)
    def innerExplosion(S):
        'starts with the last value and assigns each character to an index'
        'then flip the list'
        if S == '':
            return L[::-1]
        else:
            L[(mylen(S)-1)]=S[0]
            return innerExplosion(S[1:])
        
    if mylen(L)==mylen(S):
        return innerExplosion(S)

def ind(e,L):
    'first checks to see if the first index is equal to e'
    'then keeps slicing until either e equals whatever index or'
    'the list or string has ended'
    if L == [] or L=='':
        return 0
    elif e == L[0]:

        return 0
    else:
        return 1 + ind(e,L[1:])

def removeAll(e,L):
    
    'since i had to instantiate L once i had to make an inner def'
    newL=[None]*mylen(L)
    def innerRemoveAll(L):
        '''starts with the last value and assigns each element to an index
        removing ones that match e'''
        'then flip the list'
        if L == []:
            return newL[::-1]
        elif e==L[0]:
            del newL[(mylen(L)-1)]
            return innerRemoveAll(L[1:])
        else:
            newL[(mylen(L)-1)]=L[0]
            return innerRemoveAll(L[1:])
        
    if mylen(newL)==mylen(L):
        return innerRemoveAll(L)

def myFilter(e,L):
    
    'since i had to instantiate L once i had to make an inner def to be able to slice'
    'and return the editted list'
    newL=[None]*mylen(L)
    def innerFilter(L):
        'starts with the last value and assigns each element to an index'
        'checks if the index is false or true in the function and either keeps or deletes it'
        'then flip the list'
        if L == []:
            return newL[::-1]
        m=e(L[0])
        if m==False:
            del newL[(mylen(L)-1)]
            return innerFilter(L[1:])
        else:
            newL[(mylen(L)-1)]=L[0]
            return innerFilter(L[1:])
        
    if mylen(newL)==mylen(L):
        return innerFilter(L)
        
def deepReverse(L):
    'If you run out of indexes return []'
    if mylen(L) == 0:
        return []
    else:
        'checks if there is a list inside of a list and then reverses that'
        if isinstance(L[0], list):
            return deepReverse(L[1:]) + [deepReverse(L[0][1:])+[L[0][0]]]
        else:
            return deepReverse(L[1:])+[L[0]]
