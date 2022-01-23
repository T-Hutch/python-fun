def letterDict():
    return {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, 
            "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0 }

class WordSleuth:

    def __init__(self, *args, **kwargs):
        # Letter Dictionaries
        self.firstProp = letterDict()
        self.secondProp = letterDict()
        self.thirdProp = letterDict()
        self.fourthProp = letterDict()
        self.fifthProp = letterDict()

        # Word Guess Handling
        self.wordlist = []
        self.correctLetters = []
        self.falseLetters = []
        self.template = []
        self.badLocation = {0:'',1:'',2:'',3:'',4:''}

        #Initial Dictionary Load
        with open("wordle_complete_dictionary.txt") as source:
            r = source.readline()
            while r:
                self.wordlist.append(r[0:5])
                self.firstProp[r[0]] = self.firstProp.get(r[0]) + 1
                self.secondProp[r[1]] = self.secondProp.get(r[1]) + 1
                self.thirdProp[r[2]] = self.thirdProp.get(r[2]) + 1
                self.fourthProp[r[3]] = self.fourthProp.get(r[3]) + 1
                self.fifthProp[r[4]] = self.fifthProp.get(r[4]) + 1
                r = source.readline()
        return super().__init__(*args, **kwargs)

    # Result is in format +, -, =  (correct, incorrect, correct in position)
    def markGuess(self, guess, result):
        for n in range(0,4):
            if result[n] == "=":
                self.template[n] = guess[n]
            elif result[n] == "+":
                self.correctLetters.append(guess[n])
            elif result[n] == "-":
                self.falseLetters.append(guess[n])

# Reset letter based probabilities when the base wordList changes
    def updateProbabiliies():
        self.firstProp = letterDict()
        self.secondProp = letterDict()
        self.thirdProp = letterDict()
        self.fourthProp = letterDict()
        self.fifthProp = letterDict()

        for r in self.wordList:
            self.firstProp[r[0]] = self.firstProp.get(r[0]) + 1
            self.secondProp[r[1]] = self.secondProp.get(r[1]) + 1
            self.thirdProp[r[2]] = self.thirdProp.get(r[2]) + 1
            self.fourthProp[r[3]] = self.fourthProp.get(r[3]) + 1
            self.fifthProp[r[4]] = self.fifthProp.get(r[4]) + 1

    def print_wordlList(self):
        print(self.wordlist)


