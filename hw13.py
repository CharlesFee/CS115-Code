#Charles Fee
#I pledge my honor that I have abided by the Stevens Honor System
from cs115 import *
from math import *


class Board():
    def __init__(self, width = 7, height = 6):
        self.height = height
        self.width = width
        self.A = []
        for row in range(self.height):
            self.A+=[self.createOneRow(self.width)]

    def createOneRow(self, width):
        """Returns one row of spaces of width "width"""
        row = []
        for col in range(width):
            row += [' ']
        return row

    def __str__(self):
        stringerino = ''
        counter = 0
        for row in self.A:
            stringerino += '|'
            for col in self.A[counter]:
                stringerino += str(col)+'|'
            stringerino += '\n'
            counter += 1
        stringerino +='--'*self.width+'-'+'\n'
        for num in range(self.width):
            stringerino+=' '+str(num)
        return stringerino
    
    def allowsMove(self, col):
        l = range(self.height)
        l.reverse()
        for row in l:
            if col < self.width and self.A[row][col] == ' ':
                return True
        return False

    def whichRow(self, col):
        l = range(self.height)
        l.reverse()
        for row in l:
            if col < self.width and self.A[row][col] == ' ':
                return row

    def addMove(self, col, ox):
        if self.allowsMove(col):
            if ox == 'X':
                self.A[self.whichRow(col)][col] = 'X'
            else:
                self.A[self.whichRow(col)][col] = 'O'
        else:
            return False
    def delMove(self, col):
        if self.whichRow(col)+1< self.height:
            self.A[self.whichRow(col)+1][col] = ' '
    def winsFor(self, ox):
        'Check Vert'
        for y in range(self.height):
            for x in range(self.width):
                if y+3 < self.height and self.A[y][x] == ox and self.A[y+1][x] == ox and self.A[y+2][x] == ox and self.A[y+3][x] == ox:
                    return True

        'Check Horiz'
        for x in range(self.width):
            for y in range(self.height):
                if x+3 < self.width and self.A[y][x] == ox and self.A[y][x+1] == ox and self.A[y][x+2] == ox and self.A[y][x+3] == ox:
                    return True

        'Check \ diagonal'
        for x in range(self.width):
            for y in range(self.height):
                if y+3 < self.height and x-3 >= 0 and self.A[y][x] == ox and self.A[y+1][x-1] == ox and self.A[y+2][x-2] == ox and self.A[y+3][x-3] == ox:
                    return True

        'Check / diagonal'
        for x in range(self.width):
            for y in range(self.height):
                if y+3 < self.height and x+3 < self.width and self.A[y][x] == ox and self.A[y+1][x+1] == ox and self.A[y+2][x+2] == ox and self.A[y+3][x+3] == ox:
                    return True

        return False
    def setBoard( self, moveString ):
        """ takes in a string of columns and places
        alternating checkers in those columns,
        starting with 'X'

        For example, call b.setBoard('012345')
        to see 'X's and 'O's alternate on the
        bottom row, or b.setBoard('000000') to
        see them alternate in the left column.
        moveString must be a string of integers
        """
        nextCh = 'X' # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'

    def hostGame(self):
        userInput = ''
        ox = 'X'
        print('Welcome to Connect Four!')
        while True:
            print(self)
            validMove = False
            while validMove == False:
                try:
                    userInput = int(input(ox+"'s choice:  "))
                    if self.addMove(userInput, ox) != False:
                        validMove = True
                except ValueError:
                    validMove == False
            if self.winsFor(ox):
                break
            if ox == 'X':
                ox = 'O'
            else:
                ox = 'X'
        print(ox+' wins -- Congratulations!')
        print(self)
