from facade import Interface, ABC, abstractmethod


class Game(ABC):
    def __init__(self, interface):
        self.__game = interface

    @abstractmethod
    def execute(self):
        pass

    @property
    def game(self):
        return self.__game


class GameStart(Game):
    def __init__(self, interface):
        super().__init__(interface)

    def execute(self):
        self.game.start()


class MakeCapture(Game):
    def __init__(self, interface, check_from, check_to):
        super().__init__(interface)
        self.__check_from = check_from
        self.__check_to = check_to

    def execute(self):
        self.game.make_capture(self.__check_from, self.__check_to)


class MakeMove(Game):
    def __init__(self, interface, check_from, check_to):
        super().__init__(interface)
        self.__check_from = check_from
        self.__check_to = check_to

    def execute(self):
        self.game.make_move(self.__check_from, self.__check_to)


class GameEnd(Game):
    def __init__(self, interface):
        super().__init__(interface)

    def execute(self):
        self.game.end()
