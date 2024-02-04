import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
movie_list = []

for mov in soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH"):
  movie_list.append(mov.get_text())

print(movie_list)

file = "movie_list.txt"

with open(file, 'w') as txt_file:
  for mov in movie_list:
    txt_file.write(f"{mov}\n")

