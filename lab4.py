#Charles Fee
#I pledge my honor that I have abided by the Stevens Honor System
from cs115 import*

def knapsack(capacity, itemlist):
    if capacity == 0:
        return [0,[]]
    elif itemlist == []:
        return [0,[]]
    elif itemlist[0][0] > capacity:
        return knapsack(capacity, itemlist[1:])
    else:
        loseIt = knapsack(capacity, itemlist[1:])
        useIt = knapsack(capacity - itemlist[0][0], itemlist[1:])
        useIt = [itemlist[0][1]+useIt[0],[itemlist[0]]+useIt[1]]
        return max(useIt,loseIt)
