from random import *
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0
def check_answer(guess, answer, turns):
    """  checks answer against guess. Returns the number of turns remaining  """
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too Low.")  
        return turns - 1  
    else:
        print(f"You got it! The answer was {answer}.")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

 
def game():
    print(logo)

    print("Wecome to the Number Guessinf Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    # print(answer)


    turns = set_difficulty()

    guess = 0
    while guess != answer: 
        print(f"You have {turns} attempts remaining to guess the number")

        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0 :
            print("You ran of turns you lose!")
            return 
        elif guess != answer:
            print("Guess again")

game()