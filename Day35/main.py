import requests
import os

API_KEY = os.environ.get("OWM_API_KEY")
LAT = 39.231270
LNG = -84.377052

weather_params = {
  "lat": LAT,
  "lon": LNG,
  "cnt": 6,
  "appid": API_KEY
}

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast",
                        params=weather_params)
response.raise_for_status()
data = response.json()

def check_tennis_weather():
  weather_codes = []
  bad_weather = 0
  for forecast in data["list"]:
    weather_codes.append(forecast["weather"][0]["id"])
  for code in weather_codes:
    if 781 > code >= 200:
      bad_weather += 1
  if bad_weather == 0:
    print("Good day for tennis!")
  elif bad_weather >= 3:
    print("Bad day for tennis")
    print(f"{int(bad_weather * 3)} hours of bad conditions reported.")
  else:
    print("Tennis might be possible")
    print(f"{int(bad_weather * 3)} hours of bad conditions reported.")

check_tennis_weather()
