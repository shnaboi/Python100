import random

EASY = 10
HARD = 5

def game(): 
  lives = 0
  win = False
  num = random.choice(range(1, 100))
  level = input("Type h for hard (5 guesses) \nOr Type e for easy (10 guesses)")
  if level == 'h':
    lives = HARD
  elif level == 'e':
    lives = EASY
  while lives > 0:
    guess = int(input("Guess a number between 1 & 100: "))
    if guess < num:
      lives -= 1
      print(f"{guess} is too low. Guess higher.")
      print(f"You have {lives} guesses remaining.")
    elif guess > num:
      lives -= 1
      print(f"{guess} is too high. Guess lower")
      print(f"You have {lives} guesses remaining.")
    elif guess == num:
      win = True
      print(f"You win! The number is {num} \nYou win with {lives} remaining guesses")
      play_again = input("Do you wish to play again? \nType y to play, n to stop: ")
      if play_again == 'y':
        game()
        return
      elif play_again == 'n':
        print("Goodbye. ")
        return
    
  if lives == 0:
    print("Game Over.")
    play_again = input("Do you wish to play again? \nType y to play, n to stop: ")
    if play_again == 'y':
      game()
      return
    elif play_again == 'n':
      print("Goodbye. ")
      return
    
game()