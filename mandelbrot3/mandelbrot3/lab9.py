#Charles Fee
#I pledge my honor that I have abided by the Stevens Honor System

from cs115 import *
from cs5png import *

def mult(c, n):
    '''multiply using loops and only addition'''
    result = 0
    if isinstance(n, int):
        for x in range(n):
            result = result + c
    else:
        for x in range(c):
            result = result + n
    return result

def update(c, n):
    """update starts with z=0 and runs z = z**2 + c
    for a total of n times. It returns the final z."""
    z=0
    for x in range(n):
        z= z**2+c
    return z
    
def inMSet(c, n):
    '''same as update but is used to check if numbers are imaginary or not
    up to a certain point'''
    z=0
    for x in range(n):
        z= z**2+c
        if abs(z)>2:
            return False
    return True

def weWantThisPixel( col, row ):
    """ a function that returns True if we want
    the pixel at col, row and False otherwise"""
    if col%10 == 0  or  row%10 == 0:
        '''when changed to or it makes lines instead of points'''
        return True
    else:
        return False

def test():     
    """ a function to demonstrate how         
    to create and save a png image"""

    width = 300
    height = 200
    image = PNGImage(width, height)

    # create a loop in order to draw some pixels

    for col in range(width):
        for row in range(height):
            if weWantThisPixel( col, row ) == True:
                image.plotPoint(col, row)
				
    # we looped through every image pixel; we now write the file     
    image.saveFile()

def scale(pix, pixMax, floatMin, floatMax):
    """ scale takes in
    pix, the CURRENT pixel column (or row)
    pixMax, the total # of pixel columns
    floatMin, the min floating-point value
    floatMax, the max floating-point value
    scale returns the floating-point value that
    corresponds to pix     """
    ratio = pix/pixMax
    difference = floatMax - floatMin
    adder= difference*ratio
    answer=floatMin+adder
    return answer

def mset(width, height):
    image = PNGImage(width, height)
    
    for col in range(width):
        for row in range(height):
            x=scale(col,width,-2.0,1.0)
            y=scale(row,height,-1.0,1.0)
            c=x+y*1j
            if inMSet(c, 25) == True:
                image.plotPoint(col, row)
    image.saveFile()
