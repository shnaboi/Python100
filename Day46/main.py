from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

SPOTIFY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')
SPOTIFY_URI_RETURN = os.environ.get('SPOTIFY_URI_RETURN')

SPOTIFY_PRINTED_TOKEN = os.environ.get('SPOTIFY_PRINTED_TOKEN')
SPOTIFY_REDIRECT_URI = os.environ.get('SPOTIFY_REDIRECT_URI')
USER_ID = 'beefyboy10'

print(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_URI_RETURN, SPOTIFY_PRINTED_TOKEN, SPOTIFY_REDIRECT_URI)

# Set up OAuth handler
sp_oauth = SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                        client_secret=SPOTIFY_CLIENT_SECRET,
                        redirect_uri=SPOTIFY_REDIRECT_URI,
                        scope='playlist-modify-private playlist-modify-public')

# Get the token
token_info = sp_oauth.get_access_token(as_dict=False)

# Create a Spotipy instance using the obtained token
sp = spotipy.Spotify(auth=token_info)

# Fetch the current user's playlists
playlists = sp.current_user_playlists()

# Create Playlist
playlist_name = 'PYTEST'

playlist = sp.user_playlist_create(user=USER_ID, name=playlist_name, public=False)

playlist_id = playlist['id']

print(playlists)

response = requests.get("https://www.billboard.com/charts/hot-100/2001-05-10/")
website = response.text

soup = BeautifulSoup(website, "html.parser")

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