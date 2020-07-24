import spotipy
import config

client_credentials_manager = config.spotify_client_credentials

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
