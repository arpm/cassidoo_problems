def makeAPal(string):
    baseString = newString = str.lower(string.replace(" ", ""))
    for i in range(len(baseString)):
        if newString == newString[::-1]:
            return abs(len(newString) - len(baseString))
        else:
            newString = baseString + baseString[i::-1]

print(makeAPal("xx"))