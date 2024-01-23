import requests
SHEETY_ENDPOINT = "https://api.sheety.co/82235a205924c90499f09a2066926078/flightDealsApp/flights"
class FlightSearch:
  def __init__(self):
    pass
  def flight_search(self, sheety_data):
    for flight in sheety_data["flights"]:
      if flight["iataCode"] == "":
        flight["iataCode"] = "testing"
        # use flight_search Obj to search for the iataCode and update sheety_data
        # at the end of for loop the sheety_data should be posted to google sheet
        flight_data = {"flight": flight}
        data_2 = {'flight': {
          "iataCode": "testing"
          }
        }
        # print(flight_data, {flight_data['flight']['id']})
        response = requests.put(url=f"{SHEETY_ENDPOINT}/{flight_data['flight']['id']}", json=flight_data)
        response.raise_for_status()
        print(response.text)
    print(sheety_data)
