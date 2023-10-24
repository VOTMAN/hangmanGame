# hangmanGame

#### Video Demo: [https://youtu.be/3agcBcyiPP8]
#### Description
This documentation provides a in-depth explanation of the Python Hangman game code. The Hangman game is a word-guessing game where players attempt to guess a hidden word by suggesting letters. If they make too many incorrect guesses, a hangman figure is drawn.

## Note
For the purposes of simplicity, i've used only the days of the week as the words to be guessed in this game.

## Features

### 1. Required Modules
The code starts by importing three Python modules, `random`, `pyfiglet`, and `termcolor`.

- `random` is used for generating a random word for the game.
- `pyfiglet` is used for creating stylized text for the game title.
- `termcolor` is used for adding colored text to the game.

### 2. `randomWord` Function
This function selects a random day of the week (Monday to Sunday) from a predefined list and returns it as the secret word for the game.

### 3. `getGuess` Function
This function handles user input for guessing letters. It enforces the following rules:
- Only single alphabetical characters are allowed as input.
- If the input doesn't meet these criteria, the user is prompted to enter a valid guess.

### 4. `scoreBoard` Function
The `scoreBoard` function takes the secret word and the correct guesses made by the player and returns a string representing the word, with underscores (_) for unguessed letters.

### 5. `hangmanAskii` Function
This function is responsible for displaying ASCII art representing the hangman's current state based on the number of wrong guesses made. It returns different hangman figures.

### 6. `main` Function
- The `main` function is the core of the Hangman game.
- It initializes variables, including `wrongGuesses` (tracking incorrect guesses), `secretWord` (the target word), and `correctGuessed` (list of correctly guessed letters).
- The game begins with a welcome message using stylized text and instructions to save the man from being hanged.
- The game loop continues until one of two conditions is met: the word is guessed or six wrong guesses are made.
- In each iteration, the hangman figure, wrong guesses count, and the current state of the word are displayed.
- The player is prompted for a guess, and the game checks if the guess is correct.
- If the word is correctly guessed or six wrong guesses are made, the game ends, and an appropriate message is displayed in green (win) or red (loss).

## Dependencies
  All the modules are installed with pip
- `random`: Used for random word selection.
- `pyfiglet`: Used for creating stylized text.
- `termcolor`: Used for adding colored text.
- Random Module: In-build with python
- pyfiglet Module: `pip install pyfiglet`
- termcolor Module: `pip install termcolor`
