import art
import random

#set constant var (global scope)
EASY_LEVEL = 10
HARD_LEVEL = 5

#def func to check player guess against actual value
def check_guess(player_input, chosen_number, lives): #pass in player guess, actual value and lives as input
    """Check player guess against actual value"""
    if player_input == chosen_number:
        print(f"Wow, you guess right! The answer is {chosen_number}")
    elif player_input > chosen_number:
        print("Too high")
        return lives -1
    elif player_input < chosen_number:
        print("Too low")
        return lives -1

#def func for player to choose game level - easy or hard
def set_level(): #no input pass to
    level = input("Choose a difficulty. Type 'easy' or 'hard' ").lower()
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def play_game():
    print(art.logo)

    chosen_number = random.randint(1,100)
    #player_input = int(input("Make a guess: "))
    lives = set_level()

    print(chosen_number)
    player_input = 0
    while player_input != chosen_number:
        print(f"You have {lives} left!")
        player_input = int(input("Make a guess: "))
        #track lives. Deduct if answer wrong
        lives = check_guess(player_input, chosen_number, lives)
        if lives == 0:
            print("You ran out of lives!")
            return
        elif player_input != chosen_number:
            print("Guess again.")            

while input("Play Guessing Game? 'y' or 'n': ").lower() == "y":
    print("\n"*20)
    play_game()
