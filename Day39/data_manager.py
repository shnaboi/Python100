#This class is responsible for talking to the Google Sheet.
import requests

SHEETY_ENDPOINT = "https://api.sheety.co/82235a205924c90499f09a2066926078/flightDealsApp/flights"

class DataManager:

  def __init__(self):
    self.travel_data = {}

  def get_travel_data(self):
    sheety_response = requests.get(url=SHEETY_ENDPOINT)
    sheety_data = sheety_response.json()
    self.travel_data = sheety_data["flights"]
    return self.travel_data
  def update_iata_code(self):
    # THIS UPDATES SHEETY IATA_CODE *AFTER* FLIGHT SEARCH OBJ UPDATES THE CODE IN MAIN.PY
    for flight in self.travel_data:

      updated_data = {
        "flight": {
          "iataCode": flight["iataCode"]
        }
      }
      # ^^^ set updated_data to the updated data from flight search obj
      response = requests.put(url=f"{SHEETY_ENDPOINT}/{flight['id']}", json=updated_data)
      response.raise_for_status()
      print(f"response = {response.text}")
