import datetime
import sqlite3
from sqlite3 import Error

global sqlite_connection


def save_game_in_db(name_of_gamer, color, game_result, game_duration, game_history):
    try:
        global sqlite_connection
        # Подключение к БД и создание таблицы
        sqlite_connection = sqlite3.connect('sqlite_python_chess.db')
        sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS chess_table (
                                       id INTEGER PRIMARY KEY autoincrement,
                                       name_of_gamer TEXT NOT NULL,
                                       color TEXT NOT NULL,
                                       game_result TEXT NOT NULL,
                                       game_duration datetime NOT NULL,
                                       game_date datetime NOT NULL,
                                       game_history TEXT NOT NULL);'''
        cursor = sqlite_connection.cursor()
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        print("База данных подключена к SQLite, таблица создана")
        # Внесение результатов игры в таблицу
        sqlite_insert_query = """INSERT INTO chess_table
        (name_of_gamer, color, game_result, game_duration, game_date, game_history) 
        VALUES(?, ?, ?, ?, ?, ?);"""
        data_tuple = (name_of_gamer, color, game_result, game_duration, datetime.datetime.now(), game_history)
        cursor.execute(sqlite_insert_query, data_tuple)
        sqlite_connection.commit()
        cursor.close()

    except Error:
        print("Ошибка при подключении к sqlite", Error)

    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQlite закрыто")
