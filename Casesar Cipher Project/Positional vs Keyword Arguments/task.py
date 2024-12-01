# Functions with input

def greet_with_name(name,location):
    print(f"Hello {name},{location}")
    print(f"How do you do {name}?")


greet_with_name(name="soubhik",location="kolkata")

l = ["L","K"]


def calculate_love_score(name_1, name_2):
    count_true = 0
    count_love = 0
    for i in name_1.lower():
        if i == "t":
            count_true += 1
        elif i == "r":
            count_true += 1
        elif i == "u":
            count_true += 1
        elif i == "e":
            count_true += 1
    for i in name_2.lower():
        if i == "t":
            count_true += 1
        elif i == "r":
            count_true += 1
        elif i == "u":
            count_true += 1
        elif i == "e":
            count_true += 1
    for i in name_1.lower():
        if i == "l":
            count_love += 1
        elif i == "o":
            count_love += 1
        elif i == "v":
            count_love += 1
        elif i == "e":
            count_love += 1
    for i in name_2.lower():
        if i == "l":
            count_love += 1
        elif i == "o":
            count_love += 1
        elif i == "v":
            count_love += 1
        elif i == "e":
            count_love += 1
    print(f"LOVE SCORE = {count_true}{count_love}")


calculate_love_score("Kanye west", "Kim kardashian")
