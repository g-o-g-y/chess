from tkinter import Tk, RIGHT, BOTH, RAISED, LEFT, N, Text, X, TOP, BooleanVar, messagebox
from tkinter.ttk import *


class UI1(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.input_name = str()
        self.parent = parent
        self.init_first_ui()

    def init_first_ui(self):
        self.parent.title("ШАХМАТЫ")
        self.pack(fill=BOTH, expand=True)
        # Создание фрейма
        frame1 = Frame(self)
        frame1.pack(fill=X)
        # Создание меток и текстового поля
        entry1 = Entry(frame1, font=("Open Sans", 12))
        lbl1 = Label(frame1, text="Приветствуем в игре \"ШАХМАТЫ\"", font=("Open Sans", 12))
        lbl2 = Label(frame1, text="Пожалуйста, введите ваши имя и фамилию", font=("Open Sans", 12))
        lbl1.pack(side=TOP, padx=15, pady=5)
        lbl2.pack(side=TOP, padx=15, pady=5)
        entry1.pack(pady=15, expand=True)
        # Создание кнопок

        def get_entry(event):
            self.input_name = entry1.get()
            self.destroy()
            self.quit()

        def quit_bot(event):
            root = Tk()
            root.geometry("350x150+300+300")
            ex = UIquit(root, "Игра окончена!")
            root.mainloop()

        close_button = Button(self, text="Quit")
        close_button.pack(side=RIGHT, padx=5, pady=5)
        ok_button = Button(self, text="OK")
        ok_button.pack(side=RIGHT)
        # Добавление функциональности кнопке
        ok_button.bind('<Button-1>', get_entry)
        close_button.bind('<Button-1>', quit_bot)
        entry1.bind("<Return>", get_entry)


class UI2(Frame):
    def __init__(self, parent, name):
        Frame.__init__(self, parent)
        self.parent = parent
        self.input_color = str()
        self.name = name
        self.init_second_ui()

    def init_second_ui(self):
        self.parent.title("ШАХМАТЫ")
        self.pack(fill=BOTH, expand=True)
        # Создание фрейма
        frame1 = Frame(self)
        frame1.pack(fill=X)
        # Создание метки
        lbl1 = Label(frame1, text=f"Приветствуем, {self.name}", font=("Open Sans", 12))
        lbl2 = Label(frame1, text="Выберите цвет, за который будете играть", font=("Open Sans", 12))
        lbl1.pack(side=TOP, padx=15, pady=5)
        lbl2.pack(side=TOP, padx=15, pady=5)
        # Создание кнопок

        def set_write(event):
            self.input_color = "write"
            self.destroy()
            self.quit()

        def set_black(event):
            self.input_color = "black"
            self.destroy()
            self.quit()

        def quit_bot(event):
            root = Tk()
            root.geometry("350x150+300+300")
            ex = UIquit(root, "Игра окончена!")
            root.mainloop()

        write_button = Button(frame1, text="Write", width=20)
        write_button.pack(side=LEFT, padx=15, pady=15)
        write_button.bind('<Button-1>', set_write)
        black_button = Button(frame1, text="Black", width=20)
        black_button.pack(side=RIGHT, padx=15, pady=15)
        black_button.bind('<Button-1>', set_black)
        close_button = Button(self, text="Quit")
        close_button.pack(side=RIGHT, padx=5)
        close_button.bind('<Button-1>', quit_bot)


class UI3(Frame):
    def __init__(self, parent, game_result):
        Frame.__init__(self, parent)
        self.parent = parent
        self.input_color = str()
        self.game_result = game_result
        self.init_third_ui()

    def init_third_ui(self):
        self.parent.title("ШАХМАТЫ")
        self.pack(fill=BOTH, expand=True)
        # Создание фрейма
        frame1 = Frame(self)
        frame1.pack(fill=X)
        # Создание меток и текстового поля
        if self.game_result == 1:
            lbl1 = Label(frame1, text="Поздравляем с победой!", font=("Open Sans", 12))
        else:
            lbl1 = Label(frame1, text="К сожалению, вы проиграли", font=("Open Sans", 12))
        lbl2 = Label(frame1, text="Спасибо за игру!", font=("Open Sans", 12))
        lbl1.pack(side=TOP, padx=15, pady=5)
        lbl2.pack(side=TOP, padx=15, pady=5)
        # Создание кнопок
        close_button = Button(self, text="Quit game", command=exit, width=25)
        close_button.pack(padx=5, pady=20)


class UIquit(Frame):
    def __init__(self, parent, ex):
        Frame.__init__(self, parent)
        self.parent = parent
        self.input_color = str()
        self.ex = ex
        self.init_qu_ui()

    def init_qu_ui(self):
        self.parent.title("ШАХМАТЫ")
        self.pack(fill=BOTH, expand=True)
        # Создание фрейма
        frame1 = Frame(self)
        frame1.pack(fill=X)
        # Создание меток и текстового поля
        lbl1 = Label(frame1, text=self.ex, font=("Open Sans", 12))
        lbl1.pack(side=TOP, padx=15, pady=5)
        # Создание кнопок
        close_button = Button(self, text="Quit game", command=exit, width=25)
        close_button.pack(padx=5, pady=20)


def gui_start():
    root = Tk()
    root.geometry("350x150+300+300")
    output = []
    ex = UI1(root)
    root.mainloop()
    output.append(ex.input_name)
    ex = UI2(root, output[0])
    root.mainloop()
    output.append(ex.input_color)
    root.destroy()
    return output


def gui_end(game_result):
    root = Tk()
    root.geometry("350x150+300+300")
    ex = UI3(root, game_result)
    root.mainloop()



