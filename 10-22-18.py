# two-part exercise

from cs115 import map

'''
Part 0
Here is a memoized version of edit distance.
Your task: make it trace the calls to fastED_help, indented
according to recursion depth.  Hint: add a parameter to fastED_help.
'''
def fastED(first, second):
    '''Returns the edit distance between the strings first and second. Uses
    memoization to speed up the process.'''
    def fastED_help(first, second, memo, tabs):
        if (first, second) in memo:
            return memo[(first, second)]
        elif first == '':
            result = len(second)
        elif second == '':
            result = len(first)
        elif first[0] == second[0]:
            print(tabs*(' ')+'fastED_help('+first[1:]+','+second[1:]+')')
            tabs+=1
            result = fastED_help(first[1:], second[1:], memo, tabs)
        else:
            print(tabs*(' ')+'fastED_help('+first[1:]+','+second[1:]+')')
            print(tabs*(' ')+'fastED_help('+first[1:]+','+second+')')
            print(tabs*(' ')+'fastED_help('+first+','+second[1:]+')')
            tabs+=1
            substitution = 1 + fastED_help(first[1:], second[1:], memo, tabs)
            deletion = 1 + fastED_help(first[1:], second, memo, tabs)
            insertion = 1 + fastED_help(first, second[1:], memo, tabs)
            result = min(substitution, deletion, insertion)
        memo[(first, second)] = result
        return result    
    return fastED_help(first, second, {}, 0)



'''
Part 1
Complete the following function.  You may use the functions
numToBinary and increment from lab 6, provided below.
Start by sketching your design in psuedo-code.
'''

def numToTC(N):
    '''Assume N is an integer.
    If N can be represented in 8 bits using two's complement, return
    that representation as a string of exactly 8 bits.  
    Otherwise return the string 'Error'.
    '''
    if N >= 128 or N < -128:
        return 'Error'
    elif N < 128 and N >= 0:
        b = numToBinary(N)
        return prefixZeroes(b)
    else:
        b = numToBinary(-N)
        b8 = prefixZeroes(b)
        flipped = helperino(b8)
        print(flipped)
        added = add(flipped,'1')
        return added
'''
Examples:
   NumToTc(1) ---> '00000001'
   NumToTc(-128) ---> '10000000'
   NumToTc(200) ---> 'Error'
'''
def add(S, T):
    '''converts to base 10 and then adds and converts back'''
    STen=baseBToNum(S, 2)
    TTen=baseBToNum(T, 2)
    newNum = STen + TTen
    answer = numToBaseB(newNum, 2)
    return answer

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
def helperino(x):
    def inhelperino(x,newx):
        if x == '':
            return newx
        elif x[0]=='0':
            newx+='1'
            return inhelperino(x[1:],newx)
        else:
            newx+='0'
            return inhelperino(x[1:],newx)
    return inhelperino(x,'')  
def prefixZeroes(s):
    '''fills up empty spaces with 0s to get 5 total numbers in each 'chunk' '''
    binary = s
    len_binary = len(binary)
    return ('0'*(8-len_binary)) + binary

def numToBinary(N):
    '''Assuming N is a non-negative integer, return its base 2
    representation as a string of bits.'''
    if N == 0:
        return ''
    if isOdd(N):
        return numToBinary(N//2) + '1'
    else:
        return numToBinary(N//2) + '0'

def increment(s):
    '''Assuming s is a string of 8 bits, return the binary representation 
    of the next larger number takes an 8 bit string of 1's and 0's and 
    returns the next largest number in base 2'''
    num = binaryToNum(s) + 1
    if num == 256:
        return '00000000'
    zeros = (len(s)-len(numToBinary(num))) * '0'
    return zeros + numToBinary(num)

def binaryToNum(s):
    '''Assuming s is a string of bits, interpret it as an unsigned binary
    number and return that number (as a python integer).
    '''
    def binaryToNumHelp(s, index):
        if s == '':
            return 0
        elif s[0] == '0':
            index -= 1
            return 0 + binaryToNumHelp(s[1:], index)
        else:
            index -= 1
            return 2**index + binaryToNumHelp(s[1:], index)
    return binaryToNumHelp(s, len(s))

def isOdd(n):
    '''returns whether a number is odd or not'''
    if n % 2 == 0:
        return False
    else:
        return True
