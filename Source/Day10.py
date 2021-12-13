import statistics
from collections import Counter

def print_count(countValue):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Total Count: {countValue}')  # Press Ctrl+F8 to toggle the breakpoint.

def split(word):
    return [char for char in word]

def IsValidIndex( listToCheck:list, index):
    if 0 <= index < len(listToCheck):
        return True
    return False

def GetCharacterCount(char, wordList):
    charCount = 0
    for word in wordList:
        count = Counter(word)
        if count[char] > 0:
            charCount += 1
    return charCount

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    illegalParen = 0
    illegalBracket = 0
    illegalAngle = 0
    illegalCurly = 0
    for fileLine in fileData:
        charList = split(fileLine.strip())
        lineStack = []
        for char in charList:
            if char == '[':
                lineStack.append(char)
            elif char == '(':
                lineStack.append(char)
            elif char == '<':
                lineStack.append(char)
            elif char == '{':
                lineStack.append(char)
            elif char == ']':
                lastChar = lineStack.pop()
                if lastChar != '[':
                    illegalBracket += 1
                    break
            elif char == ')':
                lastChar = lineStack.pop()
                if lastChar != '(':
                    illegalParen += 1
                    break
            elif char == '>':
                lastChar = lineStack.pop()
                if lastChar != '<':
                    illegalAngle += 1
                    break
            elif char == '}':
                lastChar = lineStack.pop()
                if lastChar != '{':
                    illegalCurly += 1
                    break
    return illegalParen*3 + illegalBracket*57 + illegalCurly*1197 + illegalAngle*25137

def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    incompleteRowScores = []
    for fileLine in fileData:
        charList = split(fileLine.strip())
        lineStack = []
        isInvalidLine = False
        for char in charList:
            if char == '[':
                lineStack.append(char)
            elif char == '(':
                lineStack.append(char)
            elif char == '<':
                lineStack.append(char)
            elif char == '{':
                lineStack.append(char)
            elif char == ']':
                lastChar = lineStack.pop()
                if lastChar != '[':
                    isInvalidLine = True
                    break
            elif char == ')':
                lastChar = lineStack.pop()
                if lastChar != '(':
                    isInvalidLine = True
                    break
            elif char == '>':
                lastChar = lineStack.pop()
                if lastChar != '<':
                    isInvalidLine = True
                    break
            elif char == '}':
                lastChar = lineStack.pop()
                if lastChar != '{':
                    isInvalidLine = True
                    break
        if len(lineStack) > 0 and isInvalidLine == False:
            rowVal = 0
            while len(lineStack) > 0:
                rowVal *= 5
                currentChar = lineStack.pop()
                if currentChar == '(':
                    rowVal += 1
                elif currentChar == '[':
                    rowVal += 2
                elif currentChar == '{':
                    rowVal += 3
                elif currentChar == '<':
                    rowVal += 4
            incompleteRowScores.append(rowVal)
    incompleteRowScores.sort()
    return statistics.median(incompleteRowScores)

filePath = "C:\\dev\\AdventOfCode\\Input\\Day10.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))