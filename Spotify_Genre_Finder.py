import spotipy
import spotipy.util as util
import matplotlib.pyplot as plt

SPOTIPY_CLIENT_ID='youridhere'
SPOTIPY_CLIENT_SECRET ='yoursecrethere'
SPOTIPY_REDIRECT_URI ='http://localhost/'

username = input("Spotify Username: ")

token = util.prompt_for_user_token(username,
                                   scope='user-follow-read',
                                   client_id=SPOTIPY_CLIENT_ID,
                                   client_secret=SPOTIPY_CLIENT_SECRET,
                                   redirect_uri=SPOTIPY_REDIRECT_URI)

sp = spotipy.Spotify(auth=token)
following = int(sp.current_user_followed_artists()['artists']['total'])
genres = []

for x in range(following):
    artist = sp.current_user_followed_artists(limit=1,after=x*1)
    for i, name in enumerate(artist['artists']['items']):
        genre = name['genres']
        for item in genre:
            genres.append(item)

genres_dict = {i:genres.count(i) for i in genres}
genres = []
sizes = []

for key in genres_dict:
    genres.append(key)
    sizes.append(genres_dict[key])
    
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=genres, autopct='%.2f')
ax1.axis('equal')

plt.show()
