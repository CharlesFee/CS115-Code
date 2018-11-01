from cs115 import *
board=[['','',''],['','',''],['','','']]
def printBoard(board):
    y=0
    z=0
    for i in board:
        for x in range(len(i)):
            z+=1
            if z<len(i):
                print('   '+'|',end='')
        z=0
        y+=1
        if y<len(board):
            print("\n------------")
