#This file will need to use
# DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.
import requests
import os
import datetime as dt
from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager

"""
Searching for Flights
The next step is to search for the flight prices from London (LON) to all the destinations in the Google Sheet. 
In this project, we're looking only for direct flights, that leave anytime between tomorrow and in 6 months (6x30days). 
We're also looking for round trips that return between 7 and 28 days in length. 
The currency of the price we get back should be in USD.
"""

# sheety_data = {
#   "flights": [
#     {
#       "city": "Paris",
#       "iataCode": "",
#       "lowestPrice": 54,
#       "id": 2
#     },
#     {
#       "city": "Berlin",
#       "iataCode": "",
#       "lowestPrice": 42,
#       "id": 3
#     },
#     {
#       "city": "Tokyo",
#       "iataCode": "",
#       "lowestPrice": 485,
#       "id": 4
#     },
#     {
#       "city": "Sydney",
#       "iataCode": "",
#       "lowestPrice": 551,
#       "id": 5
#     },
#     {
#       "city": "Istanbul",
#       "iataCode": "",
#       "lowestPrice": 95,
#       "id": 6
#     },
#     {
#       "city": "Kuala Lumpur",
#       "iataCode": "",
#       "lowestPrice": 414,
#       "id": 7
#     },
#     {
#       "city": "New York",
#       "iataCode": "",
#       "lowestPrice": 240,
#       "id": 8
#     },
#     {
#       "city": "San Francisco",
#       "iataCode": "",
#       "lowestPrice": 260,
#       "id": 9
#     },
#     {
#       "city": "Cape Town",
#       "iataCode": "",
#       "lowestPrice": 378,
#       "id": 10
#     }
#   ]
# }

data_man_obj = DataManager()
sheety_data = data_man_obj.get_travel_data()
# ^^^ get sheety data
print(f"sheety_data = {sheety_data}")

flight_search_obj = FlightSearch()
for flight in sheety_data:
  if flight["iataCode"] == "testing":
    flight["iataCode"] = flight_search_obj.get_iata_code(flight["city"])

data_man_obj.travel_data = sheety_data
data_man_obj.update_iata_code()

# TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")
# TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
# TEQUILA_ID = "shnaboishnaflightprices"
# TEQUILA_HEADER = {
#   "apikey": TEQUILA_API_KEY
# }
#
# tequila_params = {
#   "fly_from": "(city code)",
#   "fly_to": "(multiple city codes)",
#   "date_from": "DD/MM/YYY",
#   "date_to": "DD/MM/YYYY",
#   "limit": 15
# }
#
# params = {
#   "fly_from": "FRA",
#   "date_from": "02/04/2024",
#   "date_to": "03/04/2024",
#   "limit": 2
# }
# t_response = requests.get(url=TEQUILA_ENDPOINT, params=params, headers=TEQUILA_HEADER)
# t_response.raise_for_status()
# print(t_response.text)