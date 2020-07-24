import sys
import spotipy
import config

if len(sys.argv) > 1:
    search = sys.argv[1]
else:
    print("Usage: %s search_str" % (sys.argv[0],))
    sys.exit()

client_credentials_manager = config.spotify_client_credentials

spotify = spotipy.Spotify(
    client_credentials_manager=client_credentials_manager
)

results = spotify.search(q=search, market="MX")
items = results['tracks']['items']
if len(items) > 0:
    for item in items:
        song = item['name']
        album = item['album']['name']
        artist = item['artists'][0]['name']
        print(song + ", " + album + ", " + artist)
# Devuelve coincidencias tanto en canción como en álbumes
