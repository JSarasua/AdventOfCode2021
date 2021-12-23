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

def IsValidCoordinateTuple( listToCheck, xyTuple:tuple):
    return IsValidCoordinate(listToCheck, xyTuple[1], xyTuple[0])

def GetValAtCoordinate( list:list, xy:tuple):
    return list[xy[1]][xy[0]]

def SetValAtCoordinate( list:list, xy:tuple, val):
    list[xy[1]][xy[0]] = val
    return

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

def AddCountToDict(dict:dict, key, count):
    if key in dict.keys():
        dict[key] += count
    else:
        dict[key] = count

def MakeListInitialVal(length, initialVal):
    list = [initialVal] * length
    return list

def Make2DList(rowLen, colLen, initialVal):
    list = []
    for colIndex in range(0, colLen):
        list.append(MakeListInitialVal(rowLen, initialVal))

    return list
#For current day

def AddXY(a,b):
    c = (a[0] + b[0], a[1] + b[1])
    return c

def AddNeighbors(listToUpdate, currentElem, previousElem, map:list):
    north = (0, 1)
    south = (0, -1)
    east = (1, 0)
    west = (-1, 0)

    northElem = AddXY(currentElem, north)
    southElem = AddXY(currentElem, south)
    eastElem = AddXY(currentElem, east)
    westElem = AddXY(currentElem, west)

    if northElem != previousElem and IsValidCoordinateTuple(map, northElem) and northElem not in listToUpdate:
        listToUpdate.append(northElem)
    if southElem != previousElem and IsValidCoordinateTuple(map, southElem) and southElem not in listToUpdate:
        listToUpdate.append(southElem)
    if eastElem != previousElem and IsValidCoordinateTuple(map, eastElem) and eastElem not in listToUpdate:
        listToUpdate.append(eastElem)
    if westElem != previousElem and IsValidCoordinateTuple(map, westElem) and westElem not in listToUpdate:
        listToUpdate.append(westElem)

def UpdateNeighbors(listToUpdate:list, heatMap:list, cavernMap:list):
    if len(listToUpdate) == 0:
        return
    lowestElem = listToUpdate[0]
    lowestVal = GetValAtCoordinate(heatMap,lowestElem)
    for elem in listToUpdate:
        if lowestVal == -1:
            lowestVal = GetValAtCoordinate(heatMap, elem)
            lowestElem = elem
        else:
            currentVal = GetValAtCoordinate(heatMap,elem)
            if currentVal < lowestVal:
                lowestVal = currentVal
                lowestElem = elem
    listToUpdate.remove(lowestElem)
    elemToUpdate = lowestElem
    if not IsValidCoordinateTuple(heatMap,elemToUpdate):
        return

    north = (0,1)
    south = (0,-1)
    east = (1, 0)
    west = (-1,0)

    northElem = AddXY(elemToUpdate, north)
    southElem = AddXY(elemToUpdate, south)
    eastElem = AddXY(elemToUpdate, east)
    westElem = AddXY(elemToUpdate, west)

    currentHeatVal = GetValAtCoordinate(heatMap,elemToUpdate)

    if IsValidCoordinateTuple(cavernMap, northElem):
        heatMapVal = GetValAtCoordinate(heatMap,northElem)
        riskVal = GetValAtCoordinate(cavernMap,northElem)
        newPossibleHeatVal = currentHeatVal + riskVal
        if heatMapVal == -1 or heatMapVal > newPossibleHeatVal:
            SetValAtCoordinate(heatMap, northElem, newPossibleHeatVal)
            listToUpdate.append(northElem)

    if IsValidCoordinateTuple(cavernMap, southElem):
        heatMapVal = GetValAtCoordinate(heatMap,southElem)
        riskVal = GetValAtCoordinate(cavernMap,southElem)
        newPossibleHeatVal = currentHeatVal + riskVal
        if heatMapVal == -1 or heatMapVal > newPossibleHeatVal:
            SetValAtCoordinate(heatMap, southElem, newPossibleHeatVal)
            listToUpdate.append(southElem)

    if IsValidCoordinateTuple(cavernMap, eastElem):
        heatMapVal = GetValAtCoordinate(heatMap,eastElem)
        riskVal = GetValAtCoordinate(cavernMap,eastElem)
        newPossibleHeatVal = currentHeatVal + riskVal
        if heatMapVal == -1 or heatMapVal > newPossibleHeatVal:
            SetValAtCoordinate(heatMap, eastElem, newPossibleHeatVal)
            listToUpdate.append(eastElem)

    if IsValidCoordinateTuple(cavernMap, westElem):
        heatMapVal = GetValAtCoordinate(heatMap,westElem)
        riskVal = GetValAtCoordinate(cavernMap,westElem)
        newPossibleHeatVal = currentHeatVal + riskVal
        if heatMapVal == -1 or heatMapVal > newPossibleHeatVal:
            SetValAtCoordinate(heatMap, westElem, newPossibleHeatVal)
            listToUpdate.append(westElem)

    return



def MakeHeatMap(cavernMap:list, startPostion:tuple):

    listToUpdate = []
    heatMap = Make2DList( len(cavernMap[0]), len(cavernMap), -1)
    SetValAtCoordinate(heatMap, startPostion, GetValAtCoordinate(cavernMap,startPostion))
    listToUpdate.append(startPostion)



    while( len(listToUpdate) > 0):
        UpdateNeighbors(listToUpdate, heatMap, cavernMap)

    return heatMap

def MakeDay2CavernMap( cavernMap):
    rowLen = len(cavernMap[0])
    colLen = len(cavernMap)
    totalRowLen = len(cavernMap[0])*5
    totalColLen = len(cavernMap)*5

    BigMap = Make2DList(totalRowLen, totalColLen, 0)

    for rowIndex in range(0, len(BigMap)):
        for colIndex in range(0, len(BigMap[0])):
            rowMod = rowIndex % rowLen
            colMod = colIndex % colLen
            rowDiv = rowIndex // rowLen
            colDiv = colIndex // colLen
            newVal = GetValAtCoordinate(cavernMap, (colMod,rowMod)) + rowDiv + colDiv
            if newVal > 9:
                newVal %= 10
                newVal += 1
            SetValAtCoordinate(BigMap, (colIndex,rowIndex), newVal)

    return BigMap



def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    cavernMap = Make2DDataArray(fileData)

    startPostion = (0,0)
    endPosition = (len(cavernMap[0]) - 1, len(cavernMap) - 1)

    heatMap = MakeHeatMap(cavernMap, endPosition)
    lowestRisk = heatMap[0][0]
    return lowestRisk - GetValAtCoordinate(cavernMap,startPostion)



def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    cavernMap = Make2DDataArray(fileData)

    cavernMap = MakeDay2CavernMap(cavernMap)
    startPostion = (0,0)
    endPosition = (len(cavernMap[0]) - 1, len(cavernMap) - 1)

    heatMap = MakeHeatMap(cavernMap, endPosition)
    lowestRisk = heatMap[0][0]
    return lowestRisk - GetValAtCoordinate(cavernMap,startPostion)

filePath = "C:\\dev\\AdventOfCode\\Input\\Day15.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))