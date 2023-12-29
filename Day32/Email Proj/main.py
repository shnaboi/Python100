import random
import smtplib
# Documentation: https://docs.python.org/3/library/smtplib.html
import datetime as dt
# Documentation: https://docs.python.org/3/library/datetime.html
import pandas

my_email = "johms69420@gmail.com"
password = "jodl kdhm umwq lgmb"
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
today = (month, day)

df = pandas.read_csv('./birthdays.csv')
today_bdays = df[(df["month"] == month) & (df['day'] == day)]

if today_bdays.empty:
  pass
else:
  birthday_dict = today_bdays.to_dict(orient='records')
  for bday in birthday_dict:
    name = bday["name"]
    email = bday["email"]
    letter_num = random.randint(1, 3)
    print(letter_num)
    with open(f"./letter_templates/letter_{letter_num}.txt", mode="r") as letter:
      message = letter.readlines()
      msg = ''.join(message)
      named_message = msg.replace("[NAME]", name)
      print(named_message)
      with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
          from_addr=my_email,
          to_addrs=email,
          msg=f"Subject:Happy Birthday\n\n"
              f"{named_message}"
        )
