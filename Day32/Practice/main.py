import smtplib
# Documentation: https://docs.python.org/3/library/smtplib.html
import datetime as dt
# Documentation: https://docs.python.org/3/library/datetime.html
import random

my_email = "johms69420@gmail.com"
password = "jodl kdhm umwq lgmb"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#   connection.starttls()
#   connection.login(user=my_email, password=password)
#   connection.sendmail(
#     from_addr=my_email,
#     to_addrs="beefyboy10@gmail.com",
#     msg="Subject:Howdy\n\n"
#     "This is the body"
#     )

now = dt.datetime.now()
# current time
year = now.year
month = now.month
weekday = now.weekday()
# weekday is integer where mon=0, sun=6

dob = dt.datetime(year=1996, month=5, day=10)
# created a date of birth object

print(weekday)

if now.weekday() == 3:
  with open("quotes.txt", mode="r") as quotes:
    quotelist = [quote for quote in quotes]
    chosen_quote = random.choice(quotelist)
  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
      from_addr=my_email,
      to_addrs="beefyboy10@gmail.com",
      msg=f"Subject:Daily Motivation\n\n"
          f"{chosen_quote}"
      )
