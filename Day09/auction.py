# clear() came from replit so code might be broken outside of it
# all it's supposed to do is clear the screen so no biggie

from art import logo
print(logo)

bids = {}
bidding_complete = False

def find_highest_bid(bid_history):
  highest_bid = 0
  winner = ''
  
  for bidder in bid_history:
    bid_amount = bid_history[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"{winner} wins with a bid of {highest_bid}")

while not bidding_complete:
  name = input("What is your name? ")
  price = int(input("What's your bid? $"))
  bids[name] = price
  end_auction = input("Are there any other bidders? Type yes or no \n")
  if end_auction == 'no':
    bidding_complete = True
    find_highest_bid(bids)
  elif end_auction == 'yes':
    clear()
