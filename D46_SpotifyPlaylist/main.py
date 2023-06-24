from bs4 import BeautifulSoup
import requests
from spotipy.oauth2 import SpotifyOAuth
import spotipy

# Spotify App Credentials
c_id = "a45705dbd8914b88a6d27cc2ae6d67e3"
c_pass = "a8353da3fac74b138a5d03b192582424"



user_in = input("What year you would like to travel to? [YYY-MM-DD format] : ")
response = requests.get(
    url=f"https://www.billboard.com/charts/hot-100/{user_in}/")

billboard = response.text

# creating a soup
soup = BeautifulSoup(billboard, 'html.parser')

# finding titles of each song.
spans_titles = soup.find_all(
    name="h3", id="title-of-a-story", class_="u-line-height-125")
    # returns a list of all the h3 tags with specified id

# creating a list of the song title
song_titles = [title.getText().strip() for title in spans_titles[0:100]]


# url retrieved from Spotify Dev Dashboard->user Settings
REDIRTCT_URL = "http://example.com"

# using spotipy for authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth
                     (client_id=c_id,
                      client_secret=c_pass,
                      redirect_uri=REDIRTCT_URL,
                      scope="user-library-read",
                      cache_path="token.txt")
                     )

# Get the current user dictionary
user = sp.current_user()  # Get detailed profile information about the current user
user_id = user["id"]

# Extracting Song URIs from the Spotify.
song_uris = []
year = user_in.split("-")[0]
for song in song_titles:

    # Finding songs
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


# creating a new playlist
playlist = sp.user_playlist_create(
    user=user_id, name=f"{user_in} Billboard 100", public=False, description='Python Playlist')

# adding tracks to playlist
result = sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


print("created Successfully")
