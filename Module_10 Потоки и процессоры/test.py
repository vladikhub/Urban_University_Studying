# import time
# from threading import Thread
#
#
# class Writer(Thread):
#     def __init__(self, word_count, file_name):
#         self.file_name = file_name
#         self.word_count = word_count
#         super().__init__()
#
#     def run(self):
#         with open(self.file_name, 'w', encoding='utf-8') as f:
#             for count in range(1, self.word_count + 1):
#                 f.write(f'Какое-то слово № {count}\n')
#                 time.sleep(0.1)
#         print(f"Завершилась запись в файл {self.file_name}")
#
# threads = []
# num_of_files = 8
# start_count = 30
# for i in range(1, num_of_files+1):
#     thread = Writer(start_count, f'example{i}.txt')
#     thread.start()
#     threads.append(thread)
#
# for i in threads:
#     i.join()
#     print(f"Записался файл {i.file_name}")
#
import time
# from threading import Thread
#
# x = 0
# def thread_task():
#     global x
#     for i in range(10_000_000):
#         x = x + 1
#
#
# def main():
#     global x
#     x = 0
#     th1 = Thread(target=thread_task)
#     th2 = Thread(target=thread_task)
#
#     th1.start()
#     th2.start()
#
#     th1.join()
#     th2.join()
#
#     print(x)
#
# main()
# main()
# main()
# main()
# main()
# main()
# main()


# import time
# import threading
#
# def some_func():
#     time.sleep(4)
#     raise Exception
#
#
# def excepthook(arg):
#     print(arg.thread.name)
#
#
# threading.excepthook = excepthook
# th1 = threading.Thread(target=some_func)
# th2 = threading.Thread(target=some_func)
#
# th1.start()
# th2.start()
#
# th1.join()
# th2.join()


# from threading import Thread, Event
#
#
# def first_worker():
#     print("Первый рабочий приступи к работе")
#     print('Первый рабочий ждет Второго')
#     event.wait()
#     print("Первый рабочий продолжил работу")
#     time.sleep(2)
#     print("Первый рабочий закончил!")
#
#
# def second_worker():
#     print("Второй рабочий приступил к работе")
#     time.sleep(5)
#     print("Второй рабочий закончил!")
#     event.set()
#
#
# event = Event()
#
# th1 = Thread(target=first_worker)
# th2 = Thread(target=second_worker)
#
# th1.start()
# th2.start()


import threading
import multiprocessing

count = 0


def first_worker(n):
    global count
    for i in range(n):
        count += 1


    print("Первый рабочий закончил прибавлять", count)


def second_worker(n):
    global count
    for i in range(n):
        count += 1


    print("Второй рабочий закончил прибавлять", count)

start = time.time()
th1 = threading.Thread(target=first_worker, args=(10**8,))
th2 = threading.Thread(target=second_worker, args=(10**7,))

th1.start()
th2.start()

th1.join()
th2.join()
end = time.time()
print(end - start)
# if __name__ == "__main__":
#     start = time.time()
#     mul1 = multiprocessing.Process(target=first_worker, args=(10**8, ))
#     mul2 = multiprocessing.Process(target=second_worker, args=(10**7, ))
#
#     mul1.start()
#     mul2.start()
#
#     mul2.join()
#     mul1.join()
#
#     end = time.time()
#     print(end - start)

