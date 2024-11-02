import requests
from threading import Thread
import time

URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre'
res = []

def get_text_from_url(url):

    page = requests.get(url)
    text = page.json()
    res.append(text)


start = time.time()


th1 = Thread(target=get_text_from_url, args=(URL, ))
th2 = Thread(target=get_text_from_url, args=(URL, ))
th3 = Thread(target=get_text_from_url, args=(URL, ))
th4 = Thread(target=get_text_from_url, args=(URL, ))
th5 = Thread(target=get_text_from_url, args=(URL, ))
th6 = Thread(target=get_text_from_url, args=(URL, ))
th7 = Thread(target=get_text_from_url, args=(URL, ))
th8 = Thread(target=get_text_from_url, args=(URL, ))
th9 = Thread(target=get_text_from_url, args=(URL, ))
th10 = Thread(target=get_text_from_url, args=(URL, ))

th1.start()
th2.start()
th3.start()
th4.start()
th5.start()
th6.start()
th7.start()
th8.start()
th9.start()
th10.start()

th1.join()
th2.join()
th3.join()
th4.join()
th5.join()
th6.join()
th7.join()
th8.join()
th9.join()
th10.join()

end = time.time()
print(end - start)
print(res)