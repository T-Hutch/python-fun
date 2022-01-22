#!/usr/bin/python
#  FactFinder

# Imports:
import sys,os

def printDict(useDict):
    baseList = sorted(useDict.items(), key=lambda x:-x[1])
    sortDict = dict(baseList)
    print(sortDict)

def letterDict():
    return {  "a" : 0, "b" : 0, "c" : 0,  "d" : 0,  "e" : 0,  "f" : 0,  "g" : 0,  "h" : 0,  "i" : 0,  "j" : 0,  "k" : 0,  "l" : 0,  "m" : 0, 
            "n" : 0,  "o" : 0,  "p" : 0,  "q" : 0,  "r" : 0,  "s" : 0,  "t" : 0,  "u" : 0,  "v" : 0,  "w" : 0,  "x" : 0,  "y" : 0,  "z" : 0 }

# Variable/Dictionary Definitions
firstDict = letterDict()
secondDict = letterDict()
thirdDict = letterDict()
fourthDict = letterDict()
fifthDict = letterDict()
baseDict = letterDict()

# Read/Exclude
with open("wordle_complete_dictionary.txt") as source:
    r = source.readline()
    while r:
        n = firstDict.get(r[0])
        n += 1
        firstDict[r[0]] = n

        n = secondDict.get(r[1])
        n += 1
        secondDict[r[1]] = n

        n = thirdDict.get(r[2])
        n += 1
        thirdDict[r[2]] = n

        n = fourthDict.get(r[3])
        n += 1
        fourthDict[r[3]] = n

        n = fifthDict.get(r[4])
        n += 1
        fifthDict[r[4]] = n

        for i in baseDict:
            if r.count(i) > 0:
                baseDict[i] = baseDict.get(i) + 1

        r = source.readline()

# Return dictionary size, and letter probability in order.
print("First Letter Incidence:")
printDict(firstDict)

print("Second Letter Incidence:")
printDict(secondDict)

print("Third Letter Incidence:")
printDict(thirdDict)

print("Fourth Letter Incidence:")
printDict(fourthDict)

print("Fifth Letter Incidence:")
printDict(fifthDict)

print("General Letter Incidence: (At least Once per Word)")
printDict(baseDict)