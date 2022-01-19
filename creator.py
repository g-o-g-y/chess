from abc import ABC, abstractmethod
from chess_figures import *


class Creator(ABC):
    @abstractmethod
    def factory_method(self, check, name, colour):
        """Возвращает объект необходимого типа"""
        pass

    def creating(self, check, name, colour):
        """Сообщает о создании объекта"""
        print(f"Создание объекта {name}")
        return self.factory_method(check, name, colour)


class QuineCreator(Creator):
    def factory_method(self, check, name, colour):
        """Возвращает объект необходимого типа"""
        return Queen(check, colour)


class BishopCreator(Creator):
    def factory_method(self, check, name, colour):
        """Возвращает объект необходимого типа"""
        return Bishop(check, colour)


class RookCreator(Creator):
    def factory_method(self, check, name, colour):
        """Возвращает объект необходимого типа"""
        return Rook(check, colour)
