import random
from itertools import repeat

from art import logo
print(logo)
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_cards = random.choices(cards, k=2)
computer_cards = random.choices(cards, k=2)
blackjack = 21
user_score = sum(user_cards)
computer_score = sum(computer_cards)
final_hand = 0
repeat = True
while repeat:
    print(f"user card: {user_cards}, user_score: {user_score} ")
    if computer_score == blackjack and user_score == blackjack:
        print("User loss")
    elif computer_score == 21:
        print("User Win")

    def replace_ace(cards,score):
        if score>21:
            for i in cards:
                if i == 11:
                    index_1 = cards.index(i)
        cards[index_1] = 1
    if user_score > blackjack:
        user_cards = replace_ace(user_cards,user_score)
    elif computer_score > blackjack:
        computer_cards = replace_ace(computer_cards,computer_score)
    print("computer cards",computer_cards[0])
    if user_score > 21 or user_score == blackjack or computer_score == blackjack:
        print("Game End")
        repeat = False
    another_card = input("type y if you want another card ")
    if another_card == "y":
        user_cards += random.choices(cards, k=1)
        user_score = sum(user_cards)
    if user_score < 16 or computer_score < 16:
        computer_cards = random.choices(cards, k=1)
        computer_score = sum(computer_cards)

    if computer_score > 16:
        repeat = False
    elif user_score > computer_score:
        print("User Win")
        final_hand += user_score
    elif computer_score > user_score:
        print("Computer Win")
        final_hand += computer_score
    elif  computer_score == user_score:
        print("Draw")
    print("final_hand", final_hand)













# while continue_card:
#
#     print(f"your cards: {your_cards} user score: {your_cards_sum}")
#     print(f"computer first card: {computer_cards[0]}")
#     other_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
#     if other_card == "y":
#         if your_cards_sum >= 21:
#             print("YOU LOOSE")
#             break
#         elif your_cards_sum < 21:
#             your_cards += random.choices(cards, k=1)
#             your_cards_sum = sum(your_cards)
#             continue_card = True
#



