import tkinter
from tkinter import *
import numpy as np

import figures
from figures import *


class ChessFieldCanvas(Canvas):
    def __init__(self, master=None, figure=None, cnf={}, **kw):
        Canvas.__init__(self, master=None, cnf={}, **kw)
        self._figure = figure

    @property
    def Figure(self):
        return self._figure

    @Figure.setter
    def Figure(self, figure):
        if figure is None:  # фигура уходит с этой клетки
            self.delete(self.find_all()[-1])
            self._figure = None
        elif self._figure is None:  # эта клетка была пустая, пришла фигура
            self._figure = figure
            self._figure.field = self
            if self._figure.coords_on_img : self._figure.drawself()
        elif self._figure and figure:  # на эту клетку ставят фигуру, но на ней фигура уже есть
            del self._figure
            self._figure = figure
            self._figure.field = self
            self.delete(self.find_all()[-1])
            if self._figure.coords_on_img: self._figure.drawself()
        # иначе, если на клетке не было фигуры и приходит None, то ничего не делаем


class FiguresList(list):
    def __init__(self):
        super(FiguresList, self).__init__()
        self.figures_map = np.zeros((8, 8), dtype=int)
