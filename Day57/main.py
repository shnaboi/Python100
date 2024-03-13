from flask import Flask, render_template
import requests
import random
import datetime as dt

# Use genderize.io API and agify.io API
genderize_API = "https://api.genderize.io?"
agify_API = "https://api.agify.io?"

# gender_response = requests.get(url=f"{genderize_API}name={}")
# gender_response.raise_for_status()
# shane1 = gender_response.json()
#
# age_response = requests.get(url=f"{agify_API}name={}")
# age_response.raise_for_status()
# shane2 = age_response.json()

# print(shane1, shane2)

app = Flask(__name__)

@app.route("/")
def home():
  random_num = random.randint(69, 420)
  year = dt.datetime.now().year
  year_str = str(year)
  return render_template("server.html", num=random_num, year=year_str)

@app.route("/<name>")
def name_results(name):
  gender_response = requests.get(url=f"{genderize_API}name={name}")
  gender_response.raise_for_status()
  gender_json = gender_response.json()
  age_response = requests.get(url=f"{agify_API}name={name}")
  age_response.raise_for_status()
  age_json = age_response.json()
  random_num = random.randint(69, 420)

  return render_template("server.html",
                         num=random_num,
                         name_gender=gender_json['gender'],
                         name_age=age_json['age'],
                         name=name)

@app.route("/blog")
def blog_posts():
  response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
  response.raise_for_status()
  blog_data = response.json()
  return render_template("blog.html", blogs=blog_data)

if __name__ == "__main__":
  app.run()

