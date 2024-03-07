from flask import Flask
import random

app = Flask(__name__)

gif = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZXc5d3hna3FxNDFzcDZrZG00NHhvdTBpbXM2MGpjaG8ybmRldG00MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LfbDxyQIWtzLTtMnc0/giphy.gif"

def detect_route(func):
  def wrapper():
    pass
  return wrapper

num = random.randint(1, 9)
print(num)

num_string = f"/{num}"

# if app.route(f"/{num}"):
# #   html page needs to display you win
# #   else if you are higher or lower, the page needs to tell us

@app.route("/")
def homepage():
  html = f"""
  <h1>Higher / Lower Guessing Game<h1>
  <img src={gif}>
  <p>Change the number in the address bar to guess a number<p>
  """
  return html


# create func that has if statements to tell if number was guessed correct or high or low
@app.route("/<guess>")
def num_guess(guess):
  html = f"{guess}"
  # if
  #   html = f"""
  #     <h1>You guessed the correct answer! Reload the server to play again.</h1>
  #     """
  return html

