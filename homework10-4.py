from random import randint
from threading import Thread
import queue
from time import sleep


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))



class Cafe:
    def __init__(self, *args):
        self.queue = queue.Queue()
        self.tables = args

    def guest_arrival(self, *guests):
        for guest in guests:
            if any(True for i in self.tables if i.guest is None):
                table = [i for i in self.tables if i.guest is None][0]
                print(f"{guest.name} сел(-а) за стол номер {table.number}")
                table.guest = guest
                guest.start()
            else:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(False for i in self.tables if i.guest):
            for table in (i for i in self.tables if i.guest):
                if table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушел(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None
                if not self.queue.empty():
                    table.guest = self.queue.get()
                    print(f"{table.guest.name} вышел(-ла) из очереди сел(-а) за стол номер {table.number}")
                    table.guest.start()

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
