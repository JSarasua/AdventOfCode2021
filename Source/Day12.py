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
def GetFilteredPreviousSteps(currentPath):
    filteredSteps = []
    for step in currentPath:
        if step.islower():
            filteredSteps.append(step)
    return filteredSteps

def GetFilteredPreviousStepsDay2(currentPath):
    stepsVisitedOnce = []
    stepVisitedTwice = []
    filteredSteps = []
    for step in currentPath:
        if step == 'start' or step == 'end':
            filteredSteps.append(step)
        elif step.islower():
            if len(stepVisitedTwice) > 0:
                filteredSteps.append(step)
            elif step in stepsVisitedOnce:
                stepVisitedTwice.append(step)
                filteredSteps.append(step)
            else:
                stepsVisitedOnce.append(step)
    if len(stepVisitedTwice) > 0:
        for oneStep in stepsVisitedOnce:
            filteredSteps.append(oneStep)
    return filteredSteps

def AddAllPathsFromCurrentPath(dataGraph, currentPath, possiblePaths):
    CurrentPossiblePaths = []
    nextPossibleRoutes = dataGraph[currentPath[len(currentPath) - 1]]
    nogoSteps = GetFilteredPreviousSteps(currentPath)
    for route in nextPossibleRoutes:
        if route == "end":
            newPath = currentPath.copy()
            newPath.append(route)
            possiblePaths.append(newPath)
        elif route not in nogoSteps:
            newPath = currentPath.copy()
            newPath.append(route)
            AddAllPathsFromCurrentPath(dataGraph, newPath, possiblePaths)

def AddAllPathsFromCurrentPathDay2(dataGraph, currentPath, possiblePaths):
    CurrentPossiblePaths = []
    nextPossibleRoutes = dataGraph[currentPath[len(currentPath) - 1]]
    nogoSteps = GetFilteredPreviousStepsDay2(currentPath)
    for route in nextPossibleRoutes:
        if route == "end":
            newPath = currentPath.copy()
            newPath.append(route)
            possiblePaths.append(newPath)
        elif route not in nogoSteps:
            newPath = currentPath.copy()
            newPath.append(route)
            AddAllPathsFromCurrentPathDay2(dataGraph, newPath, possiblePaths)


def GetListOfAllPossiblePaths(dataGraph:dict):
    possiblePaths = []
    currentPath = ['start']
    AddAllPathsFromCurrentPath(dataGraph, currentPath, possiblePaths)
    return possiblePaths

def GetListOfAllPossiblePathsDay2(dataGraph:dict):
    possiblePaths = []
    currentPath = ['start']
    AddAllPathsFromCurrentPathDay2(dataGraph, currentPath, possiblePaths)
    return possiblePaths


def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    #Make a dictionary of dictionaries with the input as the starting spot and the outputs as the possible end spot.
    dataGraph = {}
    for fileLine in fileData:
        inOut = fileLine.strip().split("-")
        if inOut[0] not in dataGraph.keys():
            dataGraph[inOut[0]] = []
        if inOut[1] not in dataGraph[inOut[0]]:
            dataGraph[inOut[0]].append(inOut[1])
        if inOut[1] not in dataGraph.keys():
            dataGraph[inOut[1]] = []
        if inOut[0] not in dataGraph[inOut[1]]:
            dataGraph[inOut[1]].append(inOut[0])
    possiblePaths = GetListOfAllPossiblePaths(dataGraph)

    #Recursively check all possibilities
    return len(possiblePaths)

def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    #Make a dictionary of dictionaries with the input as the starting spot and the outputs as the possible end spot.
    dataGraph = {}
    for fileLine in fileData:
        inOut = fileLine.strip().split("-")
        if inOut[0] not in dataGraph.keys():
            dataGraph[inOut[0]] = []
        if inOut[1] not in dataGraph[inOut[0]]:
            dataGraph[inOut[0]].append(inOut[1])
        if inOut[1] not in dataGraph.keys():
            dataGraph[inOut[1]] = []
        if inOut[0] not in dataGraph[inOut[1]]:
            dataGraph[inOut[1]].append(inOut[0])
    possiblePaths = GetListOfAllPossiblePathsDay2(dataGraph)

    #Recursively check all possibilities
    return len(possiblePaths)

filePath = "C:\\dev\\AdventOfCode\\Input\\Day12.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))