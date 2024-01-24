# This class is responsible for searching for iata codes and flight prices
import os
import requests

TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
TEQUILA_ID = "shnaboishnaflightprices"
TEQUILA_HEADER = {
  "apikey": TEQUILA_API_KEY
}
class FlightSearch:
  def __init__(self):
    pass
  def get_iata_code(self, city):
    params = {
      "term": city
    }
    response = requests.get(url="https://api.tequila.kiwi.com/locations/query", params=params, headers=TEQUILA_HEADER)
    response.raise_for_status()
    data = response.json()
    code = data["locations"][0]["code"]
    return code

tequila_params = {
  "fly_from": "(city code)",
  "fly_to": "(multiple city codes)",
  "date_from": "DD/MM/YYY",
  "date_to": "DD/MM/YYYY",
  "limit": 15
}

params = {
  "fly_from": "CVG",
  "date_from": "02/04/2024",
  "date_to": "03/04/2024",
  "limit": 2
}
t_response = requests.get(url=TEQUILA_ENDPOINT, params=params, headers=TEQUILA_HEADER)
t_response.raise_for_status()
print(t_response.text)