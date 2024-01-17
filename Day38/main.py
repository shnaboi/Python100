import requests
import os
import datetime as dt

APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
NUTRITIONIX_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
HEADER = {
  "x-app-id": APP_ID,
  "x-app-key": API_KEY
}

SHEETY_KEY = os.environ.get("sheety_auth")

now = dt.datetime.now()
today = now.strftime("%m/%d/%Y")
now_time = now.strftime("%H:%M:%S")

exercise_params = {
  "query": input("Describe your workout:\n"),
  "age": int(input("What is your age?\n"))
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=exercise_params, headers=HEADER)
response.raise_for_status()
# print(response.json())
nutritionix_data = response.json()

sheety_endpoint = "https://api.sheety.co/82235a205924c90499f09a2066926078/myWorkoutsApp/workouts"

sheety_header = {
  "Authorization": SHEETY_KEY
}

sheety_data = {
  "workout": {
    "date": today,
    "time": now_time,
    "exercise": nutritionix_data['exercises'][0]['name'],
    "duration": nutritionix_data['exercises'][0]['duration_min'],
    "calories": nutritionix_data['exercises'][0]['nf_calories']
  }
}

print(sheety_data)

response_b = requests.post(url=sheety_endpoint, json=sheety_data, headers=sheety_header)
response_b.raise_for_status()
print(response_b.text)
