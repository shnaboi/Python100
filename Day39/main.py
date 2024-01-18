#This file will need to use
# DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.
import requests
import os
import datetime as dt


"""
Google Sheet Data Management - https://sheety.co/

Kiwi Partners Flight Search API (Free Signup, Credit Card not required) - https://partners.kiwi.com/

Tequila Flight Search API Documentation - https://tequila.kiwi.com/portal/docs/tequila_api

Twilio SMS API - https://www.twilio.com/docs/sms
"""

SHEETY_ENDPOINT = "https://api.sheety.co/82235a205924c90499f09a2066926078/flightDealsApp/flights"

TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
TEQUILA_ID = "shnaboishnaflightprices"
TEQUILA_HEADER = {
  "apikey": TEQUILA_API_KEY
}

tequila_params = {
  "fly_from": "(city code)",
  "fly_to": "(multiple city codes)",
  "date_from": "DD/MM/YYY",
  "date_to": "DD/MM/YYYY",
  "limit": 15
}

params = {
  "fly_from": "FRA",
  "date_from": "02/04/2024",
  "date_to": "03/04/2024",
  "limit": 2
}
t_response = requests.get(url=TEQUILA_ENDPOINT, params=params, headers=TEQUILA_HEADER)
t_response.raise_for_status()
print(t_response.text)