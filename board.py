import tkinter
from tkinter import *
import numpy as np
from chessfieldcanvas import ChessFieldCanvas, FiguresList

import figures
from figures import *


class Gameboard:
    def __init__(self, window):
        self.window = window  # окно tkinter
        self.canvaslists = []  # списки клеток по рядам
        self.history = []
        self.drawboard()  # рисуем доску
        self.white_figures_list = FiguresList(self)
        self.black_figures_list = FiguresList(self)
        self.figures_on_start_positions()  # рисуем фигуры
        self.save_canvas_bgcolor_dict = {}  # словарь хранения клеток и их цветов
        self.clickedFigure = None  # флаг клика

    def drawboard(self):  # рисуем доску
        for r in range(8):
            rowlist = []
            for c in range(8):
                canvas = ChessFieldCanvas(self.window, width=80, x=r, y=c, height=80, background='#eeeed2',
                                          bd=0, highlightthickness=0)
                if (r + c) % 2 == 0:
                    canvas.configure(bg='lightgray')
                    if c == 0:
                        canvas.create_text(10, 15, fill='#568737', font=("Helvetica", 14), text=str(8 - r))
                    if r == 7:
                        canvas.create_text(73, 70, fill='#568737', font=("Helvetica", 14), text=chr(97 + c))
                else:
                    canvas.configure(bg='#568737')
                    if c == 0:
                        canvas.create_text(10, 15, fill='lightgray', font=("Helvetica", 14), text=str(8 - r))
                    if r == 7:
                        canvas.create_text(73, 70, fill='lightgray', font=("Helvetica", 14), text=chr(97 + c))
                canvas.grid(row=r, column=c, padx=0, pady=0)
                canvas.bind('<ButtonPress-1>', self.click_on_figure)
                rowlist.append(canvas)
            self.canvaslists.append(rowlist)

    def figures_on_start_positions(self):  # рисуем фигуры
        self.black_figures_list.append(Rook(self.canvaslists[0][0], 'black', self))
        self.black_figures_list.append(Knight(self.canvaslists[0][1], 'black', self))
        self.black_figures_list.append(Bishop(self.canvaslists[0][2], 'black', self))
        self.black_figures_list.append(Queen(self.canvaslists[0][3], 'black', self))
        self.black_figures_list.append(King(self.canvaslists[0][4], 'black', self))
        self.black_figures_list.append(Bishop(self.canvaslists[0][5], 'black', self))
        self.black_figures_list.append(Knight(self.canvaslists[0][6], 'black', self))
        self.black_figures_list.append(Rook(self.canvaslists[0][7], 'black', self))
        for coord in range(8): self.black_figures_list.append(Pawn(self.canvaslists[1][coord], 'black', self))
        for coord in range(8): self.white_figures_list.append(Pawn(self.canvaslists[6][coord], 'white', self))
        self.white_figures_list.append(Rook(self.canvaslists[7][0], 'white', self))
        self.white_figures_list.append(Knight(self.canvaslists[7][1], 'white', self))
        self.white_figures_list.append(Bishop(self.canvaslists[7][2], 'white', self))
        self.white_figures_list.append(Queen(self.canvaslists[7][3], 'white', self))
        self.white_figures_list.append(King(self.canvaslists[7][4], 'white', self))
        self.white_figures_list.append(Bishop(self.canvaslists[7][5], 'white', self))
        self.white_figures_list.append(Knight(self.canvaslists[7][6], 'white', self))
        self.white_figures_list.append(Rook(self.canvaslists[7][7], 'white', self))

    def click_on_figure(self, event):  # событие клика
        self.back_canvases_colors()  # возвращаем цвета назад
        if self.clickedFigure:  # если на предыдущем клике была выбрана фигура
            self.clickedFigure.move(event.widget)  # пытаемся её двинуть на выбранную клетку
            self.clickedFigure = None
        else:  # если предыдущий клик был по пустой клетке, или была попытка сделать ход
            self.change_canvas_color(event.widget, ('darkgray', 'darkolivegreen'))  # просто выделяем клетку
            if event.widget.Figure:  # если на клетке есть фигура, показываем возможные ходы
                self.clickedFigure = event.widget.Figure  # сохраняем фигуру для след клика
                res = np.where(self.clickedFigure.available_movements == 1)
                for r in zip(res[0], res[1]):  # рисуем возможные ходы выбранной фигуры
                    self.change_canvas_color(self.canvaslists[r[0]][r[1]], ('lightpink', 'palevioletred'))

    def back_canvases_colors(self):
        for canvas in self.save_canvas_bgcolor_dict:
            canvas.configure(bg=self.save_canvas_bgcolor_dict[canvas])
        self.save_canvas_bgcolor_dict = {}

    def change_canvas_color(self, canvas, colors):
        '''
        меняем цвет клетки
        :param canvas: ChessFieldCanvas
        :param colors: tuple two params (firstcolor, secondcolor)
        :return:
        '''
        self.save_canvas_bgcolor_dict[canvas] = canvas['background']  # сохраняем цвет текущей клетки
        if canvas['background'] == 'lightgray':  # задаем для неё новый цвет
            canvas.configure(bg=colors[0])
        else:
            canvas.configure(bg=colors[1])

    def calculateMovements(self):
        '''
        считаем возможные ходы для фигур и проверяем есть ли шах королям
        '''
        white_map_beats = np.zeros((8, 8))
        black_map_beats = np.zeros((8, 8))
        white_king = None
        black_king = None
        # считаем ходы всех фигур
        for figure in self.white_figures_list:
            if not isinstance(figure, King):
                figure.check_movements()
                if not isinstance(figure, Pawn):
                    white_map_beats = np.logical_or(white_map_beats, figure.available_movements)
                else:
                    white_map_beats = np.logical_or(white_map_beats, figure.available_beats)
            else:
                white_king = figure

        # считаем ходы всех фигур
        for figure in self.black_figures_list:
            if not isinstance(figure, King):
                figure.check_movements()
                if not isinstance(figure, Pawn):
                    black_map_beats = np.logical_or(black_map_beats, figure.available_movements)
                else:
                    black_map_beats = np.logical_or(black_map_beats, figure.available_beats)
            else:
                black_king = figure

        # шах королю
        if white_king:
            white_king.has_check = bool(black_map_beats[white_king.field.x, white_king.field.y])
            white_king.check_movements()

        # шах королю
        if black_king:
            black_king.has_check = bool(white_map_beats[black_king.field.x, black_king.field.y])
            black_king.check_movements()

        # оставляем только ходы, спасающие короля от шаха
        if white_king and white_king.has_check:
            for figure in self.white_figures_list:
                figure.save_king_from_check()

        if white_king and white_king.has_check:
            for figure in self.white_figures_list:
                figure.save_king_from_check()