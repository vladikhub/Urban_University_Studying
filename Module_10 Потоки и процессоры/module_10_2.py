from threading import Thread
import time


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        count_enemies = 100
        for i in range(1, 101):
            time.sleep(1)
            count_enemies -= self.power
            if count_enemies <= 0:
                print(f"{self.name} одержал победу спустя {i} дней(дня)!", end='\n')
                break
            print(f"{self.name} сражается {i} день(дня)..., осталось {count_enemies} воинов.")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")