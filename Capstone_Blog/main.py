from flask import Flask, request, render_template
import requests

app = Flask(__name__)

blog_post_api = "https://api.npoint.io/674f5423f73deab1e9a7"
response = requests.get(blog_post_api)
response.raise_for_status()
blog_data = response.json()
print(blog_data)

# render homepage when server is started
@app.route('/')
def home():
  return render_template("./index.html", blog_data=blog_data)

@app.route('/about')
def about():
  return render_template('./about.html')

@app.route('/contact', methods=['POST', 'GET'])
def contact():
  if request.method == 'POST':
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']
    print(f"{name}, {phone}, {email}, {message}")
    return render_template("./contact.html", msg_sent=True)
  return render_template('./contact.html', msg_sent=False)

# get_blog_post(x) is called as an href (when clicked) on the html doc,
# when the <a href=""> is generated, it passes through the id of the correct blog post

# @app.route('/contact', methods=['POST', 'GET'])
# def data_sent():
#   if request.method == 'POST':
#     name = request.form['name']
#     email = request.form['email']
#     phone = request.form['phone']
#     message = request.form['message']
#     return render_template("./contact.html")

@app.route('/post/<post_num>')
def get_blog_post(post_num):
  blog_post = 'None'
  num = int(post_num)
  for blog in blog_data:
    if blog["id"] == num:
      blog_post = blog
  print(blog)

  return render_template("./post.html", blog=blog_post)

if __name__ == "__main__":
  app.run(debug=True)

