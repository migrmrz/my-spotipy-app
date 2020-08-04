from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import os

user = 'anticraista'
scope = 'playlist-modify-private'
client_id = os.environ.get("client_id")
client_secret = os.environ.get("client_secret")
redirect_uri = 'http://migrmrz.wordpress.com/'

spotify_client_credentials = SpotifyClientCredentials(
    client_id,
    client_secret
)

user_token = util.prompt_for_user_token(
    user,
    scope,
    client_id,
    client_secret,
    redirect_uri)
