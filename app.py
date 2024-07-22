import os
import pandas as pd
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
# Este archivo debe contener las credenciales de Spotify y otras configuraciones necesarias
load_dotenv()

# Autenticación con la API de Spotify
# Configura la autenticación OAuth con las credenciales obtenidas del archivo .env
sp = Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv('SPOTIPY_CLIENT_ID'),         # ID de cliente obtenido de Spotify Developer Dashboard
    client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'), # Secreto de cliente obtenido de Spotify Developer Dashboard
    redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),   # URI de redirección configurada en el Spotify Developer Dashboard
    scope='playlist-read-private,playlist-read-collaborative,user-top-read' # Permisos necesarios para leer datos de playlists y usuarios
))

# Función para obtener los top tracks de un mercado específico
def get_top_tracks(market, limit=10):
    """
    Obtiene los principales tracks del mercado especificado usando la API de Spotify.
    
    :param market: Código del mercado (país) para obtener datos. Ej. 'US' para Estados Unidos.
    :param limit: Número máximo de tracks a obtener.
    :return: Lista de diccionarios con información sobre cada track.
    """
    # Realiza una búsqueda en Spotify para obtener tracks del género pop en el mercado especificado
    results = sp.search(q='genre:pop', type='track', market=market, limit=limit)
    tracks = []
    # Itera sobre los resultados obtenidos
    for item in results['tracks']['items']:
        # Crea un diccionario con la información relevante de cada track
        track = {
            'name': item['name'],                      # Nombre del track
            'artist': item['artists'][0]['name'],      # Nombre del artista (primer artista en caso de múltiples)
            'album': item['album']['name'],            # Nombre del álbum
            'popularity': item['popularity'],          # Popularidad del track (0-100)
            'market': market,                          # Mercado en el que se obtuvieron los datos
            'type': 'track'                           # Tipo de dato (track)
        }
        # Añade el diccionario a la lista de tracks
        tracks.append(track)
    return tracks

# Función para obtener los top playlists de un mercado específico
def get_top_playlists(market, limit=10):
    """
    Obtiene las principales playlists del mercado especificado usando la API de Spotify.
    
    :param market: Código del mercado (país) para obtener datos. Ej. 'US' para Estados Unidos.
    :param limit: Número máximo de playlists a obtener.
    :return: Lista de diccionarios con información sobre cada playlist.
    """
    # Realiza una búsqueda en Spotify para obtener playlists del género pop en el mercado especificado
    results = sp.search(q='genre:pop', type='playlist', market=market, limit=limit)
    playlists = []
    # Itera sobre los resultados obtenidos
    for item in results['playlists']['items']:
        # Crea un diccionario con la información relevante de cada playlist
        playlist = {
            'name': item['name'],                      # Nombre de la playlist
            'owner': item['owner']['display_name'],    # Nombre del propietario de la playlist
            'tracks': item['tracks']['total'],         # Número total de tracks en la playlist
            'market': market,                          # Mercado en el que se obtuvieron los datos
            'type': 'playlist'                        # Tipo de dato (playlist)
        }
        # Añade el diccionario a la lista de playlists
        playlists.append(playlist)
    return playlists

# Función para obtener los top artists de un mercado específico
def get_top_artists(market, limit=10):
    """
    Obtiene los principales artistas del mercado especificado usando la API de Spotify.
    
    :param market: Código del mercado (país) para obtener datos. Ej. 'US' para Estados Unidos.
    :param limit: Número máximo de artistas a obtener.
    :return: Lista de diccionarios con información sobre cada artista.
    """
    # Realiza una búsqueda en Spotify para obtener artistas del género pop en el mercado especificado
    results = sp.search(q='genre:pop', type='artist', market=market, limit=limit)
    artists = []
    # Itera sobre los resultados obtenidos
    for item in results['artists']['items']:
        # Crea un diccionario con la información relevante de cada artista
        artist = {
            'name': item['name'],                      # Nombre del artista
            'followers': item['followers']['total'],   # Número total de seguidores del artista
            'popularity': item['popularity'],          # Popularidad del artista (0-100)
            'market': market,                          # Mercado en el que se obtuvieron los datos
            'type': 'artist'                          # Tipo de dato (artist)
        }
        # Añade el diccionario a la lista de artistas
        artists.append(artist)
    return artists

# Lista de mercados para obtener los datos
markets = ['US', 'GB', 'CA', 'DE', 'FR']

# Lista para almacenar todos los datos obtenidos
all_data = []

# Obtener datos para cada mercado y añadirlos a la lista
for market in markets:
    # Llama a las funciones para obtener tracks, playlists y artistas
    tracks = get_top_tracks(market)
    playlists = get_top_playlists(market)
    artists = get_top_artists(market)

    # Añade los datos obtenidos a la lista principal
    all_data.extend(tracks)
    all_data.extend(playlists)
    all_data.extend(artists)

    # Imprime un mensaje indicando que los datos para el mercado han sido recopilados
    print(f'Datos recopilados para el mercado: {market}')

# Convertir la lista de datos a un DataFrame de pandas
# Esto permite manipular y guardar los datos en formato tabular
all_data_df = pd.DataFrame(all_data)

# Guardar todos los datos en un único archivo CSV
# Este archivo CSV contendrá toda la información sobre tracks, playlists y artistas de los diferentes mercados
all_data_df.to_csv('spotify_top_data.csv', index=False)

# Imprime un mensaje indicando que los datos han sido guardados en el archivo CSV
print('Datos guardados en spotify_top_data.csv')
