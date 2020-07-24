import sys
import spotipy
import config

if len(sys.argv) > 1:
    track = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = config.user_token

spotify = spotipy.Spotify(auth=token)

spotify.user_playlist_add_tracks(
    user="anticraista",
    playlist_id="spotify:user:anticraista:playlist:2zNMgSnwlCDBQFL8s7eA8z",
    tracks=[track])
