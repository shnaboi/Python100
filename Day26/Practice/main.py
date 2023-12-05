# Day26 is all about list comprehension & Dictionary comprehension
numbers = [1, 2, 3]
new_list = [num + 1 for num in numbers]

range_list = [num * 2 for num in range(1,5)]
print(range_list)

# list = [new_item for item in list if test]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
cap_names = [name.upper() for name in names if len(name) >= 5]

print(cap_names)

# Dictionary comprehension

# new_dict = {new_key:new_value for (key,value) in dict.items()}
# or
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}
# ^^^ Syntax > .items() just returns all items in a dict or tuple

# You can generate a dict from a list
# new_dict = {new_key:new_value for item in list}

student_dict = {
  "student": ["Angela", "James", "Lily"],
  "score": [56, 76, 98]
}

import pandas

student_df = pandas.DataFrame(student_dict)
# create pandas data frame from dict

# Loop through dictionaries:
for (key, value) in student_dict.items():
  print(value)

# pandas has a method called iterrows to loop through rows of a data frame
for (index, row) in student_df.iterrows():
  print(row)

# You can create a dict from a data frame like this:
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}
