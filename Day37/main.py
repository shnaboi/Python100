import requests
import os

USERNAME = "shnaboi"
TOKEN = os.environ.get("PIXELA_TOKEN")
HEADERS = {
  "X-USER-TOKEN": TOKEN
}
graph_link = "https://pixe.la/v1/users/shnaboi/graphs/test1.html"

# pixela_user_create = "https://pixe.la/v1/users"
#
# pixela_user_params = {
#   "token": "m9&8*o00Qb7H##2Ky2+9n2I",
#   "username": "shnaboi",
#   "agreeTermsOfService": "yes",
#   "notMinor": "yes"
# }
#
# response = requests.post(url=pixela_user_create, json=pixela_user_params)
# print(response.text)

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

print(TOKEN)