# with open("weather_data.csv") as data_file:
#   data = data_file.readlines()
#   # data is a list of all lines
#
# # You can also do import csv
#
# import csv
#
# with open("weather_data.csv") as data_file:
#   data = csv.reader(data_file)
#   # data is a csv object that has rows and columns
#   # for row in data:
#   #   # print(row)
#   #   # this returns every row as a list
#   # After looping through each row once, the file pointer is at the end of the file
#   # So there are no more rows to read through
#   # You can use data_file.seek(0) to move the file pointer back to the start
#   # Or you can save data as a list: data = list(csv.reader(data_file))
#
#   # data_file.seek(0)
#   temperatures = []
#   for row in data:
#     temperatures.append(row[1])
#
#   # print(temperatures)
#
# # Everything is alot easier using pandas
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data)
# # print(data["temp"])
# # ^^^ This prints the entire temp row
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# # turns the temp row into a list
# print(temp_list)
#
# avg = sum(temp_list) / len(temp_list)
# print(avg)
#
# # or you can just do this
#
# print(data["temp"].mean())
#
# print(data["temp"].max())
#
# # pandas is even smarter, you can do this
# # it recognizes each column by the title.
#
# print(data.temp.max())
# # ^^^Get data in a column
#
# # Get data in a Row
# print(data[data.day == "Monday"])
#
# # When we use bracket notation, we are giving a condition, the condition met (row) is returned
# print(data[data.temp == data.temp.max()])
# # ^^^ Find value in temp column that is the max temp and return that row
#
# monday = data[data.day == "Monday"]
# # get monday row
# monday_temp = monday.temp[0]
# # create variable with monday's temp value in the monday row
#
# # create a dataframe form scratch
# # say you have a dictionary
# stud_dict = {
#   "students": ["Amy", "James", "Angela"],
#   "scores": [76, 56, 65]
# }
# data3 = pandas.DataFrame(stud_dict)
# # pass stud_dict into pandas.DataFrame and set that obj as variable called data3
# data3.to_csv("new_data.csv")
# # create a csv file from data3 obj
#
# # Find how many black, gray and cinnamon squirrels are in squirrel csv

import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
black = 0
gray = 0
cinnamon = 0
for color in squirrel_data["Primary Fur Color"]:
  if color == "Black":
    black += 1
  elif color == "Gray":
    gray += 1
  elif color == "Cinnamon":
    cinnamon += 1

print(f"Black: {black}, Gray: {gray}, Cinnamon: {cinnamon}")

# or you can do all of this simpler

print(squirrel_data["Primary Fur Color"] == "Gray")
# ^^^ Find the Primary Fur Color column, and return boolean for every entry that == "Gray"

print(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
# ^^^ This returns every row for every data entry of "Gray" in the Primary Fur Color column

print(len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]))
# ^^^ This returns the length of every data entry of "Gray" in the Primary Fur Color column
# (so the amount of gray squirrels)

print(len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]))
print(len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]))
# ^^^ Print the amount of black and cinnamon squirrels

# Now let's create a dict and data frame & csv with this info

cinnamon = (len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]))
black = (len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]))
gray = (len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]))

squirrel_dict = {
  "Fur Color": ["Gray", "Cinnamon", "Black"],
  "Count": [gray, cinnamon, black]
}
# Create dict with our fur color findings

squirrel_df = pandas.DataFrame(squirrel_dict)
# ^^^ Create pandas data frame from our dict
squirrel_df.to_csv("squirrel_count.csv")
# ^^^ Create csv file from the data frame which came from our dict
