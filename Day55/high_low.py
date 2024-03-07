from flask import Flask

app = Flask(__name__)

gif = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZXc5d3hna3FxNDFzcDZrZG00NHhvdTBpbXM2MGpjaG8ybmRldG00MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LfbDxyQIWtzLTtMnc0/giphy.gif"

@app.route("/")
def homepage():
  html = f"""
  <h1>Higher / Lower Guessing Game<h1>
  <img src={gif}>
  """
  return html

