from flask import Flask, render_template
import requests
import random
import datetime as dt

# Use genderize.io API and agify.io API
genderize_API = "https://api.genderize.io?"
agify_API = "https://api.agify.io?"

app = Flask(__name__)

@app.route("/")
def home():
  random_num = random.randint(69, 420)
  year = dt.datetime.now().year
  year_str = str(year)
  return render_template("server.html", num=random_num, year=year_str)

if __name__ == "__main__":
  app.run()

