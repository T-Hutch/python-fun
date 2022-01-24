def letterDict():
    return {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, 
            "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0 }

class WordSleuth:

    # Internal Functions
    def __resetProbabilities(self):
        self.letProb = []
        for n in range(0,5):
            self.letProb.append(letterDict())
        return

    def __addProbabilities(self,r):
        for i in range(0,5):
            prob = self.letProb[i]
            prob[r[i]] = prob.get(r[i]) + 1
            self.letProb[i] = prob
        return

    def __passTemplate(self,word):
        for i in range(0,5):
            if self.template[i] == " ":
               pass
            elif self.template[i] != word[i]:
                return False
        return True

    def __containsAny(self,let,word):
        for c in let:
            if word.count(c) > 0:
                return True
        return False

    def __containsAll(self,let,word):
        for c in let:
            if word.count(c) == 0:
                return False
        return True

    def __hasBadPlacement(self,word):
        for n in range(0,5):
            if self.badLocation[n].count(word[n]) > 0:
                return True
        return False

    def __hasBadDuplicates(self,word):
        for n in range(0,5):
            let = word[n]
            if word.count(let) > 1 and (self.noDuplicate.count(let) > 0):
                return True
        return False

    def __rescanWordList(self):
        newList = []
        for word in self.wordList:
            if not self.__passTemplate(word):
                pass
            elif not self.__containsAll(self.correctLetters,word):
                pass
            elif self.__containsAny(self.falseLetters,word):
                pass
            elif self.__hasBadPlacement(word):
                pass
            elif self.__hasBadDuplicates(word):
                print("Excluded: ",word)
                pass
            else:
                newList.append(word)    
        self.wordList = newList
        return

# Initialize New WordSleuth 
    def __init__(self, *args, **kwargs):
        # Letter Dictionaries
        self.__resetProbabilities()

        # Word Guess Handling
        self.wordList = []
        self.correctLetters = []
        self.falseLetters = []
        self.noDuplicate = []
        self.template = [" "," "," "," "," "]
        self.badLocation = ["","","","",""]

        #Initial Dictionary Load
        with open("wordle_complete_dictionary.txt") as source:
            r = source.readline()
            while r:
                self.wordList.append(r[0:5])
                self.__addProbabilities(r[0:5])
                r = source.readline()
        return super().__init__(*args, **kwargs)

# Affect current Word State using a new guess.
# Result is in format +, -, =  (correct, incorrect, correct in position)
    def markGuess(self, guess, result):
        for n in range(0,5):
            if result[n] == "=":
                self.template[n] = guess[n]
                self.correctLetters.append(guess[n])
            elif result[n] == "+":
                self.correctLetters.append(guess[n])
                self.badLocation[n] = self.badLocation[n] + guess[n]
            elif result[n] == "-":
                if self.correctLetters.count(guess[n]) > 0:
                    self.noDuplicate.append(guess[n])
                else: 
                    self.falseLetters.append(guess[n])

        self.__rescanWordList()

        self.__resetProbabilities()

        for r in self.wordList:
            self.__addProbabilities(r)

# Print Active List of Words
    def print_wordlList(self):
        print(self.wordList)

# Print State Data
    def print_state(self):
        print("Total Words:",len(self.wordList))
        print("Correct Letters: ",self.correctLetters)
        print("False Letters",self.falseLetters)
        print("Template: ",self.template)
        print("Known False Locations: ",self.badLocation)
        print("Known Non-Duplicates",self.noDuplicate)

## Print Letter Probabilities
    def print_letterProbs(self):
        for n in range(0,5):
            print("Letter ",n+1," Probabilities")
            print(self.letProb[n])

## Get best guesses for next word
    def print_bestGuess(self):
        probDict = {}
        for word in self.wordList:
            total = 0
            used = []
            for i in range(0,5):
                modifier = 1.00 - (used.count(word[i]) * .33)
                total = total + (self.letProb[i].get(word[i]) * modifier)
                used.append(word[i])
            probDict[word] = total
        baseList = sorted(probDict.items(), key=lambda x:-x[1])
        sortDict = dict(baseList[:20])
        print(sortDict)