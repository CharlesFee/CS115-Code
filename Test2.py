# Another test

from cs115 import reduce, range

M = range(0,10)

def add(x,y):
    return x+y

def mult(x,y):
    return x*y

def square(x):
    return x*x

def f(L):
    return reduce(add, L)

def fact(N):
    return reduce(mult, range(1,N+1))

def gauss(N):
    return reduce(add, range(1, N+1))
def span(L):
    m = reduce(min, L)
    n = reduce(max, L)

    return n-m

def sumOfSquares(N):
    M=range(1,N+1)
    return reduce(add, map(square, M))
