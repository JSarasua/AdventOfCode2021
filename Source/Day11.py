import statistics
from collections import Counter

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

def IncrementNeighbors(rowIndex, colIndex, dataArray, listToSetTo0, listAlreadyFlashed):
    flashCount = 1
    #Add left
    leftColIndex = colIndex - 1
    if IsValidIndex(dataArray[rowIndex], leftColIndex):
        dataArray[rowIndex][leftColIndex] += 1
        if dataArray[rowIndex][leftColIndex] == 10 and (rowIndex,leftColIndex) not in listAlreadyFlashed:
            listAlreadyFlashed.append((rowIndex, leftColIndex))
            flashCount += IncrementNeighbors(rowIndex, leftColIndex, dataArray, listToSetTo0, listAlreadyFlashed)
            listToSetTo0.append((rowIndex,leftColIndex))
    #Add right
    rightColIndex = colIndex + 1
    if IsValidIndex(dataArray[rowIndex], rightColIndex):
        dataArray[rowIndex][rightColIndex] += 1
        if dataArray[rowIndex][rightColIndex] == 10 and (rowIndex,rightColIndex) not in listAlreadyFlashed:
            listAlreadyFlashed.append((rowIndex, rightColIndex))
            flashCount += IncrementNeighbors(rowIndex, rightColIndex, dataArray, listToSetTo0, listAlreadyFlashed)
            listToSetTo0.append((rowIndex,rightColIndex))
    #Add north
    northRowIndex = rowIndex + 1
    if IsValidIndex(dataArray, northRowIndex):
        dataArray[northRowIndex][colIndex] += 1
        if dataArray[northRowIndex][colIndex] == 10 and (northRowIndex,colIndex) not in listAlreadyFlashed:
            listAlreadyFlashed.append((northRowIndex, colIndex))
            flashCount += IncrementNeighbors(northRowIndex, colIndex, dataArray, listToSetTo0, listAlreadyFlashed)
            listToSetTo0.append((northRowIndex,colIndex))
    #Add south
    southRowIndex = rowIndex - 1
    if IsValidIndex(dataArray, southRowIndex):
        dataArray[southRowIndex][colIndex] += 1
        if dataArray[southRowIndex][colIndex] == 10 and (southRowIndex,colIndex) not in listAlreadyFlashed:
            listAlreadyFlashed.append((southRowIndex, colIndex))
            flashCount += IncrementNeighbors(southRowIndex, colIndex, dataArray, listToSetTo0, listAlreadyFlashed)
            listToSetTo0.append((southRowIndex,colIndex))
    #Add leftNorth
    if IsValidCoordinate(dataArray, northRowIndex, leftColIndex):
        dataArray[northRowIndex][leftColIndex] += 1
        if dataArray[northRowIndex][leftColIndex] == 10 and (northRowIndex,leftColIndex) not in listAlreadyFlashed:
            listAlreadyFlashed.append((northRowIndex, leftColIndex))
            flashCount += IncrementNeighbors(northRowIndex, leftColIndex, dataArray, listToSetTo0, listAlreadyFlashed)
            listToSetTo0.append((northRowIndex,leftColIndex))
    #Add rightNorth
    if IsValidCoordinate(dataArray, northRowIndex, rightColIndex):
        dataArray[northRowIndex][rightColIndex] += 1
        if dataArray[northRowIndex][rightColIndex] == 10 and (northRowIndex,rightColIndex) not in listAlreadyFlashed:
            listAlreadyFlashed.append((northRowIndex, rightColIndex))
            flashCount += IncrementNeighbors(northRowIndex, rightColIndex, dataArray, listToSetTo0, listAlreadyFlashed)
            listToSetTo0.append((northRowIndex,rightColIndex))
    #Add leftSouth
    if IsValidCoordinate(dataArray, southRowIndex, leftColIndex):
        dataArray[southRowIndex][leftColIndex] += 1
        if dataArray[southRowIndex][leftColIndex] == 10 and (southRowIndex,leftColIndex) not in listAlreadyFlashed:
            listAlreadyFlashed.append((southRowIndex, leftColIndex))
            flashCount += IncrementNeighbors(southRowIndex, leftColIndex, dataArray, listToSetTo0, listAlreadyFlashed)
            listToSetTo0.append((southRowIndex,leftColIndex))
    #Add rightSouth
    if IsValidCoordinate(dataArray, southRowIndex, rightColIndex):
        dataArray[southRowIndex][rightColIndex] += 1
        if dataArray[southRowIndex][rightColIndex] == 10 and (southRowIndex,rightColIndex) not in listAlreadyFlashed:
            listAlreadyFlashed.append((southRowIndex, rightColIndex))
            flashCount += IncrementNeighbors(southRowIndex, rightColIndex, dataArray, listToSetTo0, listAlreadyFlashed)
            listToSetTo0.append((southRowIndex,rightColIndex))
    return flashCount

