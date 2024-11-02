import pprint

import requests
from threading import Thread, Event
import queue

ACCESS_TOKEN = "kGl_hDVDJtXoINMFXwCov0yASFog4Hg1vsq_GXKPvMPSflNuGDOIl8dEmHjTuw0a"
RANDOM_GENRE_API_URL = "https://binaryjazz.us/wp-json/genrenator/v1/genre/"
GENIUS_API_URL = "https://api.genius.com/search"
GENIUS_URL = "https://genius.com"


class GetGenre(Thread):
    def __init__(self, queue, event):
        self.event = event
        self.queue = queue
        super().__init__()

    def run(self):
        while self.event.is_set():
            genre = requests.get(RANDOM_GENRE_API_URL).json()
            self.queue.put(genre)


class Genius(Thread):
    songs_list = []

    def __init__(self, queue, event, counter):
        self.queue = queue
        self.event = event
        self.counter = counter
        super().__init__()

    def run(self):
        while self.event.is_set():
            genre = self.queue.get()
            print(self.queue.qsize())
            data = requests.get(GENIUS_API_URL, params={'access_token': ACCESS_TOKEN, 'q': genre}).json()

            try:
                song_id = data['response']['hits'][0]['result']['api_path']
                if self.list_full():
                    event.clear()
                else:
                    self.songs_list.append(GENIUS_URL + song_id)
            except KeyError:
                self.run()
            except IndexError:
                self.run()

    def list_full(self):
        return self.counter < len(self.songs_list)


queue = queue.Queue()
counter = 100

event = Event()
event.set()


genre_list = []
genius_list = []

for i in range(6):
    t = GetGenre(queue, event)
    t.start()
    genre_list.append(t)

for i in range(10):
    t = Genius(queue, event, counter)
    t.start()
    genius_list.append(t)

for t in genius_list:
    t.join()

print(Genius.songs_list)
print(len(Genius.songs_list))




