class FlightSearch:
  def __init__(self):
    pass
  def flight_search(self, sheety_data):
    for flight in sheety_data["flights"]:
      if flight["iataCode"] == "":
        flight["iataCode"] = "testing"
        # use flight_search Obj to search for the iataCode and update sheety_data
        # at the end of for loop the sheety_data should be posted to google sheet
    print(sheety_data)
