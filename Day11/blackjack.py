# from replit import clear
import os
# for Windows
if os.name == 'nt':
  os.system('cls')
# for Unix / Linux / Mac
else:
  os.system('clear')
import random

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# endgame_msg = f"You have {user_arg} & CPU has {cpu_arg}.\n"

def check_reset(flag):
  reset = input("Would you like to play again? Type y or n \n")
  if reset == 'y':
    os.system('clear')
    blackjack()
  elif reset == 'n':
    flag = False
    print("Goodbye")

def check_ace(hand):
  if sum(hand) > 21:
    for card in hand:
      if card == 11:
        index = hand.index(card)
        hand[index] = 1
        print(f"Ace card becomes 1. Your cards are {hand}. Total is {sum(hand)}")
  else:
    return

def check_win(user_arg, cpu_arg, flag):
  win = False
  if user_arg == 21:
    print(f"You have {user_arg} & CPU has {cpu_arg}.\nYou Win!")
    win = True
  elif cpu_arg == 21:
    print(f"You have {user_arg} & CPU has {cpu_arg}.\nYou lose!")
    win = True
  elif cpu_arg > 21:
    print(f"You have {user_arg} & CPU has {cpu_arg}.\nYou Win!")
    win = True
  elif user_arg > 21:
    print(f"You have {user_arg} & CPU has {cpu_arg}.\nYou lose!")
    win = True

  return
  # elif user_arg > cpu_arg:
  #   print(f"You have {user_arg} & CPU has {cpu_arg}.\nYou Win!")
  #   win = True
  # elif user_arg == cpu_arg:
  #   print(f"You have {user_arg} & CPU has {cpu_arg}.\nTie!")
  #   win = True
  # else:
  #   print(f"You have {user_arg} & CPU has {cpu_arg}.\nYou lose!")
  #   win = True
  # if win == True:
  #   check_reset(flag)

def blackjack():
  keep_playing = True
  while keep_playing == True:
    hitting = True
    user_cards = [random.choice(deck), random.choice(deck)]
    cpu_cards = [random.choice(deck), random.choice(deck)]
    user = sum(user_cards)
    cpu = sum(cpu_cards)

    check_win(user, cpu, keep_playing)
  
    # if user == 21:
    #   if cpu == 21:
    #     print('You have 21. Tie!')
    #     reset = input("Would you like to play again? Type y or n \n")
    #   print('You have 21, you win!')
    #   reset = input("Would you like to play again? Type y or n \n")
    # if cpu == 21:
    #   print('CPU has 21. You lose!')
    #   reset = input("Would you like to play again? Type y or n \n")
  
    print(f'CPUs cards: {cpu_cards[0]} & {cpu_cards[1]} \nTotal: {cpu}')
  
    while hitting and user < 21:
      draw_again = input(f"Your cards: {user_cards} \nTotal: {user} \nWould you like to draw a card? Type y for another card\n")
      if draw_again == 'y':
        user_cards.append(random.choice(deck))
        user = sum(user_cards)
        print(user_cards)
        card_amount = int(len(user_cards) - 1)
        check_ace(user_cards)
        # if user > 21:
        #   reset = input(f"You drew {user_cards[card_amount]} for a total of {user}. You lose! \nWould you like to play again? Type y or n \n")
      else:
        hitting = False
        while cpu < 17:
          cpu_hit = random.choice(deck)
          cpu += cpu_hit

    check_win(user, cpu, keep_playing)

    check_reset(keep_playing)

blackjack()

# Create a check_win() function to be called 
# keep playing while loop is not working