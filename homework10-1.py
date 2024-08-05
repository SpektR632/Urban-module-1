from threading import Thread
import time
from datetime import datetime
def wite_words(word_count, file_name):

    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count+1):
            file.write(f"Какое-то слово № {i}\n")
            time.sleep(0.1)
        print(f"Завершилось запись в файл {file_name}")


time_start = datetime.now()

wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

time_end = datetime.now()

print(f"Работа потоков: {time_end-time_start}")

time_start = datetime.now()

thr_first = Thread(target=wite_words, args=(10, 'example5.txt'))

thr_second = Thread(target=wite_words, args=(30, 'example6.txt'))

thr_third = Thread(target=wite_words, args=(200, 'example7.txt'))

thr_fourth = Thread(target=wite_words, args=(100, 'example8.txt'))


thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()

time_end = datetime.now()

print(f"Работа потоков: {time_end-time_start}")