from chess import *
from GUI import gui_start, gui_end
import asyncio
from db import *


def log_reader():
    """Считывает информацию о проделанных ходах
    из log.txt"""
    f = open('log.txt', 'r')
    last_lines = f.readlines()
    last_lines[0] = ""
    lines = ""
    for line in last_lines:
        lines += line
    f.close()
    return lines


class Singleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


class Interface(metaclass=Singleton):
    def start(self):
        loop = asyncio.get_event_loop()
        tasks = [
            loop.create_task(self.__greeting()),
            loop.create_task(self.__initialization())
        ]
        loop.run_until_complete(asyncio.wait(tasks))
        loop.close()

    async def __greeting(self):
        self.__start = time.time()
        [self.__name, self.__color] = gui_start()
        await asyncio.sleep(1)
        f = open('log.txt', 'w')
        f.close()
        logger(f"Игрок: {self.__name}, цвет: {self.__color}")

    async def __initialization(self):
        self.__chessboard = Chessboard()
        print("Шахматная доска уже готова к игре!")
        await asyncio.sleep(1)

    def make_capture(self, check_from, check_to):
        try:
            self.__chessboard.make_capture(check_from, check_to)
        except InputException as e:
            print(e)

    def make_move(self, check_from, check_to):
        try:
            self.__chessboard.make_move(check_from, check_to)
        except InputException as e:
            print(e)

    def sys_back(self, board):
        self.__chessboard.board = board

    def end(self):
        game_result = random.randint(0, 1)
        logger(f"Результат: {'Победа' if game_result == 1 else 'Поражение'}")
        save_game_in_db(
            self.__name,
            self.__color,
            f"{'Победа' if game_result == 1 else 'Поражение'}",
            time.time() - self.__start,
            log_reader()
        )
        gui_end(game_result)
