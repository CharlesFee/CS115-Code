#
# life.py - Game of Life lab
#
# Name:Charles Fee
# Pledge:I pledge my honor that I have abided by the Stevens Honor System
#

import random
import sys

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    "creates a new board with the given dimensions"

    A = []

    for row in range(height):
        A+=[createOneRow(width)]

    return A
def printBoard( A ):
    """ this function prints the 2d list-of-  lists
        A without spaces (using sys.stdout.write)"""
    
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )

def diagonalize(width,height):
    """ creates an empty board and then modifies it
        so that it has a diagonal strip of "on" cells."""
    A = createBoard( width, height )
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def innerCells(width,height):
    "creates a border of zeroes and makes the inside 1s"
    A= createBoard(width,height)
    for row in range(height):
        if row!= 0 and row != height-1:
            for col in range(width):
                if col !=0 and col != width-1:
                    A[row][col]=1
                else:
                    A[row][col]=0
    return A

def randomCells(width,height):
    "creates a border of zeroes and makes the inside 1s"
    A= createBoard(width,height)
    for row in range(height):
        if row!= 0 and row != height-1:
            for col in range(width):
                if col !=0 and col != width-1:
                    A[row][col]=random.choice([0,1])
                else:
                    A[row][col]=0
    return A

def copy(A):
    height = len(A)
    width = len(A[0])
    newA = createBoard(len(A[0]),len(A))
    for row in range(height):
        for col in range(width):
            if A[row][col] != newA[row][col]:
                newA[row][col] = 1
    return newA
        

def innerReverse(A):
    newA=copy(A)
    height = len(newA)
    width = len(newA[0])
    for row in range(height):
        if row!= 0 and row != height-1:
            for col in range(width):
                if col !=0 and col != width-1:
                    if newA[row][col] == 0:
                        newA[row][col]=1
                    else:
                        newA[row][col]=0
    return newA

def next_life_generation(A):
    """makes a copy of A and
    then advances 1 generation
    in Conway's game of life"""
    newA = copy(A)
    height = len(newA)
    width = len(newA[0])
    for row in range(1,height):
        for col in range(1,width):
            if countNeighbors(row,col,A) < 2:
                newA[row][col] = 0
            elif countNeighbors(row,col,A) == 3:
                newA[row][col] = 1
            elif countNeighbors(row,col,A) > 3:
                newA[row][col] = 0
    return newA
def countNeighbors(row, col, A):
    if A[row][col] == 1:
        i=-1
    else:
        i=0
    if row >= 1 and row < (len(A)-1) and col >=1 and col < (len(A[0])-1):
        for r in range(row-1,row+2):
            for c in range(col-1,col+2):
                if A[r][c]==1:
                    i+=1
    else:
        return 0
    return i
