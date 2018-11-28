#Charles Fee (Naumann)
#Ahmed Elhady (Borowski)
# I pledge my honor that I have abided by the Stevens Honor System
import os.path
def main():
    userInput = ''
    users = loadUsers('musicrecplus.txt')
    print("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):")
    name = input()
    if name not in users:
        prefs = getPreferences(name, users)
        users[name] = prefs
    prefs = users[name]
    while userInput != 'q':
        print("Enter a letter to choose an option:")
        print("e - Enter preferences")
        print("r - Get recommendations")
        print("p - Show most popular artists")
        print("h - How popular is the most popular")
        print("m - Which user has the most likes")
        print("q - Save and quit")
        userInput = input()
        if userInput == 'e':
            users.pop(name)
            prefs = getPreferences(name, users)
            users[name] = prefs
        if userInput == 'r':
            getRecommendations(users[name], prefs, users)
        if userInput == 'p':
            mostPopularArtists(users)
        if userInput == 'h':
            mostLikes(users)
        if userInput == 'm':
            mostUserLikes(users)
        if userInput == 'q':
            saveUserPreferences(name, prefs, users, 'musicrecplus.txt')
            
def loadUsers(fileName):
    ''' Reads in a file of stored users' preferences stored
        in the file 'fileName'.
        Returns a dictionary containing a mapping of user
        names to a list of preferred artists
    '''
    if not os.path.isfile(fileName):
        file = open(fileName, 'w')
        file.close()
    file = open(fileName, 'r')
    userDict = {}
    for line in file:
        # Read and parse a single line
        [userName, bands] = line.strip().split(":")
        bandList = bands.split(",")
        bandList.sort()
        userDict[userName] = bandList
    file.close()
    return userDict

def saveUserPreferences(userName, prefs, userMap, fileName):
    ''' Writes all of the user preferences to the file.
        Returns nothing. '''
    userMap[userName] = prefs
    file = open(fileName, "w")
    for user in userMap:
        toSave = str(user) + ":" + ",".join(userMap[user]) + \
                    "\n"
        file.write(toSave)
    file.close()

def getPreferences(userName, userMap):
    ''' Returns a list of the uesr's preferred artists.

        If the system already knows about the user,
        it gets the preferences out of the userMap
        dictionary and then asks the user if she has
        additional preferences.  If the user is new,
        it simply asks the user for her preferences. '''
    newPref = ""
    prefs = []
    print("Enter an artist that you like (Enter to finish):")
    newPref = input( )
        
    while newPref != "":
        prefs.append(newPref)
        print("Enter an artist that you like (Enter to finish):")
        newPref = input()
        
    # Always keep the lists in sorted order for ease of
    # comparison
    prefs.sort()
    return prefs

'''def getRecommendations(currUser, prefs, users):
    rec = []
    boole = True;
    for i in users:
        inter = []
        if not i.endswith('$') and users[i] != currUser:
            inter = intersect(currUser, users[i])
            if len(inter)>2:
                if boole:
                    rec = dintersect(users[i],currUser)
                    boole = False;
                else:
                    rec += dintersect(rec,dintersect(users[i],currUser))
    if rec == []:
        print("No recommendations available at this time")
    else:
        rec.sort()
        for i in rec:
            print(i)'''

def getRecommendations(currUser, prefs, userMap):
    ''' Gets recommendations for a user (currUser) based
    on the users in userMap (a dictionary)
    and the user's preferences in pref (a list).
    Returns a list of recommended artists.  '''
    bestUser = findBestUser(currUser, prefs, userMap)
    recommendations = dintersect(bestUser, currUser)
    
    for i in recommendations:
        print(i)
    
def findBestUser(currUser, prefs, userMap):
    ''' Find the user whose tastes are closest to the current
    user.  Return the best user's name (a string) '''
    bestUser = None
    bestScore = -1
    for user in userMap:
        score = len(intersect(userMap[user], currUser))
        if score > bestScore and currUser != userMap[user] and not user.endswith('$'):
            bestScore = score
            bestUser = userMap[user]
    return bestUser

def mostPopularArtists(userMap):
    '''Returns the most popular artist or artists'''
    users = userMap.keys()
    pop = {}
    maxlikes = 0
    mostpop = []
    for user in users:
        if not user.endswith('$'):
            for artist in userMap[user]:
                if artist in pop:
                    popularity_count = pop[artist]
                    popularity_count += 1
                    pop[artist] = popularity_count
                else:
                    pop[artist] = 1
    for artist in pop:
        if pop[artist] > maxlikes:
            maxlikes = pop[artist]
    for artist in pop:
        if pop[artist] == maxlikes:
            mostpop += [artist]
    if mostpop == []:
        print("Sorry, no artists found")
    else:
        mostpop.sort()
        for i in mostpop:
            print(i)

def mostLikes(userMap):
    '''Returns the most likes on an artist or artists'''
    users = userMap.keys()
    pop = {}
    maxlikes = 0
    mostpop = []
    for user in users:
        for artist in userMap[user]:
            if artist in pop:
                popularity_count = pop[artist]
                popularity_count += 1
                pop[artist] = popularity_count
            else:
                pop[artist] = 1
    for artist in pop:
        if pop[artist] > maxlikes:
            maxlikes = pop[artist]
    for artist in pop:
        if pop[artist] == maxlikes:
            mostpop += [artist]
    if mostpop == []:
        print("Sorry, no artists found")
    else:
        print(maxlikes)

def mostUserLikes(userMap):
    most = []
    listOfNames = []
    for i in userMap:
        if len(userMap[i]) >= len(most) and not i.endswith('$'):
            most = userMap[i]
            listOfNames += [i]
    if listOfNames == []:
        print("Sorry, no artists found")
    else:
        listOfNames.sort()        
        for i in listOfNames:
            print(i)
        

def intersect(L,M):
    res = []
    i = 0
    j = 0
    while i < len(L) and j< len(M):
        if L[i] == M[j]:
            res+=[L[i]]
            i+=1
            j +=1
        elif L[i] > M[j]:
            j+=1
        else:
            i+=1
    return res
        
def dintersect(L,M):
    if L != None:
        res = list(L)
        i = 0
        j = 0
        while i < len(L) and j< len(M):
            if L[i] == M[j]:
                res.remove(L[i])
                i+=1
                j +=1
            elif L[i] > M[j]:
                j+=1
            else:
                i+=1
        return res
    else:
        return ["No recommendations available at this time"]
if __name__ == "__main__":
    main()
