#Charles Fee
#I pledge my honor that I have abided by the Stevens Honor System
# nim template DNaumann (2018), for assignment nim_hw11.txt 

# Global variables used by several functions
piles = []         # list containing the current pile amounts
num_piles = 0      # number of piles, which should equal len(pile)


def play_nim():
    """ plays game of nim between user and computer; computer plays optimally """
    
    init_piles()
    display_piles()
    while True:
        user_plays()
        display_piles()
        if sum(piles) == 0:

            print("I let you win this time...")

            break
        computer_plays()
        display_piles()
        if sum(piles) == 0:

            print("HAHAHAHAHA Lemons like you can never defeat me!!!")

            break


def init_piles():
    """ Assign initial values to the global variables 'num_piles' and
        'piles'
        User chooses number of piles and initial size of each pile.
        Keep prompting until they enter valid values."""
    global piles
    global num_piles
    
    print("How many piles do you want to play with?")
    num_piles = int(input())
    piles = []
    while len(piles) != num_piles:
        piles.append(0)
        piles[len(piles)-1] = int(input("How many in pile "+str((len(piles)-1))+"? "))
        
def display_piles():
    """ display current amount in each pile """
    global piles
    global num_piles
    y = 0
    for x in piles:
        print('pile '+str(y)+' = '+str(x))
        y+=1;


def user_plays():
    """ get user's choices and update chosen pile """
    global piles
    
    print("Your turn ...")
    p = get_pile()
    amt = get_number(p)
    piles[p] = piles[p] - amt


def get_pile():
    """ return user's choice of pile
        Keep prompting until the choice is valid, i.e.,
        in the range 0 to num_piles - 1. """
    global piles
    global num_piles

    while True:
        userInput = int(input("Which pile? "))
        if userInput >= 0 and userInput <= num_piles-1:
            return userInput
            break


def get_number(pnum):
    """ return user's choice of how many to remove from pile 'pnum'
        Keep prompting until the amount is valid, i.e., at least 1
        and at most the amount in the pile."""
    global piles
    
    while True:
        userInput = int(input("How many? "))
        if userInput >= 1 and userInput <= piles[pnum]:
            return userInput
            break

def game_nim_sum():
    """ return the nim-sum of the piles """
    global piles
    global num_piles 
    nim_sum = 0
    for x in piles:
        nim_sum = nim_sum^x
    
    return nim_sum

def opt_play():
    """ Return (p,n) where p is the pile number and n is the amt to
        remove, if there is an optimal play.  Otherwise, (p,1) where
        is the pile number of a non-zero pile.

        Implement this using game_nim_sum() and following instructions
        in the homework text."""
    global piles
    global num_piles 
    nim_sum = game_nim_sum()
    pile_sum = list(piles)
    for x in range(len(piles)):
        pile_sum[x] = nim_sum^piles[x]
        
    for y in range(len(piles)):
        if pile_sum[y] < piles[y]:
            return (y, piles[y]-pile_sum[y])

    for z in range(len(piles)):
        if piles[z] != 0:
            return (z,1)


def computer_plays():
    """ compute optimal play, update chosen pile, and tell user what was played

        Implement this using opt_play(). """
    global piles
    global num_piles

    print('Your move was MEDIOCRE at best MY TURN!!!!')
    opt = opt_play()
    print('I shall remove '+str(opt[1])+' from pile '+str(opt[0]))
    piles[opt[0]] -= opt[1]

    


#   start playing automatically
if __name__ == "__main__" : play_nim()
