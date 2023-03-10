import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

client_id = os.getenv('spotifyclientid')
client_secret = os.getenv('spotifyclientsecret')

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_music(genre_name):
    try:
        genre = f"genre:{genre_name}"
        results = sp.search(q=genre, type='track')
        # print(results)
    except Exception as exc:
        print(exc)
    else:
        if not results['tracks']['items']:
            print("unavailable genre")
        else:
            for track in results['tracks']['items']:
                print(f"{track['name']} by {track['artists'][0]['name']}")
                print(f"Preview URL: {track['preview_url']}")


if __name__ == '__main__':
    get_music('rock')
