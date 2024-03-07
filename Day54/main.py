from flask import Flask

app = Flask(__name__)


def make_bold(func):
  def wrapper():
    return f"<b>{func()}</b>"
  return wrapper

def make_italic(func):
  def wrapper():
    return f"<em>{func()}</em>"
  return wrapper

def make_underlined(func):
  def wrapper():
    return f"<u>{func()}</u>"
  return wrapper


@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"


@app.route("/bye")
@make_bold
@make_underlined
@make_italic
def bye():
  return "Bye!"

