#Charles Fee
#I pledge my honor that I have abided by the Stevens Honor System
import sys
from cs115 import map, reduce, filter
# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'aaa']
x=-1
# Implement your functions here.

def letterScore(letter, scorelist):
    'takes in the letter and sends it over to my val function to get the value'
    if letter=='':
        return 0
    else:
        return val(letter[0],scrabbleScores)

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

def scoreList(Rack):
    'will take in any list of characters and see how many words you can make from those character'
    x=0
    tempRack= Rack
    rackResetter = []
    Rack3 =[]
    def reset():
        del rackResetter[:]
        return []
    def betterScoreList(Rack1, Dict):
        '''rackResetter was a pain in the butt but it basically will take whatever letter you take out of
        the rack to make a word and then puts it back in when you make a new word'''
        nonlocal x
        nonlocal rackResetter
        if Dict==[]:
            return []
        elif x>(len(Dict[0])-1):
            x=0
            Rack3=Rack1+rackResetter
            reset()
            return [[Dict[0], wordScore(Dict[0], scrabbleScores)]]+betterScoreList(Rack3,Dict[1:])
        elif Dict[0][x] in Rack1:
            Rack1.remove(Dict[0][x])
            rackResetter.append(Dict[0][x])
            x+=1
            return betterScoreList(Rack1,Dict)
        else:
            x=0
            Rack3=Rack1+rackResetter
            reset()
            return betterScoreList(Rack3,Dict[1:])
        
    return betterScoreList(Rack,Dictionary)
def bestWord(Rack):
    '''takes the list of words and finds which one has the highest value'''
    x = 1
    Listerino=scoreList(Rack)
    if Listerino == []:
        return ['',0]
    else:
        highest = Listerino[0]
    
    def compare(highest2):
        nonlocal x
        if x>(len(Listerino)-1):
            return highest2
        elif Listerino[x][1]>highest2[1]:
            highest2=Listerino[x]
            x+=1
            return compare(highest2)
        else:
            x+=1
            return compare(highest2)
    return compare(highest)
