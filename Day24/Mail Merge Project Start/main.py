#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('./Input/Names/invited_names.txt') as names_file:
  names = names_file.readlines()
  print(names)
  for name in names:
    raw_name = name.replace("\n", "")
    with open(f"./Output/ReadyToSend/invite_{raw_name}.txt", mode='w') as final:
      final.write(
      f"""Dear {raw_name},

      You are invited to my birthday this Saturday.

      Hope you can make it!

      Angela"""
      )