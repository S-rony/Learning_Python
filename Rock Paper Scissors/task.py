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

# my_list = []
# if my_value == 0:
#     my_list.append("Rock")
# if my_value == 1:
#     my_list.append("Paper")
# if my_value == 2:
#     my_list.append("Scissor")
my_game = input("What do you choose? Type 0 for Rock, 1 for paper,or 2 for Scissor:")
my_value = []
if my_game == "0":
    my_value.append("Rock")
elif my_game == "1":
    my_value.append("Paper")
elif my_game == "2":
    my_value.append("Scissor")
print("MY_VALUE : ",my_value[0])
game = ["Rock","Paper","Scissor"]
random_game = random.choice(game)
print("PC_VALUE : ",random_game)
random_list = []
# print("random_list",random_list)
if random_game == "Rock":
    random_list.append("Rock")
elif random_game == "Paper":
    random_list.append("Paper")
elif random_game == "Scissor":
    random_list.append("Scissor")

if my_value[0] == "Rock" and random_list[0] == "Rock":
    print("Draw")
elif my_value[0] == "Rock" and random_list[0] == "Paper":
    print("You Loose")
    print(paper)
elif my_value == "Rock" and random_list[0] == "Scissor":
    print("You Win")
    print(rock)

elif my_value[0] == "Paper" and random_list[0] == "Rock":
    print("You Win")
    print(paper)
elif my_value[0] == "Paper" and random_list[0] == "Paper":
    print("Draw")
elif my_value[0] == "Paper" and random_list[0] == "Scissor":
    print("You Loose")
    print(scissors)

elif my_value[0] == "Scissor" and random_list[0] == "Rock":
    print("You Loose")
    print(rock)
elif my_value[0] == "Scissor" and random_list[0] == "Paper":
    print("You Win")
    print(scissors)
elif my_value[0] == "Scissor" and random_list[0] == "Scissor":
    print("Draw")

###########################################################################################################################################################





# my_computer = []



# if my_list[0] == my_computer[0] and my_list[0] == my_computer
#     print()
#
#