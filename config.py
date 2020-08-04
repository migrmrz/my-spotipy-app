from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import os

client_id = os.environ.get("client_id")
client_secret = os.environ.get("client_secret")

spotify_client_credentials = SpotifyClientCredentials(
    client_id,
    client_secret
)

scope = 'playlist-modify-private'

user_token = util.prompt_for_user_token(
    'anticraista',
    scope,
    client_id,
    client_secret,
    'http://migrmrz.wordpress.com/')
