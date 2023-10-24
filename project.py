import random
import pyfiglet as fig
from termcolor import colored

def randomWord():
    words = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
    secretWord = random.choice(words)
    return secretWord

def getGuess():
    while True:
        guess = input("Enter a letter: ").upper()
        if not guess.isalpha():
            print("Enter only a alphabet")
            continue
        if len(guess) != 1:
            print("Enter a single alphabet")
            continue
        else:
            return guess

def scoreBoard(secretWord, guess):
    guesses = ""
    for char in secretWord:
        if char in guess:
            guesses += char
        else:
            guesses += "_"
    return guesses


def hangmanAskii (wrongGuesses):
    hangman_art = [
        """
        -----
        |   |
            |
            |
            |
            |
        """,
        """
        -----
        |   |
        O   |
            |
            |
            |
        """,
        """
        -----
        |   |
        O   |
        |   |
            |
            |
        """,
        """
        -----
        |   |
        O   |
       /|   |
            |
            |
        """,
        """
        -----
        |   |
        O   |
       /|\\  |
            |
            |
        """,
        """
        -----
        |   |
        O   |
       /|\\  |
       /    |
            |
        """,
        """
        -----
        |   |
        O   |
       /|\\  |
       / \\  |
            |
        """,
        """
      /SAVED\\
      
       \O/
        |
      // \\
      
        """        
    ]

    return hangman_art[wrongGuesses]

def main():
    wrongGuesses = 0
    secretWord = randomWord()
    correctGuessed = []

    print(fig.figlet_format("HANGMAN", font="slant"))
    print("Save the man from being hanged!!")

    while wrongGuesses != 6:
        word = scoreBoard(secretWord, correctGuessed)
        print(hangmanAskii(wrongGuesses))
        print(f"Wrong Guesses: {wrongGuesses}")
        print(word)
        
        if word != secretWord :
            guess = getGuess()

        if guess in secretWord:
            print("Correct Guess :)")
            correctGuessed.append(guess)
        else:
            print("Wrong Guess :(")
            wrongGuesses += 1

        if word == secretWord:
            print(hangmanAskii(7))
            print(colored("You Saved Him!", "green"))
            break
        
        if wrongGuesses == 6:
            print(hangmanAskii(6))
            print(colored("He was hanged", "red"))
            break


if __name__ == "__main__":
    main()


    