from tkinter import *
from tkinter.ttk import *


class window:
    #Makes a new Tkinter window with a widgets and binds the enter key to a new move
    def __init__(self):
        self.game = Tk()
        self.game.title("Rubix Cube Controller")
        self.game.geometry("300x200")
        self.m = StringVar()
        self.savedKey = ""
        self.canScramble = False
        self.isReturnKeyPressed = False
        moveLabel = Label(self.game, text="Input Moves Separated By A Space")
        moveLabel.grid(row=0, column=0)
        enterLabel = Label(self.game, text="Press The Enter Key to Confirm")
        enterLabel.grid(row=1, column=0)
        move = Entry(self.game, width=20, textvariable=self.m)
        move.grid(row=2, column=0)
        self.game.bind("<Return>", lambda event: self.updateMove(event, move.get()))
        scrambleBtn = Button(self.game, text="Click To Scramble The Cube", command=self.scrambleCommand)
        scrambleBtn.grid(row=3,column=0)
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

#Cube can scramble
    def scrambleCommand(self):
        self.canScramble = True

#Cube can't scramble
    def rmScramble(self):
        self.canScramble = False