from bs4 import BeautifulSoup

with open("website.html", encoding="UTF-8") as file:
  contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
print(soup.title.string)

all_anchor_tags = soup.find_all(name='a')
# find all anchor tags

for tag in all_anchor_tags:
  print(tag.getText())
# print all anchor tag text
  print(tag.get("href"))
# print link

heading = soup.find(name="h1", id="name")
# heading will equal any h1 tags with id of 'name', can also do this with class_ attribute
print(heading.getText(), heading.name, heading.get("id"))
# print returns content of h1 tag, h1, and name

company_url = soup.select_one(selector="p a")
print(company_url)
# company_url = the entire & 1st a tag inside the p tag

name = soup.select_one(selector="#name")
# selecting elements by css selector

heading_list = soup.select(selector=".heading")
# select all elements that have css class of heading, the var is a LIST
