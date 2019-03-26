import sys
import spotipy
import spotipy.util as util

scope = 'playlist-modify-private'

if len(sys.argv) > 1:
    track = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token('anticraista', scope, 'aba114e12c4b474895556922ce1a572d',
                                   'e8abb96b0e514ffa803e3568c6cb8e56', 'http://migrmrz.wordpress.com/')

spotify = spotipy.Spotify(auth=token)

spotify.user_playlist_add_tracks(user="anticraista",
                                 playlist_id="spotify:user:anticraista:playlist:2zNMgSnwlCDBQFL8s7eA8z",
                                 tracks=[track])
