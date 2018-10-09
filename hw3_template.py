'''
Created on _______________________
@author:   _______________________
Pledge:    _______________________

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from cs115 import*
from itertools import *

def giveChange(amount, coins):
    if amount == 0:
        return [0,[]]
    elif coins == []:
        return [float("inf"),[]]
    elif coins[0] > amount:
        return giveChange(amount, coins[1:])
    else:
        loseIt = giveChange(amount, coins[1:])
        useIt = giveChange(amount - coins[0], coins)
        useIt = [1+useIt[0],[coins[0]]+useIt[1]]
        return min(useIt,loseIt)
# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def val(whateverLetter,score):
    'can take a letter and then compute what its scrabble score is'
    if score == []:
        return 'Enter a valid character you lemon'
    if whateverLetter == score[0][0]:
        return score[0][1]
    else:
        return val(whateverLetter,score[1:])

def wordScore(letters, scorelist):
    'Takes in words and goes 1 by 1 adding up the scrabble scores for each letter'
    if letters=='':
        return 0
    else:
        return val(letters[0],scorelist)+wordScore(letters[1:], scorelist)
    
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    if dct == []:
        return []
    else:
        return [[dct[0],wordScore(dct[0],scores)]]+wordsWithScore(dct[1:], scores)
    



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n]. newL is declared above'''
    newL = []
    def inner(n2, L2):
        if len(newL) == n2:
            return newL
        else:
            newL.append(L2[0])
            return inner(n2, L2[1:])
    if len(L) <= n:
        return L
    elif abs(n) >= len(L):
        return []
    elif n < 0:
        d = len(L)+n
        return inner(d,L)
    else:
        return inner(n, L)



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:].'''
    newL = []
    def inner(n2, L2):
        if len(newL) == n2:
            return L2
        else:
            newL.append(L2[0])
            return inner(n2, L2[1:])
    if len(L) <= n:
        return []
    elif abs(n) >= len(L):
        return L
    elif n < 0:
        d = len(L)+n
        return inner(d, L)
    else:
        return inner(n, L)

