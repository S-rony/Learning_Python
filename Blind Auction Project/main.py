# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


from art import logo
print(logo)
print("Welcome to the secret auction program.")
secret_auction = {}
otherBidder = True

def higest_bidder(bidding_dic):
    max_key = None
    max_value = 0
    for key, value in bidding_dic.items():
        if value > max_value:
            max_value = value
            max_key = key
        # print(key, value)
    print(f"The winner is {max_key} with a bid of ${max_value}")


while otherBidder:
    key = input("What is your name?: ")
    value = int(input("What's your bid?: $"))
    # secret_auction[key] = value

    bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if bidders == "no":
        otherBidder = False
        secret_auction[key] = value
        higest_bidder(secret_auction)
    elif bidders == "yes":
        secret_auction[key] = value
        print("\n"*100)
# print(secret_auction)

