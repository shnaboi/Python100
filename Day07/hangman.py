import random
from hangman_art import stages 
from hangman_art import logo
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#Print logo at start of game

print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
past_letters = []
display = []
for _ in range(word_length):
  display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    print(guess)

    # Check if letter was already guessed
    if guess in past_letters:
      print(f"You already guessed this. \nGuessed letters include: {''.join(past_letters)}")
    else:
      past_letters.append(guess)
    #Check if guessed letter is correct
      for position in range(word_length):
          letter = chosen_word[position]
          if letter == guess:
              display[position] = letter

      #Check if guessed letter is wrong.
      if guess not in chosen_word:
          lives -= 1
          print(f"You guessed {guess} which is not in the word.")
          if lives == 0:
              end_of_game = True
              print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])