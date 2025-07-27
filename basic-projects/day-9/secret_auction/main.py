import art

print("Welcome to the Secret Auction Program!")
print(art.logo)

name_bid_dict = {}

name = input("What is your name? ")
bid_price = input("What is your bid price? $")

# Store the name and bid price in the dictionary

name_bid_dict[name] = bid_price

# Ask if there are any other bidders

other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").strip().lower()

while other_bidders == "yes":
    name = input("What is your name? ")
    bid_price = input("What is your bid price? $")
    
    # Store the name and bid price in the dictionary
    name_bid_dict[name] = bid_price
    
    # Ask if there are any other bidders
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").strip().lower()

if other_bidders == "no":
    print("Bidding has ended.")

# Find the highest bid

highest_bid = 0
highest_bidder = ""
for name, bid in name_bid_dict.items():
    bid = int(bid)
    if bid > highest_bid:
        highest_bid = bid
        highest_bidder = name
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")
# End of the auction program