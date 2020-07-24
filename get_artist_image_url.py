import spotipy
import sys
import config

client_credentials_manager = config.spotify_client_credentials

spotify = spotipy.Spotify(
    client_credentials_manager=client_credentials_manager
)

if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = 'Radiohead'

results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']
if len(items) > 0:
    artist = items[0]
    print(artist['name'], artist['images'][0]['url'])
