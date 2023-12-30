import requests
import datetime as dt

LAT = 39.231270
LNG = -84.377052

response1 = requests.get(url="http://api.open-notify.org/iss-now.json")
response1.raise_for_status()
data_iss = response1.json()

iss_latitude = float(data_iss["iss_position"]["latitude"])
iss_longitude = float(data_iss["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

parameters = {
  "lat": LAT,
  "lng": LNG,
  "formatted": 0,
  "tzId": "America/Detroit"
}

response2 = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response2.raise_for_status()
data_me = response2.json()
sunrise = data_me['results']['sunrise'].split("T")[1].split(":")
sunset = data_me['results']['sunset'].split("T")[1].split(":")

rise_list = [''.join(sunrise[0 : 2])]
set_list = [''.join(sunset[0 : 2])]
sunrise_num = int(rise_list[0])
sunset_num = int(set_list[0])
print(sunrise_num, sunset_num)

now = str(dt.datetime.now()).split(" ")[1].split(":")
now_list = [''.join(now[0 : 2])]
now_num = int(now_list[0])
print(now_list, now_num)

if now_num < sunrise_num or now_num > sunset_num:
  print("dark")
else:
  print("not dark")

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



