from art import logo
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#deal both user and computer a starting hand of 2 random card values
user_cards = random.choices(cards,k=2)
computer_cards = random.choices(cards,k=2)
print(logo)


# print(user_cards)
# print(computer_cards)
def ace_over_21(cards_1):
    for i in cards_1:
        if i == 11:
            index = cards_1.index(i)
            cards_1[index] = 1
        elif i != 11:
            print("Loose")
blackjack = True
while blackjack:
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)

    blackjack = 21
    # Detect when computer or user has a blackjack. (Ace + 10 value card).
    if user_score == blackjack and computer_score == blackjack:
        print("Loose")
    elif user_score == blackjack:
        print("Win")
    else:
        if user_score > 21:
            user_cards =  ace_over_21(user_cards)
            computer_cards = ace_over_21(computer_cards)
            if sum(user_cards) > blackjack and sum(computer_cards) > blackjack:
                print("LOOSE")

        else:
            ask_user = input('"Y" for again and "n" for no').lower()
            if ask_user == "y":
                user_cards = random.choices(cards,k=1)
                user_score = sum(user_cards)
                blackjack = True
            else:
                if computer_score < 17:
                    computer_cards = random.choices(cards,k=1)
                    computer_score = sum(computer_cards)
                    blackjack = True
                elif computer_score > blackjack:
                    print("Win")
                else:
                    if computer_score > user_score:
                        print("Loose")
                    elif computer_score < user_score:
                        print("Win")
                    elif computer_score == user_score:
                        print("Draw")











