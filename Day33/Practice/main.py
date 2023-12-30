import requests
import datetime as dt

LAT = 39.231270
LNG = -84.377052

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# # ^^^This will catch errors with the response variable if there are any errors
#
# data = response.json()
# # response variable has json data and the HTTP status code, so we just need the json data
#
# print(data)
# # data is a dictionary with a bunch of ... data.
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# # in the data dict, return longitude and latitude data
#
# iss_position = (longitude, latitude)
# # create tuple with longitude and latitude data
#
# print(iss_position)

parameters = {
  "lat": LAT,
  "lng": LNG,
  "formatted": 0,
  "tzId": "America/Detroit"
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split("T")[1].split(":")
sunset = data['results']['sunset'].split("T")[1].split(":")
print(sunrise, sunset)

time_now = dt.datetime.now()
print(time_now)