import statistics
from collections import Counter

def print_count(countValue):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Total Count: {countValue}')  # Press Ctrl+F8 to toggle the breakpoint.

def split(word):
    return [char for char in word]

def GetCharacterCount(char, wordList):
    charCount = 0
    for word in wordList:
        count = Counter(word)
        if count[char] > 0:
            charCount += 1
    return charCount

def GenerateNumCodes(codedNums:list):
    numCodes = []

    possibleChars = ['a','b','c','d','e','f','g']
    top = possibleChars.copy()
    topRight = possibleChars.copy()
    botRight =possibleChars.copy()
    bot = possibleChars.copy()
    botLeft = possibleChars.copy()
    topLeft = possibleChars.copy()
    middle = possibleChars.copy()

    codedNums.sort(key=len)

    for codedNum in codedNums:
        chars = set(split(codedNum))
        if len(chars) == 2:
            topRight = [x for x in topRight if x[0] in chars]
            botRight = [x for x in botRight if x[0] in chars]

        elif len(chars) == 3:
            top = [x for x in top if x[0] in chars]
            topRight = [x for x in topRight if x[0] in chars]
            botRight = [x for x in botRight if x[0] in chars]
        elif len(chars) == 4:
            topRight = [x for x in topRight if x[0] in chars]
            botRight = [x for x in botRight if x[0] in chars]
            middle = [x for x in middle if x[0] in chars]
            topLeft = [x for x in topLeft if x[0] in chars]

    top = [x for x in top if x[0] not in topRight]

    topLeft = [x for x in topLeft if x[0] not in topRight]
    topLeft = [x for x in topLeft if x[0] not in top]
    middle = [x for x in middle if x[0] not in topRight]
    middle = [x for x in middle if x[0] not in top]
    bot = [x for x in bot if x[0] not in topRight]
    bot = [x for x in bot if x[0] not in top]
    bot = [x for x in bot if x[0] not in middle]
    botLeft = [x for x in botLeft if x[0] not in topRight]
    botLeft = [x for x in botLeft if x[0] not in top]
    botLeft = [x for x in botLeft if x[0] not in middle]

# count each case for bot left. One will have count 4 (bot left) and the other 7 (bot)
    if GetCharacterCount(botLeft[0], codedNums) == 7:
        botLeft.remove(botLeft[0])
        bot.remove(bot[1])
    else:
        botLeft.remove(botLeft[1])
        bot.remove(bot[0])
# count each case for top right. one will have count 9 (bot right) and the other 8 (top right)
    if GetCharacterCount(topRight[0], codedNums) == 9:
        topRight.remove(topRight[0])
        botRight.remove(botRight[1])
    else:
        topRight.remove(topRight[1])
        botRight.remove(botRight[0])
# count each case for top left. one will have count 6 (top left) and the other 7 (middle)
    if GetCharacterCount(topLeft[0], codedNums) == 7:
        topLeft.remove(topLeft[0])
        middle.remove(middle[1])
    else:
        topLeft.remove(topLeft[1])
        middle.remove(middle[0])

    zero = "".join(sorted(top[0] + topLeft[0] + topRight[0] + botLeft[0] + botRight[0] + bot[0]))
    one = "".join(sorted(topRight[0] + botRight[0]))
    two = "".join(sorted(top[0] + topRight[0] + middle[0] + botLeft[0] + bot[0]))
    three = "".join(sorted(top[0] + topRight[0] + middle[0] + botRight[0] + bot[0]))
    four = "".join(sorted(topLeft[0] + topRight[0] + middle[0] + botRight[0]))
    five = "".join(sorted(top[0] + topLeft[0] + middle[0] + botRight[0] + bot[0]))
    six = "".join(sorted(top[0] + topLeft[0] + middle[0] + botLeft[0] + botRight[0] + bot[0]))
    seven = "".join(sorted(top[0] + topRight[0] + botRight[0]))
    eight = "".join(sorted(top[0] + topLeft[0] + topRight[0] + botLeft[0] + botRight[0] + bot[0] + middle[0]))
    nine = "".join(sorted(top[0] + topLeft[0] + topRight[0] + middle[0] + botRight[0] + bot[0]))

    numCodes.append(zero)
    numCodes.append(one)
    numCodes.append(two)
    numCodes.append(three)
    numCodes.append(four)
    numCodes.append(five)
    numCodes.append(six)
    numCodes.append(seven)
    numCodes.append(eight)
    numCodes.append(nine)

    return numCodes

def GenerateOutputNum( numCodes, lineOutput):
    num = []
    for lineNum in lineOutput:
        num.append(numCodes.index("".join(sorted(lineNum))))
    numStr = ''.join([str(elem) for elem in num])
    outputNum = int(numStr)
    return outputNum

def SolveDayPartA(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    outputs = []
    for fileLine in fileData:
        outputs.append(fileLine.strip().split(" | ")[1].split(" "))

    count1478 = 0
    for output in outputs:
        for num in output:
            if len(num) == 2 or len(num) == 3 or len(num) == 4 or len(num) == 7:
                count1478 += 1

    return count1478

def SolveDayPartB(filepath):
    with open(filepath, "r") as openedFile:
        fileData = openedFile.readlines()

    sumOutputs = 0
    outputs = []
    for fileLine in fileData:
        lineData = fileLine.strip().split(" | ")
        lineInput = lineData[0].split(" ")
        lineOutput = lineData[1].split(" ")
        numCodes = GenerateNumCodes(lineInput)
        lineNum = GenerateOutputNum(numCodes, lineOutput)
        sumOutputs += lineNum

    return sumOutputs

filePath = "C:\\dev\\AdventOfCode\\Input\\Day8.txt"
print_count(SolveDayPartA(filePath))
print_count(SolveDayPartB(filePath))

