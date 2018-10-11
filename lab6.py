'''
Created on 10/10/18
@author:   Charles Fee
Pledge:    I pledge my honor that I have abided by the Stevens Honor system.

CS115 - Lab 6
'''
def isOdd(n):
    if n%2==0:
        return False
    else:
        return True

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n==0:
        return ''
    else:
        return numToBinary(n//2)+str(n%2)

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    biterinos = len(s)
    if s=='':
        return 0
    elif s[0] == '0':
        return binaryToNum(s[1:])
    elif s[0] == '1':
        return ((2**(biterinos-1))) + binaryToNum(s[1:])

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if s == '11111111':
        return ('0'*8)
    else:
        baseten = binaryToNum(s)
        increment = baseten
        inc = numToBinary(increment+1)
        lenInc = len(inc)
        return ('0'*(8-lenInc)) + inc

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n<0:
        return
    else:
        print(s)
        count(increment(s),n-1)

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n==0:
        return '' 
    else:
        return numToTernary(n//3)+str(n%3)

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    ternerinos = len(s)
    if s=='':
        return 0
    elif s[0] == '0':
        return ternaryToNum(s[1:])
    elif s[0] == '1' or s[0]=='2':
        return ((3**(ternerinos-1))*int(s[0])) + ternaryToNum(s[1:])
