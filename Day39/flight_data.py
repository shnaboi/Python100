class FlightData:
  #This class is responsible for structuring the flight data.
  def __init__(self):
    pass

  def organize_data(self, data):
    city_name = data['data'][0]['cityTo']
    setattr(self, f"{city_name}_price", data['data'][0]['price'])


  # create data for price, departure airport code, departure city