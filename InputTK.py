import tkinter
from tkinter import *
from tkinter.ttk import *


class window:
    def __init__(self):
        self.game = Tk()
        self.game.title("Rubix Cube")
        self.game.geometry("200x50")
        self.m = tkinter.StringVar(value="")
        move = Entry(self.game, width=20, textvariable=self.m)
        move.pack()

    def loopInput(self):
        self.game.bind("<Return>",lambda event, moveDone=self.m.get(): self.returnMove(event, moveDone))
        self.game.update()

    def returnMove(self, event, m):
        print(m)
