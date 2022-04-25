from tkinter import *
from tkinter.ttk import *


class window:
    #Makes a new Tkinter window and binds the enter key to a new move
    def __init__(self):
        self.game = Tk()
        self.game.title("Rubix Cube")
        self.game.geometry("300x75")
        self.m = StringVar()
        self.savedKey = ""
        self.canScramble = False
        self.isReturnKeyPressed = False
        moveLabel = Label(self.game, text="Enter A Move: ")
        moveLabel.grid(row=0, column=0)
        move = Entry(self.game, width=20, textvariable=self.m)
        move.grid(row=0, column=1)
        self.game.bind("<Return>", lambda event: self.updateMove(event, move.get()))
        scrambleBtn = Button(self.game, text="Scramble", command=self.scrambleCommand)
        scrambleBtn.grid(row=1,column=1)
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

    def scrambleCommand(self):
        self.canScramble = True

    def rmScramble(self):
        self.canScramble = False