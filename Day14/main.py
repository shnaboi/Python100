from game_data import data
from art import logo, vs
import random

import os
if os.name == 'nt':
  os.system('cls')
else:
  os.system('clear')

def print_screen(game_boolean, points):
  os.system('clear')
  print(logo)
  if game_boolean == True:
    print(f"You're correct! Current score: {points}")
  else:
    print(f"Wrong! You lose! Final score: {points}")

def game():
  print(logo)
  score = 0
  game_over = False
  while game_over == False:
    if score == 0:
      a = random.choice(data)
      b = random.choice(data)
      a_name = a['name']
      b_name = b['name']
    else: 
      a = b
      a_name = b_name
      b = random.choice(data)
      b_name = b['name']
    if a['follower_count'] > b['follower_count']:
      answer = a_name
    else:
      answer = b_name
    # TWO INSTAGRAM ACCOUNTS AND THEIR DESCRIPTIONS
    user = input(f"Who has more instagram followers? \nA = {a_name}, a {a['description']} from {a['country']} \nor \nB = {b_name}, a {b['description']} from {b['country']} \n").lower()
    # TWO INSTAGRAM ACCOUNTS AND THEIR DESCRIPTIONS
    if user == 'a' and answer == a_name:
      correct = True
      score += 1
      print_screen(correct, score)
    elif user == 'b' and answer == b_name:
      correct = True
      score += 1
      print_screen(correct, score)
    else: 
      game_over = True
      correct = False
      
  print_screen(correct, score)
  play_more = input("Do you wish to play again? Type n to stop:\n")
  if play_more.lower() == 'n':
    print("Goodbye. \n")
    return
  else:
    game()
    return
        
game()
