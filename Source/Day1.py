import os
import sys
from pathlib import Path


def print_count(countValue):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Total Count: {countValue}')  # Press Ctrl+F8 to toggle the breakpoint.


def SolveDay1PartA(filepath):
    currentCount = 0
    previousValue = 99999999
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    for fileLine in fileData:
        currentValue = int(fileLine)
        if currentValue > previousValue:
            currentCount += 1
        previousValue = currentValue
    return currentCount

def SolveDay1PartB(filepath):
    currentCount = 0

    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    index = 0
    while index < len(fileData) - 3:
        currentSum = int(fileData[index]) + int(fileData[index+1]) + int(fileData[index+2])
        nextSum = int(fileData[index+1]) + int(fileData[index+2]) + int(fileData[index+3])
        if nextSum > currentSum:
            currentCount += 1
        index += 1
    return currentCount


if len(sys.argv) != 2:
    quit()
#day1FilePathPartA = sys.argv[1]
#totalCount = SolveDay1(day1FilePath)

day1FilePathPartB = sys.argv[1]
totalCount = SolveDay1PartB(day1FilePathPartB)
print_count(totalCount)
