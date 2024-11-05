import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            a = random.randint(50, 500)
            self.balance += a
            print(f'Пополнение: {a}. Баланс: {self.balance}.')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            a = random.randint(50, 500)
            print(f'Запрос на {a}.')
            if a <= self.balance:
                self.balance -= a
                print(f'Снятие: {a}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств.')
                self.lock.acquire()


bk = Bank()
thread_1 = threading.Thread(target=Bank.deposit, args=(bk,))
thread_2 = threading.Thread(target=Bank.take, args=(bk,))
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()


print(f'Итоговый баланс: {bk.balance}.')