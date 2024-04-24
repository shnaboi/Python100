from flask import Flask, render_template, request
# import requests

app = Flask(__name__)

@app.route('/')
def home():
  return render_template("./index.html")

@app.route('/login', methods=["POST"])
def receive_form_data():
  username = request.form['username']
  password = request.form['password']
  # can return render_template() after login is successful
  return f"{username} - {password}"

if __name__ == "__main__":
  app.run(debug=True)
