from cs115 import *

def factorial(x):
    fact=1
    if x < 0:
        return "you cannot factorial a negative number (x_x)"
    for i in range(1,x+1):
        fact *= i
    return fact

def mapSqr(L):
    m=[]
    for i in range(len(L)):
        m.append((L[i])**2)
    return m
