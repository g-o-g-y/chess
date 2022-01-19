from figure import Figure, motion_decorator, wraps, logger
from check import *


class PositiveMixin:
    """Подбадривающий класс"""
    def cheer(self):
        """Подбадривает игрока"""
        print('У тебя получится выиграть, верь в себя')


class Bishop(Figure):
    """Фигура Слон"""
    def __init__(self, check, colour):
        super().__init__(check, "B", colour)

    def is_moving_possible(self, check):
        """Проверяет возможность хода в указанную клетку"""
        new_check = Check(check) - Check(super().check)
        if new_check.y == new_check.x:
            # Генерация исключения для подачи сигнала
            raise ConditionalException


class Rook(Figure):
    """Фигура Ладья"""
    def __init__(self, check, colour):
        super().__init__(check, "R", colour)

    def is_moving_possible(self, check):
        """Проверяет возможность хода в указанную клетку"""
        new_check = Check(check) - Check(super().check)
        if new_check.y == 0 or new_check.x == 0:
            # Генерация исключения для подачи сигнала
            raise ConditionalException


# Множественное наследование: Поведение королевы наследуется от ладьи и слона
# Также используется класс-миксин
class Queen(Bishop, Rook, PositiveMixin):
    """Фигура Королева"""
    def __init__(self, check, colour):
        Figure.__init__(self, check, "Q", colour)

    # @motion_decorator
    # def move_to(self, check):
    #     """Отображает передвижение фигуры"""
    #     # Проверка возможности хода
    #     try:
    #         self.is_moving_possible(check)
    #     except ConditionalException:
    #         print(f"{self.__name}{self.__check}—{check}")
    #         self.__check = check
    #     else:
    #         raise InputException(
    #             "Фигура не может быть передвинута в заданную клетку",
    #             self.move_to.__name__
    #         )
    #
    # @motion_decorator
    # def capture_fg(self, check):
    #     """Отображает взятие фигуры"""
    #     # Проверка возможности хода
    #     try:
    #         self.is_moving_possible(check)
    #     except ConditionalException:
    #         print(f"{self.__name}{self.__check}x{check}")
    #         self.__check = check
    #         self.cheer()
    #     else:
    #         raise InputException(
    #             "Фигура не может быть передвинута в заданную клетку",
    #             self.capture_fg.__name__
    #         )

    def is_moving_possible(self, check):
        """Проверяет возможность хода в указанную клетку"""
        # Генерация исключения для подачи сигнала
        Bishop.is_moving_possible(self, check)
        Rook.is_moving_possible(self, check)


