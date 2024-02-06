from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.billboard.com/charts/hot-100/2001-05-10/")
website = response.text

soup = BeautifulSoup(website, "html.parser")
# print(soup)

# song_names = soup.find_all(name="h3", class_="c-title")
# print(song_names)

song_names = soup.select("div div ul li ul li h3")
artist_names = soup.find_all(name="span", class_="a-no-trucate")
print(len(song_names), len(artist_names))

top_100_dict = {}
for x in range(len(song_names)):
  song_raw = song_names[x].get_text()
  artist_raw = artist_names[x].get_text()

  song = song_raw.replace('\n', '').replace('\t', '')
  artist = artist_raw.replace('\n', '').replace('\t', '')

  new_data = {f"{x+1}": {
    "song": song,
    "artist": artist
  }}
  top_100_dict.update(new_data)

print(top_100_dict)