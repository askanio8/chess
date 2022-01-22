from tkinter import *
import numpy as np


class Figure:
    file = 'Chess_Pieces.png'

    def __init__(self, field, color, board):
        self.color = color
        self.board = board
        self.img = PhotoImage(file=self.file)
        self.available_movements = np.ones((8, 8), dtype=int)
        self.template_movements = np.zeros((15, 15), dtype=int)
        self.coords_on_img = None
        self.field = None
        self.x = None
        self.y = None
        self.move(field)

    def move(self, field):
        num_canvas = 0 if len(str(field)[18:]) == 0 else int(str(field)[18:]) - 1
        if self.available_movements[num_canvas // 8, num_canvas % 8] == 1:  # если ход возможен, то делаем его
            self.__register_in_figure_list__(num_canvas)
            self.board.history.append((self, (self.x, self.y), (num_canvas // 8, num_canvas % 8)))
            self.x = num_canvas // 8
            self.y = num_canvas % 8
            if self.field: self.field.Figure = None  # здесь проблема гдето
            self.field = field
            field.Figure = self
            self.board.calculateMovements()  # пересчитываем возможные ходы для всех фигур

    def __register_in_figure_list__(self, num_canvas):
        if self.color == 'white':
            self.board.white_figures_list.figures_map[num_canvas // 8, num_canvas % 8] = 1
            if self.field: self.board.white_figures_list.figures_map[self.x, self.y] = 0
        else:
            self.board.black_figures_list.figures_map[num_canvas // 8, num_canvas % 8] = 1
            if self.field: self.board.black_figures_list.figures_map[self.x, self.y] = 0

    def drawself(self):
        a = self.field.create_image((self.coords_on_img[0], self.coords_on_img[1]), image=self.img)

    def check_movements(self):
        self.available_movements = self.template_movements[abs(7 - self.x):abs(7 - self.x) + 8,
                                   abs(7 - self.y):abs(7 - self.y) + 8].copy()
        if self.color == 'white':
            self.available_movements -= np.logical_and(self.available_movements,
                                                       self.board.white_figures_list.figures_map)
        else:
            self.available_movements -= np.logical_and(self.available_movements,
                                                       self.board.black_figures_list.figures_map)



class Pawn(Figure):
    def __init__(self, field, color, board):
        super().__init__(field, color, board)
        if self.color == 'white':
            self.coords_on_img = (-160, 80)
        else:
            self.coords_on_img = (-160, 0)
        self.template_movements = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int)
        if self.color == 'black': self.template_movements = np.flip(self.template_movements, axis=0)
        self.drawself()

    def move(self, field):
        num_canvas = 0 if len(str(field)[18:]) == 0 else int(str(field)[18:]) - 1
        if self.y and num_canvas % 8 != self.y and field.Figure == None:
            if self.color == 'white':
                self.board.canvaslists[num_canvas//8 + 1][num_canvas%8].Figure = None
            else:
                self.board.canvaslists[num_canvas//8 - 1][num_canvas%8].Figure = None
        super().move(field)

    def check_movements(self):
        super().check_movements()
        if self.color == 'white':
            # если поле перед пешкой занято, ход запрещаем
            if np.logical_or(self.board.white_figures_list.figures_map,
                            self.board.black_figures_list.figures_map)[self.x - 1, self.y] == 1:
                self.available_movements[self.x - 1, self.y] = 0
            # если поле перед пешкой свободно, пешка на начальной позиции и а два поля впереди нет фигур
            # разрешаем ход на две клетки вперед
            elif self.x == 6 and np.logical_or(self.board.white_figures_list.figures_map,
                            self.board.black_figures_list.figures_map)[self.x - 2, self.y] == 0:
                self.available_movements[self.x - 2, self.y] = 1
            # разрешаем бить на поля по диагонали
            if self.y < 7 and self.board.black_figures_list.figures_map[self.x - 1, self.y + 1] == 1:
                self.available_movements[self.x - 1, self.y + 1] = 1
            if self.y >= 0 and self.board.black_figures_list.figures_map[self.x - 1, self.y - 1] == 1:
                self.available_movements[self.x - 1, self.y - 1] = 1
            # проверяем возможность боя на проходе
            if self.x == 3 and type(self.board.history[-1][0]) == type(self) and self.board.history[-1][1][0] == 1 \
                    and self.board.history[-1][2][0] == 3 and (self.y - self.board.history[-1][2][1]) == 1:
                self.available_movements[self.x - 1, self.y - 1] = 1
            if self.x == 3 and type(self.board.history[-1][0]) == type(self) and self.board.history[-1][1][0] == 1 \
                    and self.board.history[-1][2][0] == 3 and (self.y - self.board.history[-1][2][1]) == -1:
                self.available_movements[self.x - 1, self.y + 1] = 1
        elif self.color == 'black':
            # если поле перед пешкой занято, ход запрещаем
            if np.logical_or(self.board.white_figures_list.figures_map,
                            self.board.black_figures_list.figures_map)[self.x + 1, self.y] == 1:
                self.available_movements[self.x + 1, self.y] = 0
            # если поле перед пешкой свободно, пешка на начальной позиции и а два поля впереди нет фигур
            # разрешаем ход на две клетки вперед
            elif self.x == 1 and np.logical_or(self.board.white_figures_list.figures_map,
                            self.board.black_figures_list.figures_map)[self.x + 2, self.y] == 0:
                self.available_movements[self.x + 2, self.y] = 1
            # разрешаем бить на поля по диагонали
            if self.y < 7 and self.board.white_figures_list.figures_map[self.x + 1, self.y + 1] == 1:
                self.available_movements[self.x + 1, self.y + 1] = 1
            if self.y >= 0 and self.board.white_figures_list.figures_map[self.x + 1, self.y - 1] == 1:
                self.available_movements[self.x + 1, self.y - 1] = 1
            # проверяем возможность боя на проходе
            if self.x == 4 and type(self.board.history[-1][0]) == type(self) and self.board.history[-1][1][0] == 6 \
                    and self.board.history[-1][2][0] == 4 and (self.y - self.board.history[-1][2][1]) == 1:
                self.available_movements[self.x + 1, self.y - 1] = 1
            if self.x == 4 and type(self.board.history[-1][0]) == type(self) and self.board.history[-1][1][0] == 6 \
                    and self.board.history[-1][2][0] == 4 and (self.y - self.board.history[-1][2][1]) == -1:
                self.available_movements[self.x + 1, self.y + 1] = 1


class Rook(Figure):
    def __init__(self, field, color, board):
        super().__init__(field, color, board)
        if self.color == 'white':
            self.coords_on_img = (-80, 80)
        else:
            self.coords_on_img = (-80, 0)
        self.template_movements = np.array([[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                                            [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
                                            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]], dtype=int)
        self.drawself()
        self.moved = False

    def move(self, field):
        super().move(field)
        self.moved = True

    def check_movements(self):
        super().check_movements()


class Knight(Figure):
    def __init__(self, field, color, board):
        super().__init__(field, color, board)
        if self.color == 'white':
            self.coords_on_img = (0, 80)
        else:
            self.coords_on_img = (0, 0)
        self.template_movements = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int)
        self.drawself()

    def check_movements(self):
        super().check_movements()


class Bishop(Figure):
    def __init__(self, field, color, board):
        super().__init__(field, color, board)
        if self.color == 'white':
            self.coords_on_img = (80, 80)
        else:
            self.coords_on_img = (80, 0)
        self.template_movements = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                                            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                                            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                                            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                                            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                                            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]], dtype=int)
        self.drawself()

    def check_movements(self):
        super().check_movements()


class Queen(Figure):
    def __init__(self, field, color, board):
        super().__init__(field, color, board)
        if self.color == 'white':
            self.coords_on_img = (160, 80)
        else:
            self.coords_on_img = (160, 0)
        self.template_movements = np.array([[1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                                            [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                                            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                                            [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                                            [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                                            [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
                                            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                                            [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                                            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                                            [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                                            [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1]], dtype=int)
        self.drawself()

    def check_movements(self):
        super().check_movements()


class King(Figure):
    def __init__(self, field, color, board):
        super().__init__(field, color, board)
        if self.color == 'white':
            self.coords_on_img = (240, 80)
        else:
            self.coords_on_img = (240, 0)
        self.template_movements = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int)
        self.drawself()
        self.moved = False

    def move(self, field):
        super().move(field)
        self.moved = True

    def check_movements(self):
        super().check_movements()
