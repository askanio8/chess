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
        self.to_field(field)

    def move(self, field):
        if self.available_movements[field.x, field.y] == 1:  # если ход возможен, то делаем его
            self.board.history.append((self, (self.field.x, self.field.y), (field.x, field.y)))
            self.field.Figure = None
            self.to_field(field)
        self.board.calculateMovements()

    def to_field(self, field):
        self.field = field
        self.field.Figure = self
        if self.color == 'white':
            self.board.white_figures_list.figures_map[self.field.x, self.field.y] = 1
        else:
            self.board.black_figures_list.figures_map[self.field.x, self.field.y] = 1

    def drawself(self):
        a = self.field.create_image((self.coords_on_img[0], self.coords_on_img[1]), image=self.img)

    def check_movements(self):
        self.available_movements = self.template_movements[abs(7 - self.field.x):abs(7 - self.field.x) + 8,
                                   abs(7 - self.field.y):abs(7 - self.field.y) + 8].copy()
        if self.color == 'white':
            self.available_movements -= np.logical_and(self.available_movements,
                                                       self.board.white_figures_list.figures_map)
        else:
            self.available_movements -= np.logical_and(self.available_movements,
                                                       self.board.black_figures_list.figures_map)

    def save_king_from_check(self):
        # создаем глубокие копии списков
        # убираем эту фигуру, и добавляем такую же с координатами хода
        # считаем ходы и смотрим есть ли шах королю
        # 0 1
        pass

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

        self.template_beats = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int)
        if self.color == 'black': self.template_movements = np.flip(self.template_movements, axis=0)
        if self.color == 'black': self.template_beats = np.flip(self.template_beats, axis=0)
        self.drawself()

    def move(self, field):
        super().move(field)  # сначала нужно проверить, что туда вообще можно ходить
        if self.color == 'white':
            # убираем пешку, побитую этой на проходе
            if len(self.board.history) > 1 \
                    and self.board.canvaslists[self.field.x + 1][self.field.y].Figure == self.board.history[-2][0] \
                    and isinstance(self.board.canvaslists[self.field.x + 1, self.field.y].Figure, Pawn):
                self.board.canvaslists[field.x + 1][field.y].Figure = None
            # если ход на последнюю строку, меняем пешку на ферзя
            if self.field.x == 0:
                self.field.Figure = None
                self.board.white_figures_list.remove(self)
                self.board.white_figures_list.append(Queen(field, self.color, self.board))
                del self
        else:
            # убираем пешку, побитую этой на проходе
            if len(self.board.history) > 1 \
                    and self.board.canvaslists[self.field.x - 1][self.field.y].Figure == self.board.history[-2][0] \
                    and isinstance(self.board.canvaslists[self.field.x - 1, self.field.y].Figure, Pawn):
                self.board.canvaslists[field.x - 1][field.y].Figure = None
            # если ход на последнюю строку, меняем пешку на ферзя
            if self.field.x == 7:
                self.field.Figure = None
                self.board.black_figures_list.remove(self)
                self.board.black_figures_list.append(Queen(field, self.color, self.board))
                del self

    def check_movements(self):
        super().check_movements()
        self.available_beats = self.template_beats[abs(7 - self.field.x):abs(7 - self.field.x) + 8,
                               abs(7 - self.field.y):abs(7 - self.field.y) + 8].copy()
        if self.color == 'white':
            # если поле перед пешкой занято, ход запрещаем
            if np.logical_or(self.board.white_figures_list.figures_map,
                             self.board.black_figures_list.figures_map)[self.field.x - 1, self.field.y] == 1:
                self.available_movements[self.field.x - 1, self.field.y] = 0
            # если поле перед пешкой свободно, пешка на начальной позиции и на два поля впереди нет фигур
            # разрешаем ход на две клетки вперед
            elif self.field.x == 6 and np.logical_or(self.board.white_figures_list.figures_map,
                                                     self.board.black_figures_list.figures_map)[
                self.field.x - 2, self.field.y] == 0:
                self.available_movements[self.field.x - 2, self.field.y] = 1
            # разрешаем бить на поля по диагонали
            self.available_movements = np.maximum(self.available_movements,
                                                  np.logical_and(self.available_beats,
                                                                 self.board.black_figures_list.figures_map))
            # проверяем возможность боя на проходе
            if self.field.x == 3 and type(self.board.history[-1][0]) == type(self) and self.board.history[-1][1][0] == 1 \
                    and self.board.history[-1][2][0] == 3 and (self.field.y - self.board.history[-1][2][1]) == 1:
                self.available_movements[self.field.x - 1, self.field.y - 1] = 1
            if self.field.x == 3 and type(self.board.history[-1][0]) == type(self) and self.board.history[-1][1][0] == 1 \
                    and self.board.history[-1][2][0] == 3 and (self.field.y - self.board.history[-1][2][1]) == -1:
                self.available_movements[self.field.x - 1, self.field.y + 1] = 1
        elif self.color == 'black':
            # если поле перед пешкой занято, ход запрещаем
            if np.logical_or(self.board.white_figures_list.figures_map,
                             self.board.black_figures_list.figures_map)[self.field.x + 1, self.field.y] == 1:
                self.available_movements[self.field.x + 1, self.field.y] = 0
            # если поле перед пешкой свободно, пешка на начальной позиции и на два поля впереди нет фигур
            # разрешаем ход на две клетки вперед
            elif self.field.x == 1 and np.logical_or(self.board.white_figures_list.figures_map,
                                                     self.board.black_figures_list.figures_map)[
                self.field.x + 2, self.field.y] == 0:
                self.available_movements[self.field.x + 2, self.field.y] = 1
            # разрешаем бить на поля по диагонали
            self.available_movements = np.maximum(self.available_movements,
                                                  np.logical_and(self.available_beats,
                                                                 self.board.white_figures_list.figures_map))
            # проверяем возможность боя на проходе
            if self.field.x == 4 and type(self.board.history[-1][0]) == type(self) and self.board.history[-1][1][0] == 6 \
                    and self.board.history[-1][2][0] == 4 and (self.field.y - self.board.history[-1][2][1]) == 1:
                self.available_movements[self.field.x + 1, self.field.y - 1] = 1
            if self.field.x == 4 and type(self.board.history[-1][0]) == type(self) and self.board.history[-1][1][0] == 6 \
                    and self.board.history[-1][2][0] == 4 and (self.field.y - self.board.history[-1][2][1]) == -1:
                self.available_movements[self.field.x + 1, self.field.y + 1] = 1


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
        if not self.moved and len(self.board.history) > 0 and self.board.history[-1][0] == self:
            self.moved = True

    def check_movements(self):
        super().check_movements()
        if self.color == 'white':
            flag = True
            for i in range(self.field.x + 1, len(self.available_movements)):  # вниз
                if self.board.white_figures_list.figures_map[i, self.field.y] == 1: flag = False
                self.available_movements[i, self.field.y] = int(flag)
                if self.board.black_figures_list.figures_map[i, self.field.y] == 1: flag = False
            flag = True
            for i in range(self.field.x - 1, -1, -1):  # вверх
                if self.board.white_figures_list.figures_map[i, self.field.y] == 1: flag = False
                self.available_movements[i, self.field.y] = int(flag)
                if self.board.black_figures_list.figures_map[i, self.field.y] == 1: flag = False
            flag = True
            for i in range(self.field.y + 1, len(self.available_movements)):  # вправо
                if self.board.white_figures_list.figures_map[self.field.x, i] == 1: flag = False
                self.available_movements[self.field.x, i] = int(flag)
                if self.board.black_figures_list.figures_map[self.field.x, i] == 1: flag = False
            flag = True
            for i in range(self.field.y - 1, -1, -1):  # влево
                if self.board.white_figures_list.figures_map[self.field.x, i] == 1: flag = False
                self.available_movements[self.field.x, i] = int(flag)
                if self.board.black_figures_list.figures_map[self.field.x, i] == 1: flag = False
        if self.color == 'black':
            flag = True
            for i in range(self.field.x + 1, len(self.available_movements)):  # вниз
                if self.board.black_figures_list.figures_map[i, self.field.y] == 1: flag = False
                self.available_movements[i, self.field.y] = int(flag)
                if self.board.white_figures_list.figures_map[i, self.field.y] == 1: flag = False
            flag = True
            for i in range(self.field.x - 1, -1, -1):  # вверх
                if self.board.black_figures_list.figures_map[i, self.field.y] == 1: flag = False
                self.available_movements[i, self.field.y] = int(flag)
                if self.board.white_figures_list.figures_map[i, self.field.y] == 1: flag = False
            flag = True
            for i in range(self.field.y + 1, len(self.available_movements)):  # вправо
                if self.board.black_figures_list.figures_map[self.field.x, i] == 1: flag = False
                self.available_movements[self.field.x, i] = int(flag)
                if self.board.white_figures_list.figures_map[self.field.x, i] == 1: flag = False
            flag = True
            for i in range(self.field.y - 1, -1, -1):  # влево
                if self.board.black_figures_list.figures_map[self.field.x, i] == 1: flag = False
                self.available_movements[self.field.x, i] = int(flag)
                if self.board.white_figures_list.figures_map[self.field.x, i] == 1: flag = False


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
        if self.color == 'white':
            flag = True
            for x, y in zip(range(self.field.x + 1, 8), range(self.field.y + 1, 8)):  # вниз вправо
                if self.board.white_figures_list.figures_map[x, y] == 1: flag = False
                self.available_movements[x, y] = int(flag)
                if self.board.black_figures_list.figures_map[x, y] == 1: flag = False
            flag = True
            for x, y in zip(range(self.field.x + 1, 8), range(self.field.y - 1, -1, -1)):  # вниз влево
                if self.board.white_figures_list.figures_map[x, y] == 1: flag = False
                self.available_movements[x, y] = int(flag)
                if self.board.black_figures_list.figures_map[x, y] == 1: flag = False
            flag = True
            for x, y in zip(range(self.field.x - 1, -1, -1), range(self.field.y + 1, 8)):  # вверх вправо
                if self.board.white_figures_list.figures_map[x, y] == 1: flag = False
                self.available_movements[x, y] = int(flag)
                if self.board.black_figures_list.figures_map[x, y] == 1: flag = False
            flag = True
            for x, y in zip(range(self.field.x - 1, -1, -1), range(self.field.y - 1, -1, -1)):  # вверх влево
                if self.board.white_figures_list.figures_map[x, y] == 1: flag = False
                self.available_movements[x, y] = int(flag)
                if self.board.black_figures_list.figures_map[x, y] == 1: flag = False
        if self.color == 'black':
            flag = True
            for x, y in zip(range(self.field.x + 1, 8), range(self.field.y + 1, 8)):  # вниз вправо
                if self.board.black_figures_list.figures_map[x, y] == 1: flag = False
                self.available_movements[x, y] = int(flag)
                if self.board.white_figures_list.figures_map[x, y] == 1: flag = False
            flag = True
            for x, y in zip(range(self.field.x + 1, 8), range(self.field.y - 1, -1, -1)):  # вниз влево
                if self.board.black_figures_list.figures_map[x, y] == 1: flag = False
                self.available_movements[x, y] = int(flag)
                if self.board.white_figures_list.figures_map[x, y] == 1: flag = False
            flag = True
            for x, y in zip(range(self.field.x - 1, -1, -1), range(self.field.y + 1, 8)):  # вверх вправо
                if self.board.black_figures_list.figures_map[x, y] == 1: flag = False
                self.available_movements[x, y] = int(flag)
                if self.board.white_figures_list.figures_map[x, y] == 1: flag = False
            flag = True
            for x, y in zip(range(self.field.x - 1, -1, -1), range(self.field.y - 1, -1, -1)):  # вверх влево
                if self.board.black_figures_list.figures_map[x, y] == 1: flag = False
                self.available_movements[x, y] = int(flag)
                if self.board.white_figures_list.figures_map[x, y] == 1: flag = False


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
        if self.color == 'white':
            flag = True
            for i in range(self.field.x + 1, len(self.available_movements)):  # вниз
                if self.board.white_figures_list.figures_map[i, self.field.y] == 1: flag = False
                self.available_movements[i, self.field.y] = int(flag)
                if self.board.black_figures_list.figures_map[i, self.field.y] == 1: flag = False
            flag = True
            for i in range(self.field.x - 1, -1, -1):  # вверх
                if self.board.white_figures_list.figures_map[i, self.field.y] == 1: flag = False
                self.available_movements[i, self.field.y] = int(flag)
                if self.board.black_figures_list.figures_map[i, self.field.y] == 1: flag = False
            flag = True
            for i in range(self.field.y + 1, len(self.available_movements)):  # вправо
                if self.board.white_figures_list.figures_map[self.field.x, i] == 1: flag = False
                self.available_movements[self.field.x, i] = int(flag)
                if self.board.black_figures_list.figures_map[self.field.x, i] == 1: flag = False
            flag = True
            for i in range(self.field.y - 1, -1, -1):  # влево
                if self.board.white_figures_list.figures_map[self.field.x, i] == 1: flag = False
                self.available_movements[self.field.x, i] = int(flag)
                if self.board.black_figures_list.figures_map[self.field.x, i] == 1: flag = False
        if self.color == 'black':
            flag = True
            for i in range(self.field.x + 1, len(self.available_movements)):  # вниз
                if self.board.black_figures_list.figures_map[i, self.field.y] == 1: flag = False
                self.available_movements[i, self.field.y] = int(flag)
                if self.board.white_figures_list.figures_map[i, self.field.y] == 1: flag = False
            flag = True
            for i in range(self.field.x - 1, -1, -1):  # вверх
                if self.board.black_figures_list.figures_map[i, self.field.y] == 1: flag = False
                self.available_movements[i, self.field.y] = int(flag)
                if self.board.white_figures_list.figures_map[i, self.field.y] == 1: flag = False
            flag = True
            for i in range(self.field.y + 1, len(self.available_movements)):  # вправо
                if self.board.black_figures_list.figures_map[self.field.x, i] == 1: flag = False
                self.available_movements[self.field.x, i] = int(flag)
                if self.board.white_figures_list.figures_map[self.field.x, i] == 1: flag = False
            flag = True
            for i in range(self.field.y - 1, -1, -1):  # влево
                if self.board.black_figures_list.figures_map[self.field.x, i] == 1: flag = False
                self.available_movements[self.field.x, i] = int(flag)
                if self.board.white_figures_list.figures_map[self.field.x, i] == 1: flag = False
        if self.color == 'white':
            flag = True
            for x, y in zip(range(self.field.x + 1, 8), range(self.field.y + 1, 8)):  # вниз вправо
                if self.board.white_figures_list.figures_map[x, y] == 1: flag = False
                self.available_movements[x, y] = int(flag)
                if self.board.black_figures_list.figures_map[x, y] == 1: flag = False
            flag = True
            for x, y in zip(range(self.field.x + 1, 8), range(self.field.y - 1, -1, -1)):  # вниз влево
                if self.board.white_figures_list.figures_map[x, y] == 1: flag = False
                self.available_movements[x, y] = int(flag)
                if self.board.black_figures_list.figures_map[x, y] == 1: flag = False
            flag = True
            for x, y in zip(range(self.field.x - 1, -1, -1), range(self.field.y + 1, 8)):  # вверх вправо
                if self.board.white_figures_list.figures_map[x, y] == 1: flag = False
                self.available_movements[x, y] = int(flag)
                if self.board.black_figures_list.figures_map[x, y] == 1: flag = False
            flag = True
            for x, y in zip(range(self.field.x - 1, -1, -1), range(self.field.y - 1, -1, -1)):  # вверх влево
                if self.board.white_figures_list.figures_map[x, y] == 1: flag = False
                self.available_movements[x, y] = int(flag)
                if self.board.black_figures_list.figures_map[x, y] == 1: flag = False
        if self.color == 'black':
            flag = True
            for x, y in zip(range(self.field.x + 1, 8), range(self.field.y + 1, 8)):  # вниз вправо
                if self.board.black_figures_list.figures_map[x, y] == 1: flag = False
                self.available_movements[x, y] = int(flag)
                if self.board.white_figures_list.figures_map[x, y] == 1: flag = False
            flag = True
            for x, y in zip(range(self.field.x + 1, 8), range(self.field.y - 1, -1, -1)):  # вниз влево
                if self.board.black_figures_list.figures_map[x, y] == 1: flag = False
                self.available_movements[x, y] = int(flag)
                if self.board.white_figures_list.figures_map[x, y] == 1: flag = False
            flag = True
            for x, y in zip(range(self.field.x - 1, -1, -1), range(self.field.y + 1, 8)):  # вверх вправо
                if self.board.black_figures_list.figures_map[x, y] == 1: flag = False
                self.available_movements[x, y] = int(flag)
                if self.board.white_figures_list.figures_map[x, y] == 1: flag = False
            flag = True
            for x, y in zip(range(self.field.x - 1, -1, -1), range(self.field.y - 1, -1, -1)):  # вверх влево
                if self.board.black_figures_list.figures_map[x, y] == 1: flag = False
                self.available_movements[x, y] = int(flag)
                if self.board.white_figures_list.figures_map[x, y] == 1: flag = False


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
                                            [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=int)
        self.drawself()
        self.moved = False
        self.has_check = False

    def move(self, field):
        super().move(field)
        # рокировка
        if not self.moved and len(self.board.history) > 0 and self.board.history[-1][0] == self:
            # если сейчас этот король сделал ход
            self.moved = True
            # если он сделал ход на две клетки, двигаем и ладью тоже
            if self.field.y - self.board.history[-1][1][1] == -2:
                self.board.canvaslists[self.field.x][0].Figure.available_movements[self.field.x, self.field.y + 1] = 1
                self.board.canvaslists[self.field.x][0].Figure.move(self.board.canvaslists[self.field.x][self.field.y + 1])
                self.board.history.pop(-1)
            elif self.field.y - self.board.history[-1][1][1] == 2:
                self.board.canvaslists[self.field.x][7].Figure.available_movements[self.field.x, self.field.y - 1] = 1
                self.board.canvaslists[self.field.x][7].Figure.move(self.board.canvaslists[self.field.x][self.field.y - 1])
                self.board.history.pop(-1)

    def check_movements(self):
        super().check_movements()
        # если король на стартовой позиции, не под шахом и не двигался
        if self.color == 'white' and self.field.x == 7 and self.field.y == 4 and self.moved == False and not self.has_check:
            left_corner_canvas = self.board.canvaslists[7][0]
            # если в левом углу на той самой строке есть ладья того же цвета и она тоже не двигалась
            # и если между ними нет других фигур,
            # если король не под шахом и если поле рядом с королем со стороны ладьи не под боем
            if left_corner_canvas.Figure and type(left_corner_canvas.Figure) == Rook \
                    and left_corner_canvas.Figure.color == self.color \
                    and left_corner_canvas.Figure.moved == False \
                    and sum((self.board.black_figures_list.figures_map +
                             self.board.white_figures_list.figures_map)[self.field.x, 1:self.field.y]) == 0 \
                    and np.logical_or.reduce([x.available_movements if not isinstance(x, Pawn) else
                                              x.available_beats for x in self.board.black_figures_list])[
                self.field.x, self.field.y - 1] == 0:
                self.available_movements[self.field.x, self.field.y - 2] = 1
            # то же самое для ладьи в правом углу
            right_corner_canvas = self.board.canvaslists[7][7]
            if right_corner_canvas.Figure and type(right_corner_canvas.Figure) == Rook \
                    and right_corner_canvas.Figure.color == self.color \
                    and right_corner_canvas.Figure.moved == False \
                    and sum((self.board.black_figures_list.figures_map +
                             self.board.white_figures_list.figures_map)[self.field.x, self.field.y + 1:7]) == 0 \
                    and np.logical_or.reduce([x.available_movements if not isinstance(x, Pawn) else
                                              x.available_beats for x in self.board.black_figures_list])[
                self.field.x, self.field.y + 1] == 0:
                self.available_movements[self.field.x, self.field.y + 2] = 1
        elif self.color == 'black' and self.field.x == 0 and self.field.y == 4 and self.moved == False and not self.has_check:
            left_corner_canvas = self.board.canvaslists[0][0]
            # если в левом углу на той самой строке есть ладья того же цвета и она тоже не двигалась
            # и если между ними нет других фигур,
            # если король не под шахом и если поле рядом с королем со стороны ладьи не под боем
            if left_corner_canvas.Figure and type(left_corner_canvas.Figure) == Rook \
                    and left_corner_canvas.Figure.color == self.color \
                    and left_corner_canvas.Figure.moved == False \
                    and sum((self.board.black_figures_list.figures_map +
                             self.board.white_figures_list.figures_map)[self.field.x, 1:self.field.y]) == 0 \
                    and np.logical_or.reduce([x.available_movements if not isinstance(x, Pawn) else
                                              x.available_beats for x in self.board.white_figures_list])[
                self.field.x, self.field.y - 1] == 0:
                self.available_movements[self.field.x, self.field.y - 2] = 1
            # то же самое для ладьи в правом углу
            right_corner_canvas = self.board.canvaslists[0][7]
            if right_corner_canvas.Figure and type(right_corner_canvas.Figure) == Rook \
                    and right_corner_canvas.Figure.color == self.color \
                    and right_corner_canvas.Figure.moved == False \
                    and sum((self.board.black_figures_list.figures_map +
                             self.board.white_figures_list.figures_map)[self.field.x, self.field.y + 1:7]) == 0 \
                    and np.logical_or.reduce([x.available_movements if not isinstance(x, Pawn) else
                                              x.available_beats for x in self.board.white_figures_list])[
                self.field.x, self.field.y + 1] == 0:
                self.available_movements[self.field.x, self.field.y + 2] = 1
        # не делать ход, после которого могут сьесть короля
