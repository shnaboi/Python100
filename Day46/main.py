from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import jwt

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
                        scope='playlist-modify-public')

# token_info = SPOTIFY_URI_RETURN

# Get the token
token_info = sp_oauth.get_access_token(as_dict=False)
# print(token_info)
# # Decode the access token
# decoded_token = jwt.decode(token_info, algorithms=['HS256'], verify=False)
#
# # Print the decoded token information
# print("decode: ", decoded_token)

# Create a Spotipy instance using the obtained token
sp = spotipy.Spotify(auth=token_info)

# Create Playlist
playlist_name = 'PYTEST'

playlist = sp.user_playlist_create(user=USER_ID, name=playlist_name, public=False)

playlist_id = playlist['id']

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

  song = (song_raw.replace('\n', '').replace('\t', '').replace("'", "")).replace('"', '').lower()
  artist = artist_raw.replace('\n', '').replace('\t', '').replace("'", "").replace('"', '').lower()

  # catch if artist name contains extra characters which make the search invalid
  if "featuring" in artist:
    artist = artist.split("featuring")[0].strip()
  if "," in artist:
    artist = artist.split(",")[0].strip()

  new_data = {f"{x+1}": {
    "song": song,
    "artist": artist
  }}
  top_100_dict.update(new_data)

# search for song
def find_and_add_track(song):
  song_title = song['song']
  song_artist = song['artist']
  query = f'track:"{song_title}" artist:"{song_artist}"'
  result = sp.search(q=query, limit=1, type="track", market='ES')
  print(f"results: {result}")
  # artist_name = result['tracks']['items'][0]['album']['artists'][0]['name']
  try:
    artist_uri = result['tracks']['items'][0]['album']['artists'][0]['uri']
    track_uri = [result['tracks']['items'][0]['uri']]
    print(track_uri)
  except IndexError:
    return

  add_song_to_playlist(track_uri)
  return

def add_song_to_playlist(uri):
  sp.playlist_add_items(playlist_id, uri)

for hit in top_100_dict:
  print(top_100_dict[hit])
  hit_data = top_100_dict[hit]
  find_and_add_track(hit_data)

# add items to playlist
# playlist_add_items(playlist_id, items, position=None)
# items - a list of track/episode URIs or URLs

# print(find_track(top_100_dict['1']))