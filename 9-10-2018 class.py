def f(x):
    x = x-1
    return g(x)+1

def g(x):
    return x*2

def h(x):
    if x%2 == 1:
        return f(x) + x
    else:
        return f(f(x))

def fact(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
def tower(n):
    if n == 0:
        return 1
    else:
        return 2**tower(n-1)

def mylen(L):
    if L==[]:
        return 0
    else:
        return 1+ mylen(L[1:])

def mysum(L):
    if L==[]:
        return 0
    else:
        return L[0] + mysum(L[1:])
