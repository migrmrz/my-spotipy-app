import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id='aba114e12c4b474895556922ce1a572d',
                                                      client_secret='e8abb96b0e514ffa803e3568c6cb8e56')
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = 'Radiohead'

results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']
if len(items) > 0:
    artist = items[0]
    print(artist['name'], artist['images'][0]['url'])
