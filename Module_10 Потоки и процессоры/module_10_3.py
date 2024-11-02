from threading import Lock, Thread
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            num = random.randint(50, 500)
            self.balance += num
            if self.balance >= 1000 and self.lock.locked():
                print('\nблокировка снялась\n')
                self.lock.release()
            print(f"Пополнение: +{num}. Баланс: {self.balance}")
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            num = random.randint(50, 500)
            print(f'Запрос на {num}')
            if num <= self.balance:
                self.balance -= num
                print(f"Снятие: -{num}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            time.sleep(0.001)


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk, ))
th2 = Thread(target=Bank.take, args=(bk, ))

th1.start()
th2.start()
th1.join()
th2.join()

print(bk.balance)
