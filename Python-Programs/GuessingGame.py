secretWord = "Biswajit"
guess = ""
guesscount = 0
guesslimit = 3
outofguess = False

while guess != secretWord and not(outofguess):
    if guesscount < guesslimit:
     guess = input("Enter Your Guess: ")
     guesscount += 1
    else:
     outofguess = True

if outofguess:
    print("OutOfGuesses")
else:
    print("You Won the Game... Cheers")