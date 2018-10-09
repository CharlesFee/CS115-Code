#Charles Fee
from cs115 import *
from math import *

def change(amount, coins):
    if amount == 0:
        return 0
    elif coins == []:
        return float("inf")
    elif coins[0] > amount:
        return change(amount, coins[1:])
    else:
        loseIt = change(amount, coins[1:])
        useIt = 1+change(amount - coins[0], coins)
        return min(useIt, loseIt)