def AddNeighborsToList(rowIndex, colIndex, dataArray, listToIncrement):
    #Add left
    leftColIndex = colIndex - 1
    if IsValidIndex(dataArray[rowIndex], leftColIndex):
        dataArray[rowIndex][leftColIndex] += 1
        listToIncrement.append((rowIndex,leftColIndex))
    #Add right
    rightColIndex = colIndex + 1
    if IsValidIndex(dataArray[rowIndex], rightColIndex):
        listToIncrement.append((rowIndex,rightColIndex))
    #Add north
    northRowIndex = rowIndex + 1
    if IsValidIndex(dataArray, northRowIndex):
        listToIncrement.append((northRowIndex,colIndex))
    #Add south
    southRowIndex = rowIndex - 1
    if IsValidIndex(dataArray, southRowIndex):
        listToIncrement.append((southRowIndex,colIndex))
    #Add leftNorth
    if IsValidCoordinate(dataArray, northRowIndex, leftColIndex):
        listToIncrement.append((northRowIndex,leftColIndex))
    #Add rightNorth
    if IsValidCoordinate(dataArray, northRowIndex, rightColIndex):
        listToIncrement.append((northRowIndex,rightColIndex))
    #Add leftSouth
    if IsValidCoordinate(dataArray, southRowIndex, leftColIndex):
        listToIncrement.append((southRowIndex,leftColIndex))
    #Add rightSouth
    if IsValidCoordinate(dataArray, southRowIndex, rightColIndex):
        listToIncrement.append((southRowIndex,rightColIndex))
    return



def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    numberOfFlashes = 0
    numberOfSteps = 100
    dataArray = Make2DDataArray(fileData)

    for steps in range(0,numberOfSteps):
        listToSetTo0 = []
        flashesToHandle = []
        listAlreadyFlashed = []
        #increment everyone, add neighbors to list if light up
        for rowIndex in range(0,len(dataArray)):
            for colIndex in range(0,len(dataArray[0])):
                dataArray[rowIndex][colIndex] += 1
                if dataArray[rowIndex][colIndex] > 9:
                    flashesToHandle.append((rowIndex,colIndex))
        for tupleVec in flashesToHandle:
            rowIndex = tupleVec[0]
            colIndex = tupleVec[1]
            numberOfFlashes += IncrementNeighbors(rowIndex, colIndex, dataArray, listToSetTo0, listAlreadyFlashed)
        for tupleVec in flashesToHandle:
            dataArray[tupleVec[0]][tupleVec[1]] = 0
        for tupleVec in listAlreadyFlashed:
            dataArray[tupleVec[0]][tupleVec[1]] = 0

    return numberOfFlashes

def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    numberOfFlashes = 0
    numberOfSteps = 1000000
    dataArray = Make2DDataArray(fileData)

    totalOctopuses = len(dataArray) * len(dataArray[0])

    for steps in range(0,numberOfSteps):
        numberOfFlashes = 0
        listToSetTo0 = []
        flashesToHandle = []
        listAlreadyFlashed = []
        #increment everyone, add neighbors to list if light up
        for rowIndex in range(0,len(dataArray)):
            for colIndex in range(0,len(dataArray[0])):
                dataArray[rowIndex][colIndex] += 1
                if dataArray[rowIndex][colIndex] > 9:
                    flashesToHandle.append((rowIndex,colIndex))
        for tupleVec in flashesToHandle:
            rowIndex = tupleVec[0]
            colIndex = tupleVec[1]
            numberOfFlashes += IncrementNeighbors(rowIndex, colIndex, dataArray, listToSetTo0, listAlreadyFlashed)
        for tupleVec in flashesToHandle:
            dataArray[tupleVec[0]][tupleVec[1]] = 0
        for tupleVec in listAlreadyFlashed:
            dataArray[tupleVec[0]][tupleVec[1]] = 0
        if numberOfFlashes == totalOctopuses:
            return steps + 1

    return 0

filePath = "C:\\dev\\AdventOfCode\\Input\\Day11.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))