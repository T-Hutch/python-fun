import wordsleuth as ws
import io

sleuth = ws.WordSleuth()
word = ""

print("Welcome to the Wordle Funbreaker.")
print("Type exit to leave anytime.")
print("")
print("Here are 20 possible starting words:")
sleuth.print_bestGuess()

while word != "exit":
    word = input("Guess:")

    if not word or word == exit:
        break

    print("Output your result:  = for in place match, + for correct letter, - for incorrect letter")
    guess = input("Result:")
    if guess == "=====":
        break

    print()
    sleuth.markGuess(word,guess)
    print("Dictionary has been adjusted:")
    sleuth.print_state()
    print("Potential guesses")
    sleuth.print_bestGuess()

print("Goodbye!")