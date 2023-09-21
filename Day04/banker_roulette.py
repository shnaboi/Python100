# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
# Split up the string into list items
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

num_names = len(names)

# select a random number between 0 and length of num_names
chosen = random.randint(0, num_names - 1)

print(names[chosen])