import statistics


def print_count(countValue):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Total Count: {countValue}')  # Press Ctrl+F8 to toggle the breakpoint.

def GetExpensiveDistance(startPosition, endPosition):
    distance = abs(endPosition - startPosition)
    fuelCost = 0
    for step in range(0, distance):
        fuelCost += step+1
    return fuelCost

def CalculateExpensiveFuelCost(positions, mathPosition):
    fuelCost = 0
    for position in positions:
        fuelCost += GetExpensiveDistance(position, mathPosition)
    return fuelCost

def CalculateFuelCost(positions, matchPosition):
    fuelCost = 0
    for position in positions:
        fuelCost += abs(matchPosition-position)
    return fuelCost

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    startPositions = list(map(int,fileData[0].split(",")))
    startPositions.sort()
    minVal = startPositions[0]
    maxVal = startPositions[len(startPositions)-1]

    minimumCost = -1
    positionAtMinimumCost = -1
    for val in range(minVal,maxVal):
        currentCost = CalculateFuelCost(startPositions, val)
        if minimumCost == -1 or currentCost < minimumCost:
            minimumCost = currentCost
            positionAtMinimumCost = val

    return minimumCost

def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    startPositions = list(map(int,fileData[0].split(",")))
    startPositions.sort()
    minVal = startPositions[0]
    maxVal = startPositions[len(startPositions)-1]

    minimumCost = -1
    positionAtMinimumCost = -1
    for val in range(minVal,maxVal):
        currentCost = CalculateExpensiveFuelCost(startPositions, val)
        if minimumCost == -1 or currentCost < minimumCost:
            minimumCost = currentCost
            positionAtMinimumCost = val

    return minimumCost

def SolveUsingMedianPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    startPositions = list(map(int,fileData[0].split(",")))
    startPositions.sort()
    medianValue = statistics.median(startPositions)
    minimumCost = CalculateFuelCost(startPositions, medianValue)
    return int(minimumCost)

filePath = "C:\\dev\\AdventOfCode\\Input\\Day7.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveUsingMedianPartA(filePath))
print_count(SolveDayPartB(filePath))

