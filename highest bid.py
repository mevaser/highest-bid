import art
print(art.logo)  # Print the logo from the 'art' module

bids = {}  # Dictionary to store bidder names and bids
continue_bidding = True

while continue_bidding:
    name = input("What is your name? ")
    price = int(input("What is your bid? "))
    bids[name] = price
    
    another_bid = input("Is there anyone else who wants to bid? (yes/no) ").lower()
    print(("\n") * 20)  # Clear the screen
    
    if another_bid == "yes":
        continue_bidding = True
    elif another_bid == "no":
        continue_bidding = False
        highest_bid = max(bids, key=bids.get)
        print(f"The highest bid is {bids[highest_bid]} by {highest_bid}.")
