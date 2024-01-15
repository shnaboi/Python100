import requests
import os
import datetime as dt

USERNAME = "shnaboi"
TOKEN = os.environ.get("PIXELA_TOKEN")
HEADERS = {
  "X-USER-TOKEN": TOKEN
}
now = dt.datetime.now()
date = now.strftime("%Y%m%d")

graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"
graph_body_req = {
  "id": "test1",
  "name": "test1 Graph",
  "unit": "Good Days",
  "type": "int",
  "color": "momiji"
}

# response = requests.post(url=graph_endpoint, json=graph_body_req, headers=HEADERS)
# print(response.text)

post_pixel_endpoint = "https://pixe.la/v1/users/shnaboi/graphs/test1"
post_pixel_body = {
  "date": "20240114",
  "quantity": "1",
}

# response = requests.post(url=post_pixel_endpoint, json=post_pixel_body, headers=HEADERS)
# print(response.text)

update_pixel_endpoint = "https://pixe.la/v1/users/shnaboi/graphs/test1/20240115"
update_pixel = {
  "quantity": "0"
}

response = requests.delete(url=update_pixel_endpoint, headers=HEADERS)
print(response.text)