from cs115 import *
memo = {}
def LCSX(S1, S2):
    if S1 == '' or S2 == '':
        return 0
    elif S1[0] == S2[0]:
        return 1+LCSX(S1[1:], S2[1:])
    else:
        chopS1 = LCSX(S1[1:], S2)
        chopS2 = LCSX(S1, S2[1:])
        answer = max(chopS1, chopS2)
        return answer

def fastLCS(S1, S2):
    if (S1, S2) in memo:
        return memo[(S1, S2)]
    elif S1 =='' or S2 == '':
        memo[(S1, S2)] = 0
        return 0
    elif S1[0] == S2[0]:
        answer = 1 + fastLCS(S1[1:], S2[1:])
        memo[(S1, S2)] = answer #remembers the answer to avoid duplicate recursice calls
        return answer
    else:
        chopS1 = fastLCS(S1[1:], S2)
        chopS2 = fastLCS(S1, S2[1:])
        answer = max(chopS1, chopS2)
        memo[(S1, S2)] = answer #remember
        return answer

def fastLCSalt(S1, S2):
    memo = {}
    def fLCS(S1, S2):
        if (S1, S2) in memo:
            return memo[(S1, S2)]
        elif S1 =='' or S2 == '':
            memo[(S1, S2)] = 0
            return 0
        elif S1[0] == S2[0]:
            answer = 1 + fastLCS(S1[1:], S2[1:])
            memo[(S1, S2)] = answer #remembers the answer to avoid duplicate recursice calls
            return answer
        else:
            chopS1 = fastLCS(S1[1:], S2)
            chopS2 = fastLCS(S1, S2[1:])
            answer = max(chopS1, chopS2)
            memo[(S1, S2)] = answer #remember
            return answer
    return fLCS(S1, S2)

def LCS(S1, S2):
    def iLCS(S1, S2, tabs):
        if S1 == '' or S2== '':
            return 0
        elif S1[0] == S2[0]:
            print(tabs*(' ')+'LCS('+S1[1:]+','+S2[1:]+')')
            tabs+=1
            return 1+ iLCS(S1[1:], S2[1:],tabs)
        else:
            print(tabs*(' ')+'LCS('+S1+','+S2[1:]+')')
            print(tabs*(' ')+'LCS('+S1[1:]+','+S2+')')
            tabs+=1
            return max(iLCS(S1, S2[1:],tabs),iLCS(S1[1:], S2,tabs))

    return iLCS(S1,S2,0)
