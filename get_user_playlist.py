import spotipy
import config

client_credentials_manager = config.spotify_client_credentials

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
