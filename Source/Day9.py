import statistics
from collections import Counter

def print_count(countValue):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Total Count: {countValue}')  # Press Ctrl+F8 to toggle the breakpoint.

def split(word):
    return [int(char) for char in word]

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

def IsLowPoint(rowIndex, colIndex, dataTable):
    pointToTest = dataTable[rowIndex][colIndex]
    dataRow = dataTable[rowIndex]
    leftColIndex = colIndex - 1
    rightColIndex = colIndex + 1
    if IsValidIndex(dataRow, leftColIndex):
        if pointToTest >= dataRow[leftColIndex]:
            return False
    if IsValidIndex(dataRow, rightColIndex):
        if pointToTest >= dataRow[rightColIndex]:
            return False
    northRowIndex = rowIndex + 1
    southRowIndex = rowIndex - 1
    if IsValidIndex(dataTable, northRowIndex):
        if pointToTest >= dataTable[northRowIndex][colIndex]:
            return False
    if IsValidIndex(dataTable, southRowIndex):
        if pointToTest >= dataTable[southRowIndex][colIndex]:
            return False
    return True

def GetRiskLevelForPoint(rowIndex, colIndex, dataTable):
    return 1 + dataTable[rowIndex][colIndex]

def GetBasinSize(rowIndex, colIndex, dataTable, isVisitedSet):
    currentTuple = (rowIndex,colIndex)
    if currentTuple in isVisitedSet:
        return 0
    isVisitedSet.add(currentTuple)

    lowPointVal = dataTable[rowIndex][colIndex]
    northRowIndex = rowIndex + 1
    southRowIndex = rowIndex - 1
    leftColIndex = colIndex - 1
    rightColIndex = colIndex + 1

    basinSize = 0

    if IsValidIndex(dataTable, northRowIndex):
        northVal = dataTable[northRowIndex][colIndex]
        if northVal >= lowPointVal and northVal != 9:
            basinSize += GetBasinSize(northRowIndex, colIndex, dataTable, isVisitedSet)
    if IsValidIndex(dataTable, southRowIndex):
        southVal = dataTable[southRowIndex][colIndex]
        if southVal >= lowPointVal and southVal != 9:
            basinSize += GetBasinSize(southRowIndex, colIndex, dataTable, isVisitedSet)
    if IsValidIndex(dataTable[rowIndex], leftColIndex):
        leftVal = dataTable[rowIndex][leftColIndex]
        if leftVal >= lowPointVal and leftVal != 9:
            basinSize += GetBasinSize(rowIndex, leftColIndex, dataTable, isVisitedSet)
    if IsValidIndex(dataTable[rowIndex], rightColIndex):
        rightVal = dataTable[rowIndex][rightColIndex]
        if rightVal >= lowPointVal and rightVal != 9:
            basinSize += GetBasinSize(rowIndex, rightColIndex, dataTable, isVisitedSet)

    return 1 + basinSize

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    dataTable = []
    for fileLine in fileData:
        dataRow = split(fileLine.strip())
        dataTable.append(dataRow.copy())

    riskLevelSum = 0

    for rowIndex in range(0,len(dataTable)):
        for colIndex in range(0, len(dataTable[rowIndex])):
           if IsLowPoint(rowIndex, colIndex, dataTable):
               riskLevelSum += GetRiskLevelForPoint(rowIndex, colIndex, dataTable)

    return riskLevelSum

def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    dataTable = []
    for fileLine in fileData:
        dataRow = split(fileLine.strip())
        dataTable.append(dataRow.copy())

    basinSizes = []
    isVisitedSet = set()
    for rowIndex in range(0,len(dataTable)):
        for colIndex in range(0, len(dataTable[rowIndex])):
           if IsLowPoint(rowIndex, colIndex, dataTable):
               basinSizes.append(GetBasinSize(rowIndex, colIndex, dataTable, isVisitedSet))

    basinSizes.sort()
    lastIndex = len(basinSizes) - 1
    return basinSizes[lastIndex] * basinSizes[lastIndex - 1] * basinSizes[lastIndex - 2]

filePath = "C:\\dev\\AdventOfCode\\Input\\Day9.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))

