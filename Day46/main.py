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

# Set up OAuth handler
sp_oauth = SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                        client_secret=SPOTIFY_CLIENT_SECRET,
                        redirect_uri=SPOTIFY_REDIRECT_URI,
                        scope='playlist-modify-private playlist-modify-public')

# Get the token
token_info = sp_oauth.get_access_token(as_dict=False)

# Create a Spotipy instance using the obtained token
sp = spotipy.Spotify(auth=token_info)

# Create Playlist
# playlist_name = 'PYTEST'
#
# playlist = sp.user_playlist_create(user=USER_ID, name=playlist_name, public=False)
#
# playlist_id = playlist['id']

# def find_track(song):
#   song_title = song['song']
#   song_artist = song['artist']
#   result = sp.search(q='One Step Closer', limit=1, type="track")
#   artist_name = result['tracks']['items'][0]['album']['artists'][0]['name']
#   artist_uri = result['tracks']['items'][0]['album']['artists'][0]['uri']
#   track_uri = result['tracks']['items'][0]['uri']
#   print(artist_uri, track_uri)

# Search for song
result = sp.search(q='One Step Closer', limit=1, type="track")
artist_name = result['tracks']['items'][0]['album']['artists'][0]['name']
artist_uri = result['tracks']['items'][0]['album']['artists'][0]['uri']
track_uri = result['tracks']['items'][0]['uri']
print(artist_uri, track_uri)

# add items to playlist
# playlist_add_items(playlist_id, items, position=None)
# items - a list of track/episode URIs or URLs

# playlist_change_details(playlist_id, name=None, public=None, collaborative=None, description=None)
# playlist_id - the id of the playlist
# name - optional name of the playlist
# public - optional is the playlist public
# collaborative - optional is the playlist collaborative
# description - optional description of the playlist

# user_playlist_add_tracks(user, playlist_id, tracks, position=None)

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