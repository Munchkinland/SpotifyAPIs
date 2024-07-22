import os
import pandas as pd
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Autenticación con la API de Spotify
sp = Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv('SPOTIPY_CLIENT_ID'),
    client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
    redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
    scope='playlist-read-private,playlist-read-collaborative,user-top-read'
))

# Función para obtener los top tracks de un mercado específico
def get_top_tracks(market, limit=10):
    results = sp.search(q='genre:pop', type='track', market=market, limit=limit)
    tracks = []
    for item in results['tracks']['items']:
        track = {
            'name': item['name'],
            'artist': item['artists'][0]['name'],
            'album': item['album']['name'],
            'popularity': item['popularity'],
            'market': market,
            'type': 'track'
        }
        tracks.append(track)
    return tracks

# Función para obtener los top playlists de un mercado específico
def get_top_playlists(market, limit=10):
    results = sp.search(q='genre:pop', type='playlist', market=market, limit=limit)
    playlists = []
    for item in results['playlists']['items']:
        playlist = {
            'name': item['name'],
            'owner': item['owner']['display_name'],
            'tracks': item['tracks']['total'],
            'market': market,
            'type': 'playlist'
        }
        playlists.append(playlist)
    return playlists

# Función para obtener los top artists de un mercado específico
def get_top_artists(market, limit=10):
    results = sp.search(q='genre:pop', type='artist', market=market, limit=limit)
    artists = []
    for item in results['artists']['items']:
        artist = {
            'name': item['name'],
            'followers': item['followers']['total'],
            'popularity': item['popularity'],
            'market': market,
            'type': 'artist'
        }
        artists.append(artist)
    return artists

# Mercados para obtener los datos
markets = ['US', 'GB', 'CA', 'DE', 'FR']

# Lista para almacenar todos los datos
all_data = []

# Obtener y guardar datos en una lista
for market in markets:
    tracks = get_top_tracks(market)
    playlists = get_top_playlists(market)
    artists = get_top_artists(market)

    all_data.extend(tracks)
    all_data.extend(playlists)
    all_data.extend(artists)

    print(f'Datos recopilados para el mercado: {market}')

# Convertir la lista a un DataFrame
all_data_df = pd.DataFrame(all_data)

# Guardar todos los datos en un único archivo CSV
all_data_df.to_csv('spotify_top_data.csv', index=False)

print('Datos guardados en spotify_top_data.csv')
