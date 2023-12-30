import requests
import datetime as dt
import smtplib
import time

my_email = "johms69420@gmail.com"
password = "jodl kdhm umwq lgmb"

LAT = 39.231270
LNG = -84.377052
parameters = {
  "lat": LAT,
  "lng": LNG,
  "formatted": 0,
  "tzId": "America/Detroit"
}

def iss_pos():
  response1 = requests.get(url="http://api.open-notify.org/iss-now.json")
  response1.raise_for_status()
  data_iss = response1.json()

  iss_latitude = float(data_iss["iss_position"]["latitude"])
  iss_longitude = float(data_iss["iss_position"]["longitude"])

  if (LAT - 5) < iss_latitude < (LAT + 5) and (LNG - 5) < iss_longitude < (LNG + 5):
    return True

def is_dark():
  response2 = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
  response2.raise_for_status()
  data_me = response2.json()
  sunrise = data_me['results']['sunrise'].split("T")[1].split(":")
  sunset = data_me['results']['sunset'].split("T")[1].split(":")

  rise_list = [''.join(sunrise[0 : 2])]
  set_list = [''.join(sunset[0 : 2])]
  sunrise_num = int(rise_list[0])
  sunset_num = int(set_list[0])

  now = str(dt.datetime.now()).split(" ")[1].split(":")
  now_list = [''.join(now[0 : 2])]
  now_num = int(now_list[0])

  if now_num < sunrise_num or now_num > sunset_num:
    return True

while True:
  time.sleep(60)
  if iss_pos() and is_dark():
    with smtplib.SMTP("smtp.gmail.som") as connection:
      connection.starttls()
      connection.login(user=my_email, password=password)
      connection.sendmail(
        from_addr=my_email,
        to_addrs="shane.karner@gmail.com",
        msg=f"Subject:ISS is overhead!\n\n"
            f"Look up!"
      )
  else:
    pass
