import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(
    client_id='aba114e12c4b474895556922ce1a572d',
    client_secret='e8abb96b0e514ffa803e3568c6cb8e56'
)

spotify = spotipy.Spotify(
    client_credentials_manager=client_credentials_manager
)

artist_uri = str(input())

results = spotify.artist_albums(artist_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])
