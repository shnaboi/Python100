from flask import Flask
import random

app = Flask(__name__)

gif_start = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZXc5d3hna3FxNDFzcDZrZG00NHhvdTBpbXM2MGpjaG8ybmRldG00MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LfbDxyQIWtzLTtMnc0/giphy.gif"
gif_high = "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMDhvYmp4dW14OXhoeXl2ajRuMWYxOHV6ODl4OTMxbW5wM244NXB1NyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3s95JDGDKf24tfDDXv/giphy.gif"
gif_low = "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExYWdnazFhZHk5bzNtNzNndXJrbWloa3hzY2tkcDI4OHI3bzl0bHQ3YSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7bu56G2vRwulV3fa/giphy.gif"
gif_correct = "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTUzMHkzd3k2NHBmYXlieHRxMW5oeTE0YzBnY2I0MDR3cGszanZ1MiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fah08IDMr10VtDrcoh/giphy.gif"

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
  <img src={gif_start}>
  <p>Change the number in the address bar to guess a number<p>
  """
  return html


# create func that has if statements to tell if number was guessed correct or high or low
@app.route("/<guess>")
def num_guess(guess):
  if int(guess) == num:
    html = f"""
      <h1>You guessed the correct answer! Reload the server to play again.</h1>
      <img src={gif_correct}>
      """
  elif num < int(guess):
    html = f"""
      <h1>You're guess is too <strong>high</strong>.</h1>
      <img src={gif_high}>
      <p>Drink some water.</p>
      """
  else:
    html = f"""
      <h1>You're guess is too <strong>low</strong>.</h1>
      <img src={gif_low}>
      <p>You're cursed forever! Get haunted!</p>
      """
  return html

