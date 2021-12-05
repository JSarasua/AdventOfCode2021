import os
import sys
from pathlib import Path
import numpy


def print_count(countValue):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Total Count: {countValue}')  # Press Ctrl+F8 to toggle the breakpoint.

def MakeLineSegment(fileRow):
    lineSegmentStr = fileRow.split(" -> ")
    beginLineStr = lineSegmentStr[0].split(",")
    endLineStr = lineSegmentStr[1].split(",")
    xy1 = (int(beginLineStr[0]), int(beginLineStr[1]))
    xy2 = (int(endLineStr[0]), int(endLineStr[1]))
    lineSegment = (xy1, xy2)
    return lineSegment

def MakeFullLine(lineSegmentBeginEnd):
    fullLine = []
    currentX = lineSegmentBeginEnd[0][0]
    currentY = lineSegmentBeginEnd[0][1]
    fullLine.append((currentX, currentY))

    endX = lineSegmentBeginEnd[1][0]
    endY = lineSegmentBeginEnd[1][1]
    while currentX != endX:
        if currentX < endX:
            currentX += 1
        else:
            currentX -= 1
        fullLine.append((currentX, currentY))

    while currentY != endY:
        if currentY < endY:
            currentY += 1
        else:
            currentY -= 1
        fullLine.append((currentX, currentY))
    return fullLine

def MakeFullLineWithDiags(lineSegmentBeginEnd):
    fullLine = []
    currentX = lineSegmentBeginEnd[0][0]
    currentY = lineSegmentBeginEnd[0][1]
    fullLine.append((currentX, currentY))

    endX = lineSegmentBeginEnd[1][0]
    endY = lineSegmentBeginEnd[1][1]
    while currentX != endX:
        if currentX < endX:
            currentX += 1
        else:
            currentX -= 1
        if currentY < endY:
            currentY += 1
        elif currentY > endY:
            currentY -= 1
        fullLine.append((currentX, currentY))

    while currentY != endY:
        if currentY < endY:
            currentY += 1
        else:
            currentY -= 1
        fullLine.append((currentX, currentY))
    return fullLine

def AddPoint(ventArray, pointXY):
    ventArray[pointXY[0]][pointXY[1]] += 1

    return ventArray

def AddRowDataNoDiag(ventArray,fileRow):
    lineSegment = MakeLineSegment(fileRow)
    if not(lineSegment[0][0] == lineSegment[1][0] or lineSegment[0][1] == lineSegment[1][1]):
        return
    fullLineSegment = MakeFullLine(lineSegment)

    for point in fullLineSegment:
        ventArray = AddPoint(ventArray, point)

def AddRowData(ventArray,fileRow):
    lineSegment = MakeLineSegment(fileRow)
    fullLineSegment = MakeFullLineWithDiags(lineSegment)

    for point in fullLineSegment:
        ventArray = AddPoint(ventArray, point)

def CountOverlaps(ventArray, minCountToBeOverlap):
    currentCount = 0
    for row in ventArray:
        for point in row:
            if point >= minCountToBeOverlap:
                currentCount += 1
    return currentCount

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    #Make 2D array 1000x1000
    rows, cols = (1000, 1000)
    ventArray = [[0 for i in range(cols)] for j in range(rows)]
    for fileLine in fileData:
        AddRowDataNoDiag(ventArray, fileLine)

    return CountOverlaps(ventArray, 2)

def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    rows, cols = (1000, 1000)
    ventArray = [[0 for i in range(cols)] for j in range(rows)]
    for fileLine in fileData:
        AddRowData(ventArray, fileLine)

    return CountOverlaps(ventArray, 2)


filePath = "C:\\dev\\AdventOfCode\\Input\\Day5.txt"
#totalCount = SolveDayPartA(filePath)
totalCount = SolveDayPartB(filePath)
print_count(totalCount)
