import os
import sys
from pathlib import Path


def print_count(countValue):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Total Count: {countValue}')  # Press Ctrl+F8 to toggle the breakpoint.


def SolveDay2PartA(filepath):
    currentDepth = 0
    currentForward = 0
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    for fileLine in fileData:
        fileArray = fileLine.split(" ")
        if fileArray[0] == "forward":
            currentForward += int(fileArray[1])
        elif fileArray[0] == "down":
            currentDepth += int(fileArray[1])
        elif fileArray[0] == "up":
            currentDepth -= int(fileArray[1])

    return currentDepth * currentForward

def SolveDay2PartB(filepath):
    currentDepth = 0
    currentForward = 0
    currentAim = 0
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    for fileLine in fileData:
        fileArray = fileLine.split(" ")
        if fileArray[0] == "forward":
            currentForward += int(fileArray[1])
            currentDepth += currentAim * int(fileArray[1])
        elif fileArray[0] == "down":
            currentAim += int(fileArray[1])
        elif fileArray[0] == "up":
            currentAim -= int(fileArray[1])

    return currentDepth * currentForward


if len(sys.argv) != 2:
    quit()
filePath = sys.argv[1]
#totalCount = SolveDay2PartA(filePath)
totalCount = SolveDay2PartB(filePath)
print_count(totalCount)
