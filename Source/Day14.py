import statistics
from collections import Counter

#For all days
def print_count(countValue):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Total Count: {countValue}')  # Press Ctrl+F8 to toggle the breakpoint.

def split(word):
    return [char for char in word]

def splitInt(word):
    return [int(char) for char in word]

def IsValidIndex( listToCheck:list, index):
    if 0 <= index < len(listToCheck):
        return True
    return False

def IsValidCoordinate( listToCheck, rowIndex, colIndex):
    if IsValidIndex(listToCheck, rowIndex):
        if IsValidIndex(listToCheck[rowIndex], colIndex):
            return True
    return False

def GetCharacterCount(char, wordList):
    charCount = 0
    for word in wordList:
        count = Counter(word)
        if count[char] > 0:
            charCount += 1
    return charCount

def Make2DDataArray(fileData):
    dataArray = []
    for fileLine in fileData:
        dataArray.append(splitInt(fileLine.strip()))

    return dataArray

#For current day
def AddInsertionRule(fileLine, rulesDict:dict):
    inOut = fileLine.strip().split(" -> ")
    tupleIn = tuple(split(inOut[0]))
    rulesDict[tupleIn] = inOut[1]

    return

def ApplyRules(charList:list, rulesDict:dict):

    index = 0
    while(index < len(charList) - 1):
        for key, val in rulesDict.items():
            startChar = key[0]
            endChar = key[1]
            if charList[index] == startChar:
                if charList[index + 1] == endChar:
                    charList.insert(index + 1,val)
                    index += 1
                    break

        index += 1

    return

def AddCombinationCount( comboTuple:tuple, comboDict:dict, count):
    if comboTuple in comboDict.keys():
        comboDict[comboTuple] += count
    else:
        comboDict[comboTuple] = count
    return


def ApplyRulesB(comboDict:dict, rulesDict:dict):

    newDict = {}
    for comboTuple in comboDict:
        firstChar = comboTuple[0]
        secondChar = rulesDict[comboTuple]
        thirdChar = comboTuple[1]

        currentCount = comboDict[comboTuple]

        firstTuple = (firstChar,secondChar)
        secondTuple = (secondChar,thirdChar)
        comboDict[comboTuple] = 0

        if firstTuple in newDict.keys():
            newDict[firstTuple] += currentCount
        else:
            newDict[firstTuple] = currentCount

        if secondTuple in newDict.keys():
            newDict[secondTuple] += currentCount
        else:
            newDict[secondTuple] = currentCount

    return newDict

def AddCountToDict(dict:dict, key, count):
    if key in dict.keys():
        dict[key] += count
    else:
        dict[key] = count

def GetCharDiff(comboDict:dict, firstChar, lastChar):
    charCount = {}

    AddCountToDict(charCount, firstChar, 1)
    AddCountToDict(charCount, lastChar, 1)

    for charTuple, count in comboDict.items():
        AddCountToDict(charCount, charTuple[0],count)
        AddCountToDict(charCount, charTuple[1],count)

    counter = Counter(charCount)
    mostCommonCounter = counter.most_common()
    mostCommon = mostCommonCounter[0][1]
    mostCommon /= 2
    leastCommon = mostCommonCounter[-1][1]
    leastCommon /= 2
    return mostCommon - leastCommon


def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    startingLine = split(fileData[0].strip())
    rules = {}
    for fileLine in fileData:
        if not fileLine.__contains__("->"):
            continue
        AddInsertionRule(fileLine, rules)
    insertionRules = {}

    currentLine = startingLine
    for step in range(0,10):
        ApplyRules(currentLine, rules)

    mostCommon = Counter(currentLine).most_common()[0][1]
    leastCommon = Counter(currentLine).most_common()[-1][1]

    return  mostCommon - leastCommon



def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    startingLine = split(fileData[0].strip())
    countedLine = []
    comboDict = {}
    firstChar = startingLine[0]
    lastChar = startingLine[len(startingLine) - 1]
    for charindex in range(0, len(startingLine)-1):
        char = startingLine[charindex]
        char2 = startingLine[charindex+1]
        comboTuple = (char, char2)
        AddCombinationCount(comboTuple,comboDict,1)

    rules = {}
    for fileLine in fileData:
        if not fileLine.__contains__("->"):
            continue
        AddInsertionRule(fileLine, rules)
    insertionRules = {}

    for step in range(0,40):
        print(f'On Step: {step + 1}')
        comboDict = ApplyRulesB(comboDict, rules)

    charDiff = GetCharDiff(comboDict, firstChar, lastChar)

    return charDiff

filePath = "C:\\dev\\AdventOfCode\\Input\\Day14.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))