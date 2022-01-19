from game import *


def execute(commands):
    for command in commands:
        command.execute()


if __name__ == '__main__':
    game = Interface()
    print(game)
    game = Interface()
    print(game)
    commands = list()
    commands.append(GameStart(game))
    commands.append(MakeMove(game, 'd1', 'e2'))
    commands.append(MakeMove(game, 'd8', 'e8'))
    # Фигура не сможет походить в заданном направлении
    commands.append(MakeMove(game, 'e2', 'd4'))
    # Клетки а9 не существует
    commands.append(MakeMove(game, 'e2', 'd9'))
    # В клетке а1 нет фигуры
    commands.append(MakeMove(game, 'b1', 'g8'))
    # Осуществление взятия
    commands.append(MakeCapture(game, 'e2', 'e8'))
    commands.append(GameEnd(game))
    execute(commands)


    '''game.make_move('d1', 'e2')
    game.make_move('d8', 'e8')
    # Фигура не сможет походить в заданном направлении
    game.make_move('e2', 'd4')
    # Клетки а9 не существует
    game.make_move('e2', 'd9')
    # В клетке а1 нет фигуры
    game.make_move('b1', 'g8')
    # Осуществление взятия
    game.make_capture('e2', 'e8')
    game.end()'''






