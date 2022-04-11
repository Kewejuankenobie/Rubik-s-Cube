import tkinter
from tkinter import *
from tkinter.ttk import *


class window:
    def __init__(self):
        self.game = Tk()
        self.game.title("Rubix Cube")
        self.game.geometry("200x50")
        self.m = StringVar()
        self.savedKey = ""
        self.returnKey = False
        move = Entry(self.game, width=20, textvariable=self.m)
        move.pack()
        self.game.bind("<Return>", lambda event: self.returnMove(event, move.get()))
        self.game.update()

    def loopWindow(self):
        self.game.update()

    def returnMove(self, event, m):
        self.savedKey = m
        self.returnKey = True
        print(self.savedKey)

    def getInput(self):
        if self.returnKey:
            self.returnKey = False
            return self.savedKey

