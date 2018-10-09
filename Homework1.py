from cs115 import *
import math

def mult(x,y):
    'multiplies the two parameters'
    return x*y

def add(x,y):
    'adds the two parameters'
    return x+y

def factorial(n):
    if n < 0:
        return 'You can not get the factorial of a negative silly goose'
    if n==0:
        '0 will kick back an error in the other'
        return 1
    else:
        'makes the input a list starting from 1 to n and then multiplies to get fact'
        return reduce(mult, range(1,n+1))

def mean(L):
    'adds all of the values and then divides by the number of them'
    return reduce(add, L)/len(L)

def divides(n):
    'checks if there is a remainder'
    def div(k):
        
        return n % k == 0
    
    return div

def prime(n):
    'maps the list seeing if n divides by integers going to the sqrt of n then'
    'adds them together if all are false then it is prime'
    return reduce(add, map(divides(n),range(2,math.sqrt(n)))) == 0
