import time
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for count in range(1, word_count+1):
            f.write(f'Какое-то слово № {count}\n')
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


func_start = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

func_end = time.time()

print(f"Время выполнения функций - {func_end - func_start}")

th_start = time.time()

th1 = Thread(target=write_words, args=(10, 'example5.txt'))
th2 = Thread(target=write_words, args=(30, 'example6.txt'))
th3 = Thread(target=write_words, args=(200, 'example7.txt'))
th4 = Thread(target=write_words, args=(100, 'example8.txt'))

th1.start()
th2.start()
th3.start()
th4.start()

th1.join()
th2.join()
th3.join()
th4.join()

th_end = time.time()

print(f"Время выполнения потоков - {th_end - th_start}")