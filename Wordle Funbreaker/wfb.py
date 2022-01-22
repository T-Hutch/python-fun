#!/usr/bin/python
# Argument format:  CorrectLettersInOrder, CorrectLetters, ExcludedLetters
#    CorrectLettersInOrder:  5 letter string, spaces in place of unknown, green letters in place 
#    CorrectLetters:  Yellow letters in a string, any length
#    ExcludedLetters:  Greyed out letters in a string, any length.

# Imports:
import sys,os

# Functions:
def passTemplate(template,word):
    pos = 0
    for c in template:
        if c != " " and (template[pos] != word[pos]):
            return False
        pos += 1
    return True

def containsAny(let,word):
    for c in let:
        if word.count(c) > 0:
            return True
    return False

def containsAll(let,word):
    for c in let:
        if word.count(c) == 0:
            return False
    return True

def printDict(useDict,):
    baseList = sorted(useDict.items(), key=lambda x:-x[1])
    sortDict = dict(baseList[:10])
    print(sortDict)

def letterDict():
    return {
  "a" : 0, "b" : 0, "c" : 0,  "d" : 0,  "e" : 0,  "f" : 0,  "g" : 0,  "h" : 0,  "i" : 0,  "j" : 0,  "k" : 0,  "l" : 0,  "m" : 0, 
  "n" : 0,  "o" : 0,  "p" : 0,  "q" : 0,  "r" : 0,  "s" : 0,  "t" : 0,  "u" : 0,  "v" : 0,  "w" : 0,  "x" : 0,  "y" : 0,  "z" : 0 }

# External Documentation
if len(sys.argv) != 4:
    print("The syntax for using this command is wfb <CorrectLettersInOrder> <CorrectLetters> <ExcludedLetters>")
    sys.exit()

# Variable/Dict generation
wordList = []
total = 0
count = 0

# Arguments and File Setup
try:
    correctStr = sys.argv[1]
    correctLet = sys.argv[2]
    badLet = sys.argv[3]
except:
    print("Please provide letter groups for procesing.")
    sys.exit(2)

if(len(correctStr)!= 5):
    print("Invalid Correct String Length")
    sys.exit(2)

# Read/Exclude
with open("wordle_complete_dictionary.txt") as source:
    r = source.readline()
    r = r[:5]
    while r:
        if not passTemplate(correctStr,r):
            pass
        elif not containsAll(correctLet,r):
            pass
        elif containsAny(badLet,r):
            pass
        else:
            wordList.append(r[:5])
            count += 1
        total += 1
        r = source.readline()

# Build Letter Probability Dictionary
# Method using total incidence, including duplicates.
propDict = letterDict()
for word in wordList:
    for n in range(0,4):
        propDict[word[n]] = propDict.get(word[n]) + 1

# Build Letter Probability Dictionary
# Method using single letter incidence 
#
#propDict = letterDict()
#for word in wordList:
#    for n in propDict:
#        if word.count(n) > 0:
#            propDict[n] = propDict.get(n) + 1

# Construct Best Guest
propWords = {}
for word in wordList:
    wordTotal = 0
    for n in range(0,4):
        wordTotal = wordTotal + propDict[word[n]]
    propWords[word] = wordTotal

# Return dictionary size, and letter probability in order.
print("Total Words Processed: ",total)
print("Total Words Matched: ",count)
print("Highest Probability Guesses:")
printDict(propWords)
