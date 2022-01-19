import threading
import random
import time


class Thread(threading.Thread):
    def __init__(self, function, name):
        threading.Thread.__init__(self)
        self.__function = function
        self.__name = name

    def run(self):
        """Точка входа для потока"""
        # print(f"{self.__function.__name__} is starting")
        # запуск доверенной функции
        self.__function()
        # создание имитации работы
        # amount = random.randint(1, 10)
        # time.sleep(amount)
        # print(f"{self.__function.__name__} is ending")

    def join(self, *args):
        """Завершение потока"""
        threading.Thread.join(self, *args)
        # print(f"{self.__name} is ending")
