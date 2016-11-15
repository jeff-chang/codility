def countOpenBracket(bracketList, midindex):
    count = 0
    for i in range(midindex):
        if bracketList[i] == "(":
            count = count + 1
    return count 

def countCloseBracket(bracketList, midindex):
    count = 0
    for i in range(midindex, len(bracketList)):
        if bracketList[i] == ")":
            count = count + 1
    return count

def solution(S):
    bracketList = list(S)
    bracketListSize = len(bracketList)
    midindex = bracketListSize/2
    while True:
        openBracket = countOpenBracket(bracketList, midindex)
        closeBracket = countCloseBracket(bracketList, midindex)
        if openBracket > closeBracket:
            midindex = midindex - 1
        elif openBracket < closeBracket: 
            midindex = midindex + 1
        else:
            return midindex
