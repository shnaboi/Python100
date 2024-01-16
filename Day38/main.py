import requests
import os

APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
HEADER = {
  "x-app-id": APP_ID,
  "x-app-key": API_KEY
}

print(HEADER)

NUTRITIONIX_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'

exercise_params = {
  "query": input("Describe your workout:\n"),
  "age": int(input("What is your age?\n"))
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=exercise_params, headers=HEADER)
response.raise_for_status()
print(response.json())