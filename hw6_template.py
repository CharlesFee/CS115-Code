'''
Created on _______________________
@author:   _______________________
Pledge:    _______________________

CS115 - Hw 6
'''
from cs115 import *
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.
def add(x,y):
    return x+y
def compress(S):
    '''Returns the run-length compressed form of a binary string with a length of 64'''
    splittedgroups = splitGroups(S)
    stringtolist = stringToList(splittedgroups)
    size = map(len(),stringtolist)
    if '1' in stringtolist[0]:
        size = [0] + size
        numtobinary = map(numToBinary,size)
        prefixed = map(prefixZeroes,numtobinary)
        compressedstr = reduce(add,prefixed)
        return compressedstr

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

def splitGroup(s):
    '''Splits s into comma separated groups ie 1110101110001 -> 111,0,1,0,111,000,1'''
    if len(s)==1:
        return s[0]
    else:
        if s[0]==s[1]:
            return s[0]+splitGroup(s[1:])
        else:
            return s[0]+','+splitGroup(s[1:])

def stringToList(i):
    '''takes the comma separated string and makes it into a list'''
    index = ind(',',i)
    if i=='':
        return []
    else:
        return [i[0:index]] + stringToList(i[index+1:])

def ind(i, L):
    '''determins how long each ',' separation is'''
    if (L==''):
        return 0
    elif (L[0] == pos):
        return 0
    elif (L[0] != e):
        return (ind(pos,L[1:]) + 1)

def uncompress(s):
    '''Returns the uncompressed form of a compressed binary string'''
    listerino = separate(s)
    tenlist = map(binaryToNum,list)
    return convert(tenlist)

def separate(s):
'''Cuts a string into COMPRESSED_BLOCK_SIZE bit substrings, and puts each substring into a list as an element'''
    if s=='':
        return []
    else:
        return [s[0:COMPRESSED_BLOCK_SIZE]] + separate(s[COMPRESSED_BLOCK_SIZE:])
