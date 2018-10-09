from cs115 import *

def div(k):
        
    return n % k == 0


def divides(n):
    'checks if there is a remainder'
    def div(k):
        
        return n % k == 0
    
    return div

def divisibles(n,L):
    'assume L is a list of integers; return a list of the one divisible by n'
    if L==[]:
        return []
    else:
        if divides(L[0])(n):
            return [L[0]] + divisibles(n, L[1:])
        else:
            return divisibles(n,L[1:])
        
def make_len(n):
    
    def pad_it(word): 
        x = len(word)
        return word + ((n-x)*'*')
    
    return pad_it
def pad(words):
    'Assume words is a non-empty list of strings. Let n be the'
    'length of the longest. Write * after the shorter to make them the same length'
    m= max(map(len,words))
    return map(make_len(m), words)
