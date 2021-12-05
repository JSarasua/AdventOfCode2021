import os
import sys
from pathlib import Path
import numpy


def print_count(countValue):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Total Count: {countValue}')  # Press Ctrl+F8 to toggle the breakpoint.

def MakeBingoSheet(dataArr):
    bingoSheet = []
    for data in dataArr:
        bingoSheet.append((int(data), False))
    return bingoSheet

def UpdateBingoSheet(bingoSheet, numToCheck):
    for bingoIndex in range(0,len(bingoSheet)):
        bingoEntry = bingoSheet[bingoIndex]
        if bingoEntry[0] == numToCheck:
            bingoEntryList = list(bingoEntry)
            bingoEntryList[1] = True
            bingoSheet[bingoIndex] = tuple(bingoEntryList)
    return bingoSheet

def HasARowWon(bingoSheet):
    currentIndex = 0
    numRows = 5
    numColumns = 5

    isAtBeginningOfRow = True
    isRowAllWins = True

    while currentIndex < numRows * numColumns:
        if currentIndex % numColumns == 0:
            if currentIndex != 0 and isRowAllWins:
                return True
            else:
                isRowAllWins = True

        if not bingoSheet[currentIndex][1]:
            isRowAllWins = False

        currentIndex += 1

    if isRowAllWins:
        return True

    return False


def HasAColumnWon(bingoSheet):
    currentRowIndex = 0
    numRows = 5
    numColumns = 5
    isColumnAllWins = True

    while currentRowIndex < numRows:
        currentColumnIndex = 0
        while currentColumnIndex < numColumns:
            currentIndex = currentColumnIndex*numColumns + currentRowIndex
            if not bingoSheet[currentIndex][1]:
                isColumnAllWins = False
                break
            currentColumnIndex += 1
        if isColumnAllWins:
            return True
        else:
            isColumnAllWins = True
        currentRowIndex += 1

    return False

def HasBingoSheetWon(bingoSheet):
    return HasARowWon(bingoSheet) or HasAColumnWon(bingoSheet)

def CalculateBingoSheetScore(bingoSheet, finalNumCalled):
    unmarkedSum = 0
    for bingoEntry in bingoSheet:
        if not bingoEntry[1]:
            unmarkedSum += bingoEntry[0]

    bingoScore = unmarkedSum * finalNumCalled

    return bingoScore

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    bingoAnswersArr = list(map(int, fileData[0].split(",")))

    bingoSheets = []
    bingoSheet = []
    for lineIndex in range(2,len(fileData)):
        fileLine = fileData[lineIndex]
        if fileLine[0] == '\n':
            bingoSheets.append(MakeBingoSheet(bingoSheet))
            bingoSheet.clear()
            continue
        else:
            bingoStringRow = fileLine.strip().split(' ')
            bingoStringRow = filter(lambda a: a != '', bingoStringRow)
            bingoRow = list(map(int, bingoStringRow))
            bingoSheet.extend(bingoRow)
    bingoSheets.append(MakeBingoSheet(bingoSheet))
    for bingoAnswer in bingoAnswersArr:
        for currentBingoSheet in bingoSheets:
            currentBingoSheet = UpdateBingoSheet(currentBingoSheet, bingoAnswer)
            if HasBingoSheetWon(currentBingoSheet):
                return CalculateBingoSheetScore(currentBingoSheet, bingoAnswer)

    return 0

def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    bingoAnswersArr = list(map(int, fileData[0].split(",")))

    bingoSheets = []
    bingoSheet = []
    for lineIndex in range(2,len(fileData)):
        fileLine = fileData[lineIndex]
        if fileLine[0] == '\n':
            bingoSheets.append(MakeBingoSheet(bingoSheet))
            bingoSheet.clear()
            continue
        else:
            bingoStringRow = fileLine.strip().split(' ')
            bingoStringRow = filter(lambda a: a != '', bingoStringRow)
            bingoRow = list(map(int, bingoStringRow))
            bingoSheet.extend(bingoRow)
    bingoSheets.append(MakeBingoSheet(bingoSheet))
    for bingoAnswer in bingoAnswersArr:
        for currentBingoSheet in reversed(bingoSheets):
            currentBingoSheet = UpdateBingoSheet(currentBingoSheet, bingoAnswer)
            if HasBingoSheetWon(currentBingoSheet):
                if len(bingoSheets) == 1:
                    return CalculateBingoSheetScore(currentBingoSheet, bingoAnswer)
                else:
                    bingoSheets.remove(currentBingoSheet)


    return 0


filePath = "C:\\dev\\AdventOfCode\\Input\\Day4.txt"
#totalCount = SolveDayPartA(filePath)
totalCount = SolveDayPartB(filePath)
print_count(totalCount)
