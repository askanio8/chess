import tkinter
from tkinter import *
import numpy as np

import figures
from figures import *


class ChessFieldCanvas(Canvas):
    def __init__(self, master=None, x=None, y=None, figure=None, cnf={}, **kw):
        Canvas.__init__(self, master=None, cnf={}, **kw)
        self._figure = figure
        self.x = x
        self.y = y

    @property
    def Figure(self):
        return self._figure

    @Figure.setter
    def Figure(self, figure):
        if not figure:  # фигура уходит с этой клетки
            self.delete(self.find_all()[-1])
            self._figure.board.white_figures_list.figures_map[self.x, self.y] = 0
            self._figure.board.black_figures_list.figures_map[self.x, self.y] = 0
            self._figure = None
        elif not self._figure:  # эта клетка была пустая, пришла фигура
            self._figure = figure
            self._figure.field = self
            if self._figure.coords_on_img : self._figure.drawself()
        elif self._figure and figure:  # на эту клетку ставят фигуру, но на ней фигура уже есть
            if self._figure.color == 'white':
                self._figure.board.white_figures_list.figures_map[figure.field.x, figure.field.y] = 0
            else:
                self._figure.board.black_figures_list.figures_map[figure.field.x, figure.field.y] = 0
            self.delete(self.find_all()[-1])
            self._figure = figure
            self._figure.field = self
            if self._figure.coords_on_img: self._figure.drawself()


class FiguresList(list):
    def __init__(self, board):
        super(FiguresList, self).__init__()
        self.figures_map = np.zeros((8, 8), dtype=int)
        self.board = board

    def append(self, value):
        super().append(value)
        self.board.calculateMovements()
