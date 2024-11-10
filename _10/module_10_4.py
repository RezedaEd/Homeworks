from queue import Queue
import time
import threading
import random

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(threading.Thread):
    def __init__(self, guest_name):
        threading.Thread.__init__(self)
        self.guest_name = guest_name

    def run(self):
        time.sleep(random.randint(3,10))

class Cafe:
    def __init__(self, *tables):
        self.tables = set(tables)
        self.queue_at_cafe = Queue()

    def guest_arrival(self, *guests):
        free_tables = [table for table in self.tables if table.guest == None]
        for guest in guests:
            if free_tables:
                table = free_tables.pop(0)
                table.guest = guest
                guest.start()
                print(f'{guest.guest_name} сел(-а) за стол номер {table.number}')
            else:
                self.queue_at_cafe.put(guest)
                print(f'{guest.guest_name} ожидает в очереди.')

    def discuss_guests(self):
        while not self.queue_at_cafe.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest != None and not table.guest.is_alive():
                    print(f'{table.guest.guest_name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен.')
                    table.guest = None
                if table.guest == None and not self.queue_at_cafe.empty():
                    next_guest = self.queue_at_cafe.get()
                    table.guest = next_guest
                    next_guest.start()
                    print(f"{next_guest.guest_name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")


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