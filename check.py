from exception_class import *


class Check:
    """Клетка шахматной доски"""

    def __init__(self, check, figure=None):
        self.__x = 0
        self.__y = 0
        self.__figure = figure
        self.set_check(check)

    def get_check(self):
        """Возвращает строковое представление клетки"""
        return chr(self.__x + ord("a")) + str(self.__y + 1)

    def set_check(self, check):
        """Устанавливает координаты клетки"""
        if type(check) == str:
            if not ("a" <= check[:1] <= "h" and "1" <= check[1:] <= "8"):
                raise InputException(
                    "Неверные данные",
                    __class__.__name__,
                    self.set_check.__name__
                )
            first = check[:1]
            self.__x = ord(first) - ord("a")
            self.__y = int(check[1:]) - 1
        else:
            self.__x = check[0]
            self.__y = check[1]

    @property
    def figure(self):
        """Расположенная на клетке фигура"""
        return self.__figure

    @property
    def x(self):
        """Координата клетки по горизонтали"""
        return self.__x

    @property
    def y(self):
        """Координата клетки по вертикали"""
        return self.__y

    @figure.setter
    def figure(self, figure):
        """Устанавливает фигуру на клетку доски"""
        self.__figure = figure

    def __eq__(self, other):
        return self.__x == other.x and self.__y == other.y

    def __sub__(self, other):
        x = abs(self.__x - other.x)
        y = abs(self.__y - other.y)
        return Check(chr(x + ord("a")) + str(y + 1))

    # def __setattr__(self, key, value):
    #     raise AttributeError
