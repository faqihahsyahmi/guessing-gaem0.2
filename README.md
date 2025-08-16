# DIGIT DARTS! (Python CLI Project)

## A functional simple project fully written in Python

A simple text-based Python Digit Darts - Guessing Number game.

This program is created as a beginner-friendly learning exercise focused on Python fundamentals like loops, conditionals, and input handling.

Let's get started!

### 🎯 Game Objective

Guess the secret number chosen by the program before you run out of lives.

## How it works
* The program randomly selects a secret number using `random.randint()`.
* The player chooses a difficulty level:
   - **Easy Mode** → 10 lives
   - **Hard Mode** → 5 lives
* The player enters guesses.
* After each guess, the program gives feedback:
   - **Too high**
   - **Too low**
   - Correct guess
* The game will end when the number is guessed correctly or the player runs out of lives.


## Concept:
* `while` loops
* `if/elif/else` conditionals
* Random module
* Functions
* User input handling


## It has the following features:
* Difficulty selection (Easy: 10 lives, Hard: 5 lives)  
* Feedback after each guess  
* Limited attempts based on difficulty level  

## Weakness/To improve:
* Input validation for non-numeric entries  
* Extra difficulty levels with larger ranges  


## Versioning
* 1.0: Initial release