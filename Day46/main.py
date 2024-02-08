from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up OAuth handler
sp_oauth = SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                        client_secret=SPOTIFY_CLIENT_SECRET,
                        redirect_uri=SPOTIFY_REDIRECT_URI,
                        scope='playlist-modify-private playlist-modify-public')

# Get the token
token_info = sp_oauth.get_access_token(as_dict=False)

# Create a Spotipy instance using the obtained token
sp = spotipy.Spotify(auth=token_info)

# Example request: Fetch the current user's playlists
playlists = sp.current_user_playlists()

playlist_name = 'Generated Playlist'

playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)

playlist_id = playlist['id']

print(playlist_id, f"token = {token_info}")

response = requests.get("https://www.billboard.com/charts/hot-100/2001-05-10/")
website = response.text

soup = BeautifulSoup(website, "html.parser")
# print(soup)

# song_names = soup.find_all(name="h3", class_="c-title")
# print(song_names)

song_names = soup.select("div div ul li ul li h3")
artist_names = soup.find_all(name="span", class_="a-no-trucate")

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