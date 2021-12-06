import os
import sys
from pathlib import Path
import numpy


def print_count(countValue):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Total Count: {countValue}')  # Press Ctrl+F8 to toggle the breakpoint.

def LoadStarterFish(fishDict, starterFishStr):
    fishArray = list(map(int, starterFishStr.split(",")))
    for fish in fishArray:
        fishDict[fish] += 1


def UpdateFishArray(fishDict: dict):
    for key in fishDict:
        if key == -1:
            continue
        fishDict[key-1] = fishDict[key]
    fishDict[6] += fishDict[-1]
    fishDict[8] = fishDict[-1]
    fishDict[-1] = 0

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()
        fishDict = {-1:0,0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
        LoadStarterFish(fishDict, fileData[0])

    fishDay = 0
    while fishDay < 256:
        UpdateFishArray(fishDict)
        fishDay += 1

    fishCount = 0
    for key in fishDict:
        fishCount += fishDict[key]


    return fishCount


def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()



filePath = "C:\\dev\\AdventOfCode\\Input\\Day6.txt"
totalCount = SolveDayPartA(filePath)
#totalCount = SolveDayPartB(filePath)
print_count(totalCount)
