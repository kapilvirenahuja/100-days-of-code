import sys
sys.path.append("/Users/kapil/Code/learn/100-days-of-code")

from commons.helpers import clear
from auction_art import logo

bidders = {}
bidding_active = True


print(logo)

while bidding_active:
    name = input("What is your name? ")
    bid = input("What is your bid? $")

    bid = {
        "name": name,
        "bid": bid
    }
    bidders[name] = bid

    continue_bidding = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if continue_bidding == "no":
        bidding_active = False


highest_bid = 0
winner = ""
for bidder in bidders:
    bid_amount = int(bidders[bidder]["bid"])
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder

print(f"The winner is {winner} with a bid of ${highest_bid}")

# print all the losing bidders
for bidder in bidders:
    if bidder != winner:
        print(f"{bidder} lost with a bid of ${bidders[bidder]['bid']}")

