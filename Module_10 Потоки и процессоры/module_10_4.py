import queue
import random
import time
from threading import Thread


class Table:
    def __init__(self, number):
        self.number = number
        self.quest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        wait_time = random.randint(3, 10)
        time.sleep(wait_time)


class Cafe:
    def __init__(self, *tables: Table):
        self.queue = queue.Queue()
        self.tables = list(tables)

    def guest_arrival(self, *quests: Guest):
        for quest in quests:
            for table in self.tables:
                if table.quest is None:
                    table.quest = quest
                    quest.start()
                    print(f"{quest.name} сел(-а) за стол номер {table.number}")
                    break
            else:
                self.queue.put(quest)
                print(f"{quest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any([table.quest is not None for table in self.tables]):
            for table in self.tables:
                if table.quest and not table.quest.is_alive():
                    print(f"{table.quest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.quest = None
                if not self.queue.empty() and table.quest is None:
                    table.quest = self.queue.get()
                    print(f"{table.quest.name} вышел(-ла) из очереди "
                          f"и сел(-а) за стол номер {table.number}")
                    table.quest.start()




tables = [Table(number) for number in range(1, 6)]

guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

guests = [Guest(name) for name in guests_names]

cafe = Cafe(*tables)

cafe.guest_arrival(*guests)

cafe.discuss_guests()



