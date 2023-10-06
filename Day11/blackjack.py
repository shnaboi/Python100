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
        if hand[0] == 0:
          return
        else:
          print(f"Ace card becomes 1.")
          return
  else:
    return
  
# def game_over(winner, flag, play):
#   flag = True
#   if winner:
#     print(f"You have {user} & CPU has {cpu}.\nYou Win!")
#     check_reset(play)
#   else:
#     print(f"You have {user} & CPU has {cpu}.\nYou lose!")
#     check_reset(play)

def check_win(user_arg, cpu_arg, play, hit):
  # win_flag = False
  # user_win = False
  # if win_flag == False:
  if user_arg == 21:
    # user_win = True
    print(f"You have 21! \nYou Win!")
    check_reset(play)
  elif cpu_arg == 21:
    # user_win = False
    print(f"You have {user_arg} & CPU has 21! \nYou lose!")
    check_reset(play)
  
  if hit:
    return
  elif cpu_arg > 21:
    print(f"You have {user_arg} & CPU has {cpu_arg}.\nYou Win!")
    check_reset(play)
  elif user_arg > 21:
    print(f"You have {user_arg} & CPU has {cpu_arg}.\nYou lose!")
    check_reset(play)
  elif user_arg == cpu_arg:
    print(f"You have {user_arg} & CPU has {cpu_arg}.\nIt's a tie!")
    check_reset(play)
  

  if user_arg > cpu_arg:
    print(f"You have {user_arg} & CPU has {cpu_arg}.\nYou Win!")
    win_flag = True
  elif user_arg == cpu_arg:
    print(f"You have {user_arg} & CPU has {cpu_arg}.\nTie!")
    win_flag = True
  else:
    print(f"You have {user_arg} & CPU has {cpu_arg}.\nYou lose!")
    win_flag = True
  if win_flag == True:
    check_reset(play)

def blackjack():
  keep_playing = True
  while keep_playing == True:
    hitting = True
    user_cards = [random.choice(deck), random.choice(deck)]
    cpu_cards = [0, random.choice(deck), random.choice(deck)]
    user = sum(user_cards)
    cpu = sum(cpu_cards)

    check_win(user, cpu, keep_playing, hitting)
  
    # Print below for testing
    # print(f'CPUs cards: {cpu_cards} \nTotal: {cpu}')
  
    while hitting and user < 21:
      draw_again = input(f"Your cards: {user_cards} \nTotal: {user} \nWould you like to draw a card? Type y for another card\n")
      if draw_again == 'y':
        user_cards.append(random.choice(deck))
        check_ace(user_cards)
        user = sum(user_cards)
        print(user_cards)
      else:
        hitting = False
        while cpu < 17:
          cpu_hit = random.choice(deck)
          check_ace(cpu_cards)
          cpu += cpu_hit
    hitting = False

    check_win(user, cpu, keep_playing, hitting)

    check_reset(keep_playing)

blackjack()

# Create a check_win() function to be called 
# keep playing while loop is not working