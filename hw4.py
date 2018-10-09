from cs115 import *
#Charles Fee
#I pledge my honor that I have abided by the Stevens Honor System
def pascal_row(n):
    '''basically the inner function is a for loop that adds the selected element
    and the element after it to get the desired row'''
    x=0
    def inner(currentLine, lastLine, x):
        if x in range(len(lastLine)-1):
            currentLine.append(lastLine[x] + lastLine[x+1])
            x+=1
            return inner(currentLine, lastLine, x)
        else:
            currentLine += [1]
            return currentLine
        
    if n == 0:
        return [1]
    else:
        currentLine = [1]
        lastLine = pascal_row(n-1)
        return inner(currentLine,lastLine,x)

def pascal_triangle(n):
    '''basically the inner function is a for loop that adds the selected element
    and the element after it to get the desired row and then does that for the
    previous row until there are no more previous rows'''
    
    x=0
    def inner(currentLine, lastLine, x):
        if x in range(len(lastLine)-1):
            currentLine.append(lastLine[x] + lastLine[x+1])
            x+=1
            return inner(currentLine, lastLine, x)
        else:
            currentLine += [1]
            return pascal_triangle(n-1)+[currentLine]
        
    if n == 0:
        return [[1]]
    else:
        currentLine = [1]
        lastLine = pascal_row(n-1)
        return inner(currentLine,lastLine,x)

def test_pascal_row():
    assert pascal_row(5)==[1, 5, 10, 10, 5, 1]
    assert pascal_row(10)==[1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]
    assert pascal_row(19)==[1, 19, 171, 969, 3876, 11628, 27132, 50388, 75582, 92378, 92378, 75582, 50388, 27132, 11628, 3876, 969, 171, 19, 1]
    assert pascal_row(100)==[1, 100, 4950, 161700, 3921225, 75287520, 1192052400, 16007560800, 186087894300, 1902231808400, 17310309456440, 141629804643600, 1050421051106700, 7110542499799200, 44186942677323600, 253338471349988640, 1345860629046814650, 6650134872937201800, 30664510802988208300, 132341572939212267400, 535983370403809682970, 2041841411062132125600, 7332066885177656269200, 24865270306254660391200, 79776075565900368755100, 242519269720337121015504, 699574816500972464467800, 1917353200780443050763600, 4998813702034726525205100, 12410847811948286545336800, 29372339821610944823963760, 66324638306863423796047200, 143012501349174257560226775, 294692427022540894366527900, 580717429720889409486981450, 1095067153187962886461165020, 1977204582144932989443770175, 3420029547493938143902737600, 5670048986634686922786117600, 9013924030034630492634340800, 13746234145802811501267369720, 20116440213369968050635175200, 28258808871162574166368460400, 38116532895986727945334202400, 49378235797073715747364762200, 61448471214136179596720592960, 73470998190814997343905056800, 84413487283064039501507937600, 93206558875049876949581681100, 98913082887808032681188722800, 100891344545564193334812497256, 98913082887808032681188722800, 93206558875049876949581681100, 84413487283064039501507937600, 73470998190814997343905056800, 61448471214136179596720592960, 49378235797073715747364762200, 38116532895986727945334202400, 28258808871162574166368460400, 20116440213369968050635175200, 13746234145802811501267369720, 9013924030034630492634340800, 5670048986634686922786117600, 3420029547493938143902737600, 1977204582144932989443770175, 1095067153187962886461165020, 580717429720889409486981450, 294692427022540894366527900, 143012501349174257560226775, 66324638306863423796047200, 29372339821610944823963760, 12410847811948286545336800, 4998813702034726525205100, 1917353200780443050763600, 699574816500972464467800, 242519269720337121015504, 79776075565900368755100, 24865270306254660391200, 7332066885177656269200, 2041841411062132125600, 535983370403809682970, 132341572939212267400, 30664510802988208300, 6650134872937201800, 1345860629046814650, 253338471349988640, 44186942677323600, 7110542499799200, 1050421051106700, 141629804643600, 17310309456440, 1902231808400, 186087894300, 16007560800, 1192052400, 75287520, 3921225, 161700, 4950, 100, 1]

def test_pascal_triangle():
    assert pascal_triangle(5)==[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    assert pascal_triangle(10)==[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1], [1, 9, 36, 84, 126, 126, 84, 36, 9, 1], [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]]
    assert pascal_triangle(19)==[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1], [1, 9, 36, 84, 126, 126, 84, 36, 9, 1], [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1], [1, 11, 55, 165, 330, 462, 462, 330, 165, 55, 11, 1], [1, 12, 66, 220, 495, 792, 924, 792, 495, 220, 66, 12, 1], [1, 13, 78, 286, 715, 1287, 1716, 1716, 1287, 715, 286, 78, 13, 1], [1, 14, 91, 364, 1001, 2002, 3003, 3432, 3003, 2002, 1001, 364, 91, 14, 1], [1, 15, 105, 455, 1365, 3003, 5005, 6435, 6435, 5005, 3003, 1365, 455, 105, 15, 1], [1, 16, 120, 560, 1820, 4368, 8008, 11440, 12870, 11440, 8008, 4368, 1820, 560, 120, 16, 1], [1, 17, 136, 680, 2380, 6188, 12376, 19448, 24310, 24310, 19448, 12376, 6188, 2380, 680, 136, 17, 1], [1, 18, 153, 816, 3060, 8568, 18564, 31824, 43758, 48620, 43758, 31824, 18564, 8568, 3060, 816, 153, 18, 1], [1, 19, 171, 969, 3876, 11628, 27132, 50388, 75582, 92378, 92378, 75582, 50388, 27132, 11628, 3876, 969, 171, 19, 1]]
    assert pascal_triangle(7)==[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1]]