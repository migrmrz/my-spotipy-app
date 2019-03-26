import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(
    client_id='aba114e12c4b474895556922ce1a572d',
    client_secret='e8abb96b0e514ffa803e3568c6cb8e56'
)

spotify = spotipy.Spotify(
    client_credentials_manager=client_credentials_manager
)

results = spotify.user_playlist(
    user="anticraista",
    playlist_id="spotify:user:anticraista:playlist:2zNMgSnwlCDBQFL8s7eA8z"
)

playlist_name = results['name']
print(playlist_name + "\n")

items = results['tracks']['items']
if len(items) > 0:
    for item in items:
        song = item['track']['name']
        album = item['track']['album']['name']
        artist = item['track']['artists'][0]['name']
        print(song + ", " + album + ", " + artist)
