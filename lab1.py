from cs115 import *
import math
def inverse(n):
    '''returns the reciprocal'''
    return 1/n

def add(x,y):
    '''adds 2 inputted variables'''
    return x+y

def divideByFact(x):
    '''divides 1 by the inputted variales factorial'''
    return 1/math.factorial(x)

def e(n):
    '''uses a taylor series to approximate e'''
    '''n is how many terms there are in the series'''
    M = range(1,n+1)
    return reduce(add,map(divideByFact, M))+1

def error(n):
    '''finds the error in the approximation'''
    M = range(1,n+1)
    myE=e(n)
    return abs(math.e - myE)
