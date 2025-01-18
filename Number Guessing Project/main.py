# printing the stylish part of the game
import random
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


#funtion to check guess and random number from the computer

def check_answer(actual_answer,user_guess,turns):
    """check answer against guess, returns the number of remaining turns"""
    if user_guess > actual_answer:
        print("Too high")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")

#function to set difficulty

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return  EASY_LEVEL_TURNS
    else:
        return  HARD_LEVEL_TURNS

def game():
    #taking a random number between 1 to 100
    print("Welcome to the Number Guessing Game!")

    print("I'm thinking of a number between 1 and 100")

    answer = random.randint(1,100)
    print(f"psst the actual_actual is :{answer}")

    turns = set_difficulty()
    print(f"You have { turns } attempts remaining to guess the number.")

    # repeat the guess if the answer is wrong.
    guess= 0
    while answer != guess:
        #my_input_guess
        guess = int(input("Make a guess: "))
        turns = check_answer(answer,guess,turns)

        if turns == 0:
            print("You've run out of guesses. you loose.")
            return
        elif answer != guess:
            print("Guess again.")
#track the number of turns and reduce my one if it get it wrong
game()






















'''from art import logo
import random
number = random.randint(1, 100)



def game(number,guessed):
    print(logo)
    print("Welcome to the Number Guessing Game!")
    if number > guessed:
        print("Too low")
    if number < guessed:
        print("Too High")
    if number == guessed:
        print("Correct answer")


difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard'").lower()
if difficulty_level == "easy":
    for _ in range(5):
        print("you have 5 numbers")
        game()
else:
    for _ in range(10):
        print("you have 10 numbers")
        game()

guess=input("Make a guess: ")'''


# track the number of turns and reduce by 1 if they get it wrong

# repeat from the making the guess if the guess is wrong





















































"""from art import logo
import random

print(logo)
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# choose a number from 1 to 100
def set_difficulty():
    level = input(f"Choose a difficulty, Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS


def check_answer(user_guess, actual_guess, turns):
    if user_guess == actual_guess:
        print(f"You win {user_guess}")
    elif user_guess > actual_guess:
        print("Too High")
        return turns - 1
    elif user_guess < actual_guess:
        print("Too low")
        return turns - 1


def game():
    print("Welcome to the guessing game!")
    print("I'm thinking of a number between 1 to 100.")
    answer = random.randint(1, 100)
    print("Actual", answer)
    # set difficulty

    # number of turns
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))

        # calc or check guess and original number
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, YOU LOSE")
            return


game()"""


























































# from art import logo
# import random
# print(logo)
# print("Welcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100")
#
# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5
#
#
# answer = random.randint(1,100)
# type_1 = input("Choose the difficulty. type 'easy' or 'hard: ").lower()
#
#
# def check_answer(user_guess, actual_guess):
#     if user_guess == actual_guess:
#         print("You win")
#     elif user_guess > actual_guess:
#         print("Too High")
#     elif user_guess < actual_guess:
#         print(f"Too low {user_guess}")
#
#
# def set_difficulty():
#     level = input("Choose the difficulty. type 'easy' or 'hard: ").lower()
#     if level == "easy":
#         return EASY_LEVEL_TURNS
#     elif level == "hard":
#         return HARD_LEVEL_TURNS
#
#
# set_difficulty()





























# print(number)
# def easy_hard():
#     if type_1 == "easy":
#         for _ in range(1,11):
#             print(f"you will have {11 - i} attempts remaining to guess the number.")
#             calc()
#     elif type_1 == "hard":
#         for _ in range(1,6):
#             calc()
#
# def calc():
#     for i in range(1,11):
#         # print(f"you will have {10} attempts remaining to guess the number.")
#         your_number  = int(input("Make a guess: "))
#         if number != your_number:
#             print(f"you will have {11-i} attempts remaining to guess the number.")
#             if number < your_number:
#                 print("too High")
#             elif number > your_number:
#                 print("Too Low")
#             elif i == 10:
#                 print("Loose")
#                 break
#         elif number == your_number:
#             print(f"you got it! you guess the right answer{your_number}")
#             break
#
#
# if type_1 == "easy":
#     print(f"you will have {10} attempts remaining to guess the number.")
#     calc()
#
# elif type_1 == "hard":
#     for i in range(1,6):
#         print(f"you will have {5} attempts remaining to guess the number.")
#         your_number  = int(input("Make a guess: "))
#         if number != your_number:
#             print(f"you will have {5-i} attempts remaining to guess the number.")
#             if number < your_number:
#                 print("too High")
#             elif number > your_number:
#                 print("Too Low")
#
#         elif number == your_number:
#             print(f"you got it! you guess the right answer{your_number}")
#             break
#
#
#
#
#
#


