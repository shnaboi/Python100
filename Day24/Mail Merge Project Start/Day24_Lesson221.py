file = open("file.txt")
contents = file.read()
# when done modifying
file.close()

# can do something similar like this

with open('file.txt') as file:
  contents = file.read()
  # file will close as soon as we're done modifying

# we can also write to the file like this, start by opening file
# the open method is set to read mode by default, change it to write with mode='w'


with open('file.txt', mode='w') as file:
  file.write("New text.")

# If you only want to ADD to the text, mode should be mode='a' for APPEND mode

with open('file.txt', mode='a') as file:
  file.append("\nNew text.")

# if the file does not exist when you use the with open() method, the file will be newly created (in write mode='w')

# This is a good resource:
# https://ioflood.com/blog/python-open-file/#:~:text=Python's%20open()%20function%20supports,reading%20and%20writing%20text%20files

