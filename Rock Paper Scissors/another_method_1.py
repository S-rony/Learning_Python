rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
#############just logic########################
from random import randint

my_choice = int(input("rock 0, paper 1, scissors 2: "))
print(my_choice)
computer_choice = randint(0,2)
print(computer_choice)
if my_choice == computer_choice:
    print("draw")
elif my_choice < computer_choice:
    print("loose")
elif my_choice == 0 and computer_choice == 2:
    print("Win")
elif my_choice > computer_choice:
    print("Win")

