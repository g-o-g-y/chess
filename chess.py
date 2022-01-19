from chess_figures import *
from metaclass import DebugMeta
from threading_clases import *
import asyncio
from creator import *


def precondition_and_postcondition_checking(function):
    """Проверка пред- и постусловий"""
    # Копирование имени, документации и сигнатуры функции
    @wraps(function)
    def wrapper(self, check_from, check_to):
        # Проверка предусловий
        old_check = Check(check_from)
        new_check = Check(check_to)
        temp_figure = self.board[old_check.x][old_check.y].figure
        if temp_figure is None:
            raise InputException("В данной клетке нет фигуры", self.__class__.__name__, function.__name__)
        print("Предусловие корректно")
        function(self, check_from, check_to)
        # Проверка постусловий
        if self.board[old_check.x][old_check.y].figure is None \
                and self.board[new_check.x][new_check.y].figure == temp_figure \
                and self.board[new_check.x][new_check.y].figure.check == check_to:
            print("Постусловие корректно, смена хода\n_____________________")
        else:
            raise InputException("Постусловие некорректно", self.__class__.__name__, function.__name__)
    return wrapper


class Chessboard:
    '''(metaclass=DebugMeta):'''
    def __init__(self):
        self.__board: list = [Check] * 8
        for i in range(len(self.__board)):
            self.__board[i] = [Check] * 8
        for i in range(len(self.__board)):
            for j in range(len(self.__board)):
                self.__board[i][j] = Check([i, j])
        # time.sleep(4)
        # Создание потоков для инициализации различных фигур
        thread1 = Thread(self.__bishop_initialisation, "thread1")
        thread2 = Thread(self.__rook_initialisation, "thread2")
        thread3 = Thread(self.__queen_initialisation, "thread3")
        # Начало инициализации
        thread1.start()
        thread2.start()
        thread3.start()
        # Завершение потоков
        thread1.join()
        thread2.join()
        thread3.join()

    def __queen_initialisation(self):
        """Инициализация ферзей"""
        creator = QuineCreator()
        self.__board[3][0].figure = creator.creating(self.__board[3][0].get_check(), 'Q', 'white')
        self.__board[3][7].figure = creator.creating(self.__board[3][7].get_check(), 'Q', 'black')

    def __rook_initialisation(self):
        """Инициализация ладей"""
        creator = RookCreator()
        self.__board[0][0].figure = creator.creating(self.__board[0][0].get_check(), 'R', 'white')
        self.__board[0][7].figure = creator.creating(self.__board[0][7].get_check(), 'R', 'black')
        self.__board[7][0].figure = creator.creating(self.__board[7][0].get_check(), 'R', 'white')
        self.__board[7][7].figure = creator.creating(self.__board[7][7].get_check(), 'R', 'black')

    def __bishop_initialisation(self):
        """Инициализация слонов"""
        creator = BishopCreator()
        self.__board[2][0].figure = creator.creating(self.__board[2][0].get_check(), 'B', 'white')
        self.__board[2][7].figure = creator.creating(self.__board[2][7].get_check(), 'B', 'black')
        self.__board[5][0].figure = creator.creating(self.__board[5][0].get_check(), 'B', 'white')
        self.__board[5][7].figure = creator.creating(self.__board[5][7].get_check(), 'B', 'black')

    def __moving(self, check_from, check_to):
        """Изменяет положение фигур при передвижении по шахматной доске"""
        old_check = Check(check_from)
        new_check = Check(check_to)
        temp = self.__board[old_check.x][old_check.y].figure
        # temp.check = check_to
        self.__board[new_check.x][new_check.y].figure = temp
        self.__board[old_check.x][old_check.y].figure = None

    @precondition_and_postcondition_checking
    def make_move(self, check_from, check_to):
        """Осуществляет передвижение фигуры на шахматной доске"""
        old_check = Check(check_from)
        self.__board[old_check.x][old_check.y].figure.move_to(check_to)
        self.__moving(check_from, check_to)

    @precondition_and_postcondition_checking
    def make_capture(self, check_from, check_to):
        """Осуществляет взятие фигуры на шахматной доске"""
        old_check = Check(check_from)
        self.__board[old_check.x][old_check.y].figure.capture_fg(check_to)
        self.__moving(check_from, check_to)

    def get_figure(self, check):
        check = Check(check)
        if self.__board[check.x][check.y].figure is None:
            return 'Фигура отсутствует'
        return self.__board[check.x][check.y].figure.name

    @property
    def board(self):
        return self.__board

    @board.setter
    def board(self, board):
        self.__board = board
