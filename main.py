from tkinter import *
import board


root = Tk()
root.title('Chess')
root.resizable(False, False)
root.geometry("640x640+200+10")

gameboard = board.Gameboard(root)

root.mainloop()