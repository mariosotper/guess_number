import random

easy_level = 10
hard_level = 5
turns = 0

# function to check user's guess against actual asnwer.
def check_answer(guess, answer, turns):
    """ checks answer against guess. returns the number of turns remaining"""
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("too low")
        return turns - 1
    else:
        print(f"You got it! the answer was {answer}.")


# make function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type'easy' or 'hard': ")
    if level == "easy":
        return easy_level
    else:
        return hard_level


def game():
    # Choosing a random number between 1 and 100

    print("Welcome to the number guessing game!")
    print("Im thinking of a number between 1 and 100")

    answer = random.randint(1, 100)

    turns = set_difficulty()

    # repeat the guessing functionality if they get it wrong

    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts remaining to guess the numeber.")
        # let the user guess the number
        guess = int(input("Make a guess:"))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("you've run out guesses, you lose")
            return
        elif guess != answer:
            print("guess again")

    # Track the number of turnas and reduce by 1 if they gei it worng.


game()
