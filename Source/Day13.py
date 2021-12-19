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
def MarkCoordinateInDataDict(dataTuple, dataDict):
    dataDict[dataTuple] = 1

def TuplefyLine(fileLine):
    line = fileLine.strip().split(",")
    tupleInt = (int(line[0]),int(line[1]))
    return tupleInt

def TuplefyFold(fileLine):
    line = fileLine.strip().split(" ")[2].split("=")
    if line[0] == "y":
        return (0, int(line[1]))
    else:
        return (int(line[1]), 0)
def FoldDataDict(foldTuple:tuple, dataDict:dict):
    newDataDict = {}
    if foldTuple[0] == 0:
        for key,val in dataDict.items():
            if val == 0:
                continue
            yDist = key[1] - foldTuple[1]
            if yDist < 0:
                newDataDict[key] = val
                continue
            #dataDict[key] = 0
            newKey = (key[0],key[1] - (2*yDist))
            MarkCoordinateInDataDict(newKey, newDataDict)
    else:
        for key,val in dataDict.items():
            if val == 0:
                continue
            xDist = key[0] - foldTuple[0]
            if xDist < 0:
                newDataDict[key] = val
                continue
            #dataDict[key] = 0
            newKey = (key[0] - (2*xDist),key[1])
            MarkCoordinateInDataDict(newKey, newDataDict)
    return newDataDict

def DictToList(dataDict:dict):
    bigX = -1
    bigY = -1
    for key in dataDict.keys():
        xKey = key[0]
        yKey = key[1]
        if xKey > bigX:
            bigX = xKey
        if yKey  > bigY:
            bigY = yKey
    dataList = []
    for y in range(0, bigY + 1):
        dataList.append([0]*(bigX+1))

    for key in dataDict.keys():
        xKey = key[1]
        yKey = key[0]
        dataList[xKey][yKey] = 1
    return dataList


def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    dataDict = {}
    for fileLine in fileData:
        if fileLine.startswith("fold along "):
            foldTuple = TuplefyFold(fileLine)
            dataDict = FoldDataDict(foldTuple,dataDict)
            break
        elif fileLine == "\n":
            continue
        else:
            tupleLine = TuplefyLine(fileLine)
            MarkCoordinateInDataDict(tupleLine, dataDict)

    count = 0
    for key,val in dataDict.items():
        count += val
    return count

def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    dataDict = {}
    for fileLine in fileData:
        if fileLine.startswith("fold along "):
            foldTuple = TuplefyFold(fileLine)
            dataDict = FoldDataDict(foldTuple,dataDict)
        elif fileLine == "\n":
            continue
        else:
            tupleLine = TuplefyLine(fileLine)
            MarkCoordinateInDataDict(tupleLine, dataDict)

    dataList = DictToList(dataDict)
    for line in dataList:
        print(line)
    return 0

filePath = "C:\\dev\\AdventOfCode\\Input\\Day13.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))