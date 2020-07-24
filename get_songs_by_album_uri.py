import spotipy
import config

client_credentials_manager = config.spotify_client_credentials

spotify = spotipy.Spotify(
    client_credentials_manager=client_credentials_manager
)

album_uri = str(input())

results = spotify.album_tracks(album_uri)
tracks = results['items']
while results['next']:
    results = spotify.next(results)
    tracks.extend(results['items'])

for track in tracks:
    print(track['name'])
