from threading import Thread, Event
import random
import time
from queue import Queue


class Bun(Thread):
    def __init__(self, queue, stop_event):
        super().__init__()
        self.queue = queue
        self.stop_event = stop_event

    def run(self):
        while self.stop_event.is_set():
            time.sleep(0.5)
            if random.random() >= 0.8:
                self.queue.put("Подгорелая булка")
            else:
                self.queue.put("Хорошая булка")


class Cutlet(Thread):
    def __init__(self, queue, count, stop_event):
        super().__init__()
        self.queue = queue
        self.count = count
        self.stop_event = stop_event

    def run(self):
        while self.count:
            print(self.queue.qsize())
            bun = self.queue.get()
            if bun == "Хорошая булка":
                time.sleep(random.randint(1, 3))
                self.count -= 1
            print(f"Осталось приготовить {self.count} булок")
        self.stop_event.clear()


queue = Queue(maxsize=10)
stop_event = Event()
stop_event.set()

t1 = Bun(queue, stop_event)
t2 = Cutlet(queue, 10, stop_event)

t1.start()
t2.start()

t1.join()
t2.join()
