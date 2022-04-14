from tkinter import *
from tkinter.ttk import *


class window:
    #Makes a new Tkinter window and binds the enter key to a new move
    def __init__(self):
        self.game = Tk()
        self.game.title("Rubix Cube")
        self.game.geometry("300x50")
        self.m = StringVar()
        self.savedKey = ""
        self.isReturnKeyPressed = False
        move = Entry(self.game, width=20, textvariable=self.m)
        move.pack()
        self.game.bind("<Return>", lambda event: self.updateMove(event, move.get()))
        self.game.update()

#Updates Tkinter Window
    def loopWindow(self):
        self.game.update()

#Saves move to class variables and says that the move has been done
    def updateMove(self, event, m):
        self.savedKey = m
        self.isReturnKeyPressed = True

#If an input is recived, this returns it and sets the move Status to false
    def returnInput(self)-> str:
        if self.isReturnKeyPressed:
            self.isReturnKeyPressed = False
            return self.savedKey