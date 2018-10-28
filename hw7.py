#Charles Fee
#I pledge my honor that I have abided by the Stevens Honor System
from cs115 import *

def numToBaseB(N, B):
    '''Precondition: integer argument is non-negative.
    Returns the string with the number N converted into whatever base B'''
    def inner(N, B):
        if N==0:
            return ''
        else:
            return inner(N//B,B)+str(N%B)
    if N == 0:
        return '0'
    else:
        return inner(N,B)

def baseBToNum(S, B):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the base B representation in S.
    Note: the empty string represents 0.'''
    biterinos = len(S)
    if S=='':
        return 0
    elif S[0] == '0':
        return baseBToNum(S[1:], B)
    else:
        return ((B**(biterinos-1))*int(S[0])) + baseBToNum(S[1:], B)

def baseToBase(B1,B2,SinB1):
    '''returns the String inputed in base B1 in a string coverted to B2'''
    return numToBaseB(baseBToNum(SinB1,B1),B2)

def add(S, T):
    '''converts to base 10 and then adds and converts back'''
    STen=baseBToNum(S, 2)
    TTen=baseBToNum(T, 2)
    newNum = STen + TTen
    answer = numToBaseB(newNum, 2)
    return answer

def addB(S,T):
    '''first makes the two strings the same length by adding prefix Zeroes
        then proceeds to compare the last index in each string and determines
        if there is going to be a carryover or not. if so it carries that carryover
        to the next addition and creates a new string that in the end is the addition of the two'''
    def inner(s,t,carry,added):
        lastIndex=len(s)-1
        if s=='' and carry == 0:
            return added
        elif s=='' and carry == 1:
            added = '1'+added
            return added
        elif s[lastIndex] == '1' and t[lastIndex] == '1' and carry == 0:
            added='0'+added
            return inner(s[:lastIndex],t[:lastIndex],1,added)
        elif s[lastIndex] == '1' and t[lastIndex] == '1' and carry == 1:
            added='1'+added
            return inner(s[:lastIndex],t[:lastIndex],1,added)
        elif ((s[lastIndex] == '0' and t[lastIndex] == '1') or (s[lastIndex] == '1' and t[lastIndex] == '0')) and carry == 0:
            added = '1'+added
            return inner(s[:lastIndex],t[:lastIndex],0,added)
        elif ((s[lastIndex] == '0' and t[lastIndex] == '1') or (s[lastIndex] == '1' and t[lastIndex] == '0')) and carry == 1:
            added='0'+added
            return inner(s[:lastIndex],t[:lastIndex],1,added)
    if S == '' or T == '':
        print("enter 2 binary strings you lemon not 1")
    elif len(S) > len(T):
        return inner(S,prefixZeroes(T,S),0,'')
    elif len(S) < len(T):
        return inner(prefixZeroes(S,T),T,0,'')
    else:
        return inner(S,T,0,'')
    
def prefixZeroes(x,y):
    '''fills up empty spaces with 0s to get 5 total numbers in each 'chunk' '''
    binary = x
    len_binary = len(binary)
    return ('0'*(len(y)-len_binary)) + binary
