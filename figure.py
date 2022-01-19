from abc import ABC, abstractmethod
from exception_class import *
from functools import wraps


def motion_decorator(function):
    """Регистрирует вызовы функций перемещения фигур"""
    # Копирование имени, документации и сигнатуры функции
    @wraps(function)
    def wrapper(self, check):
        # Обозначение начала выполнения, вывод цвета
        print(f"Начало нового хода: {self.colour} figures")
        function(self, check)
        # Обозначение конца выполнения
        print("Информация о ходе предоставлена")
    return wrapper


def logger(st):
    f = open('log.txt', 'a')
    f.write(st + '\n')
    f.close()


# Абстрактный класс
class Figure(ABC):
    """Имитирует некоторую фигуру"""
    def __init__(self, check, name="F", colour=''):
        self.__check = check
        self.__name = name
        self.__colour = colour

    @motion_decorator
    def move_to(self, check):
        """Отображает передвижение фигуры"""
        # Проверка возможности хода
        try:
            self.is_moving_possible(check)
        except ConditionalException:
            # При получении сигнала функциональность выполняется
            st = f"{self.__name}{self.__check}--{check}"
            logger(st)
            print(st)
            self.__check = check
        else:
            raise InputException(
                "Фигура не может быть передвинута в заданную клетку",
                __class__.__name__,
                self.move_to.__name__
            )

    @motion_decorator
    def capture_fg(self, check):
        """Отображает взятие фигуры"""
        # Проверка возможности хода
        try:
            # Проверка генерации сигнального исключения
            self.is_moving_possible(check)
        except ConditionalException:
            # При получении сигнала функциональность выполняется
            st = f"{self.__name}{self.__check}x{check}"
            logger(st)
            print(st)
            self.__check = check
        else:
            raise InputException(
                "Фигура не может быть передвинута в заданную клетку",
                __class__.__name__,
                self.capture_fg.__name__
            )

    # Абстрактный метод
    @abstractmethod
    def is_moving_possible(self, check):
        """Проверяет возможность хода в указанную клетку"""
        pass

    @property
    def check(self):
        """Значение поля фигуры"""
        return self.__check

    @property
    def name(self):
        """Название фигуры"""
        return self.__name

    @property
    def colour(self):
        """Цвет фигуры"""
        return self.__colour

    @check.setter
    def check(self, check):
        """Установить поле фигуры"""
        self.__check = check

    # @colour.setter
    # def colour(self, colour):
    #     """Установить цвет фигуры"""
    #     self.__colour = colour

    def __eq__(self, other):
        return self.__name == other.name
