Wordle Game with Python and Tkinter
This is a Python implementation of the popular word-guessing game Wordle using the Tkinter library for the GUI. The dictionary of words used by the game is sourced from words_alpha.txt by dwyl.

Requirements
 * Python 3.x
 * Tkinter (usually pre-installed with Python)
 
Installation
 * Download both the WORDLE.py and words.txt files and save them in the same folder.
 
How to Play
 1 Run the WORDLE.py file using the command python WORDLE.py in your terminal or command prompt.
 2 Enter your guess for the 5-letter word and press the Enter key on your keyboard.
 3 You can use the Backspace button to go back to the previous box and correct your guess.
 4 The game will return a feedback of colored circles for each letter in your guess.
 5 A correct letter in the correct place will show a green circle.
 6 A correct letter in the wrong place will show a yellow circle.
 7 An incorrect letter will show a gray circle.
 8 Repeat steps 2-4 until you guess the word in six tries or less.
 
Game Rules
 1 You have to guess the Wordle in six tries or less.
 2 Every word you enter must be in the word list. There are more than 10,000 words in this list, but only a subset of them (2,309 at the time of writing) are answers to a specific puzzle.
 3 Letters can be used more than once.
 
Notes
 * This implementation is not perfect, but it follows the game rules.
 * Feel free to modify and improve upon this code according to your needs.
