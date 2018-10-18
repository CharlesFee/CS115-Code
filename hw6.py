'''
Created on 10/16/2018
@author:   Charles Fee
Pledge:    I pledge my honor that I have abided by the Stevens Honor System
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
'''**Largest number of bits** The largest number of bits is COMPRESSED_BLOCK_SIZE*64 because if you have alternating 1s
and 0s it results in that as a max'''
'''**Compression** after testing multiple strings I found that the more you had longer blocks of 1s or zeros the better
the compression was i.e compression('10'*32) is worse than compression('0'*64)'''
'''**Laicompress** 64 bit strings have 2^64 different possibilities and when trying to reduce that to a smaller string i.e.
4 bit string it only has 2^4=16 possible combinations meaning that you cannot reduce every possible number ina 64
bit string to a 4 bit string without overlapping'''
def add(x,y):
    return x+y

def compress(S):
    '''Returns the run-length compressed form of a binary string with a length of 64'''
    splittedgroups = splitGroups(S)
    stringtolist = stringToList(splittedgroups)
    size = map(length,stringtolist)
    if '1' in stringtolist[0]:
        size = [0] + size
    if helperino2(size) == True:
        return helperino(size)
    else:
        numtobinary = map(numToBinary,size)
        prefixed = map(prefixZeroes,numtobinary)
        compressedstr = reduce(add,prefixed)
        return compressedstr

def helperino2(size):
    'checks if there are any numbers greater than our max run length'
    if len(size)==0:
        return False
    if size[0] > MAX_RUN_LENGTH:
        return True
    else:
        return helperino2(size[1:])
def helperino(size):
    '''if a number is greater than the max run length then it writes out the
    proper notation'''
    if len(size)==0:
        return ''
    elif size[0] > MAX_RUN_LENGTH:
        num=size[0]//31
        othernum=size[0]%31
        numtobinary = map(numToBinary,[othernum])
        prefixed = map(prefixZeroes,numtobinary)
        compressedstr = reduce(add,prefixed)
        return '1111100000'*num+compressedstr+helperino(size[1:])
    else:
        numtobinary = map(numToBinary,size)
        prefixed = map(prefixZeroes,numtobinary)
        compressedstr = reduce(add,prefixed)
        return compressedstr+'00000'+helperino(size[1:])
        
def length(x):
    return len(x)

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

def splitGroups(s):
    '''Splits s into comma separated groups ie 1110101110001 -> 111,0,1,0,111,000,1'''
    if len(s)==1:
        return s[0]
    else:
        if s[0]==s[1]:
            return s[0]+splitGroups(s[1:])
        else:
            return s[0]+','+splitGroups(s[1:])

def stringToList(i):
    '''takes the comma separated string and makes it into a list'''
    index = ind(',',i)
    if i=='':
        return []
    else:
        return [i[0:index]] + stringToList(i[index+1:])

def ind(pos, L):
    '''determins how long each ',' separation is'''
    if (L==''):
        return 0
    elif (L[0] == pos):
        return 0
    elif (L[0] != pos):
        return (ind(pos,L[1:]) + 1)

def uncompress(s):
    '''Returns the uncompressed form of a compressed binary string'''
    listerino = separate(s)
    tenlist = map(binaryToNum,listerino)
    return convert(tenlist)

def separate(s):
    '''Cuts a string into COMPRESSED_BLOCK_SIZE bit substrings, and puts each substring into a list as an element'''
    if s=='':
        return []
    else:
        return [s[0:COMPRESSED_BLOCK_SIZE]] + separate(s[COMPRESSED_BLOCK_SIZE:])
def prefixZeroes(s):
    '''fills up empty spaces with 0s to get 5 total numbers in each 'chunk' '''
    binary = s
    len_binary = len(binary)
    return ('0'*(COMPRESSED_BLOCK_SIZE-len_binary)) + binary

def compression(s):
    '''Returns the compression ratio of compressed_string:uncompressed_string'''
    return (len(compress(s))*1.0) / (len(s)*1.0)

def convert(L):
    '''Taking a list of decimal numbers that represent the number of 0s and 1s and returns the corresponding/uncompressed string.'''
    if len(L)==1:
        return ('0'*L[0])
    elif len(L)==2:
        return ('0'*L[0]) + ('1'*L[1])
    else:
        return ('0'*L[0])+('1'*L[1])+convert(L[2:])
