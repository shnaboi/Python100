class FlightData:
  #This class is responsible for structuring the flight data.
  def __init__(self):
    pass

  def organize_data(self, data):
    city_name = data[0]['cityTo'].lower()
    organized_data = {
      "price": data[0]['price'],
      "origin_city": data[0]['cityFrom'],
      "origin_airport": data[0]['flyFrom'],
      "dest_city": data[0]['cityTo'],
      "dest_airport": data[0]['flyTo'],
      "depart_date": data[0]['route'][0]['local_departure'],
      "return_date": data[0]['route'][-1]['local_arrival']
    }
    setattr(self, city_name, organized_data)
