import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user = input("R for rock, P for paper, S for scissors: ").lower()
bot = 0

bot_choice = random.randint(0, 2)
if bot_choice == 0:
    bot = 'r'
elif bot_choice == 1:
    bot = 'p'
else:
    bot = 's'

if user == bot:
    message = f"You both chose {user}. It's a tie. "
elif user == 'r':
    if bot == 'p':
        message = f"You chose rock, bot chose paper. You lose. "
    else:
        message = f"You chose rock, bot chose scissors. You Win! "
elif user == 'p':
    if bot == 'r':
        message = "You chose paper, bot chose rock. You lose. "
    else:
        message = "You chose paper, bot chose scissors. You Win! "
elif user == 's':
    if bot == 'r':
        message = "You chose scissors, bot chose rock. Loser! You lose! "
    else:
        message = "You chose scissors, bot chose paper. You Win! "    
print(message)