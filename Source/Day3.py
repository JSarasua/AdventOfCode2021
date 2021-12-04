import os
import sys
from pathlib import Path
import numpy


def print_count(countValue):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Total Count: {countValue}')  # Press Ctrl+F8 to toggle the breakpoint.

def binaryToDecimal(binary):
    n = 0
    for digit in binary:
        n = n * 2 + digit
    return n

def binaryStringToDecimal(binary):
    n = 0
    for digit in binary:
        if digit != '\n':
            n = n * 2 + int(digit)
    return n

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()
    digitArr = numpy.zeros(len(fileData[0])-1)
    lineCount = len(fileData)
    halfLineCount = lineCount/2
    for fileLine in fileData:
        currentIndx = 0
        while currentIndx < len(digitArr):
            digitArr[currentIndx] += int(fileLine[currentIndx])
            currentIndx += 1

    gammaArr = numpy.zeros(len(digitArr))
    epsilonArr = numpy.zeros(len(digitArr))
    currentIndx = 0
    while currentIndx < len(digitArr):
        if digitArr[currentIndx] > halfLineCount:
            gammaArr[currentIndx] = 1
            epsilonArr[currentIndx] = 0
        else:
            gammaArr[currentIndx] = 0
            epsilonArr[currentIndx] = 1
        currentIndx += 1
    gammaStr = ""
    epsilonStr = ""

    for digit in gammaArr:
        gammaStr += str(int(digit))
    for digit in epsilonArr:
        gammaStr += str(int(digit))

    gammaInt = binaryToDecimal(gammaArr)
    epsilonInt = binaryToDecimal(epsilonArr)

    return gammaInt * epsilonInt


def GetFilteredBitAtDigitIndex(dataArr, filterDigit, useGreater):
    bitCount = 0
    lineCount = len(dataArr)
    halfLineCount = lineCount/2
    for fileLine in dataArr:
        digitInt = int(fileLine[filterDigit])
        bitCount += digitInt
        currentIndx = 0

    if useGreater:
        if bitCount >= halfLineCount:
            return 1
        else:
            return 0
    else:
        if bitCount >= halfLineCount:
            return 0
        else:
            return 1

def FilterByBit(dataArr, filterDigit, isGreater):
    filterBit = GetFilteredBitAtDigitIndex(dataArr, filterDigit, isGreater)
    filteredArray = []
    for dataLine in dataArr:
        leftBit = int(dataLine[filterDigit])
        if leftBit == filterBit:
            filteredArray.append(dataLine)

    return filteredArray

def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    dataArrMostCommon = fileData.copy()
    digitIndex = 0
    while len(dataArrMostCommon) > 1 and digitIndex < len(dataArrMostCommon[0]) - 1:
        dataArrMostCommon = FilterByBit(dataArrMostCommon, digitIndex, True)
        digitIndex += 1

    digitIndex = 0
    dataArrLeastCommon = fileData.copy()
    while len(dataArrLeastCommon) > 1 and digitIndex < len(dataArrLeastCommon[0]) - 1:
        dataArrLeastCommon = FilterByBit(dataArrLeastCommon, digitIndex, False)
        digitIndex += 1

    mostCommonData = dataArrMostCommon[0]
    leastCommonData = dataArrLeastCommon[0]

    mostCommonInt = binaryStringToDecimal(mostCommonData)
    leastCommonInt = binaryStringToDecimal(leastCommonData)
    return mostCommonInt * leastCommonInt


filePath = "C:\\dev\\AdventOfCode\\Input\\Day3.txt"
#totalCount = SolveDayPartA(filePath)
totalCount = SolveDayPartB(filePath)
print_count(totalCount)
