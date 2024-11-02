import pprint

import requests


ACCESS_TOKEN = "kGl_hDVDJtXoINMFXwCov0yASFog4Hg1vsq_GXKPvMPSflNuGDOIl8dEmHjTuw0a"
RANDOM_GENRE_API_URL = "https://binaryjazz.us/wp-json/genrenator/v1/genre/"
GENIUS_API_URL = "https://api.genius.com/search"
GENIUS_URL = "https://genius.com"

genre = requests.get(RANDOM_GENRE_API_URL).json()

data = requests.get(GENIUS_API_URL, params={'access_token': ACCESS_TOKEN, 'q': "Пожары"}).json()
pprint.pprint(data)
song_id = data['response']['hits'][0]['result']['api_path']
print(GENIUS_URL + song_id)
