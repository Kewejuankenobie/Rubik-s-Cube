from tkinter import *
from tkinter.ttk import *
from tkinter.tix import *
from PIL import Image, ImageTk
from pathlib import Path
import os


class window:
    #Makes a new Tkinter window with a widgets and binds the enter key to a new move
    #Creates a frame for each user interface, initializes all of them, and displays the main page
    def __init__(self):
        self.game = Tk()
        self.game.title("Rubix Cube Controller")
        self.game.geometry("350x250")
        self.main = Frame(self.game)
        self.inst = Frame(self.game)
        self.movG = Frame(self.game)
        self.movG2 = Frame(self.game)
        self.movG3 = Frame(self.game)
        self.MainPage()
        self.Instructions()
        self.MoveGuide()
        self.MoveGuide2()
        self.main.pack()

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

#Handles switching the interface
    def switchInt(self, destination, current):
        current.pack_forget()
        destination.pack()

#Main Page
    def MainPage(self):
        self.m = StringVar()
        self.savedKey = ""
        self.canScramble = False
        self.isReturnKeyPressed = False
        contInst = Button(self.main, text="Controller Instructions", command=lambda: self.switchInt(self.inst, self.main))
        contInst.grid(row=0, column=0, sticky="ew")
        mvInst = Button(self.main, text="Rubiks Cube Move Guide", command=lambda: self.switchInt(self.movG, self.main))
        mvInst.grid(row=0, column=1, sticky="ew")
        spacer1 = Label(self.main, text="")
        spacer1.grid(row=1, column=0, pady=20)
        moveLabel = Label(self.main, text="Enter Moves")
        moveLabel.grid(row=2, column=1)
        move = Entry(self.main, width=20, textvariable=self.m)
        move.grid(row=3, column=1, padx=20)
        self.game.bind("<Return>", lambda event: self.updateMove(event, move.get()))
        scrambleBtn = Button(self.main, text="Scramble Puzzle", command=self.scrambleCommand)
        scrambleBtn.grid(row=3, column=0, padx=20)

#Program Instructions Page
    def Instructions(self):
        InLabel = Label(self.inst, text="How To Use The Controller", font='bold')
        InLabel.grid(row=0, column=0)
        Label(self.inst, text="Press the scramble button to scramble the cube").grid(row=1, column=0)
        Label(self.inst, text="This generates a random 25 move scramble").grid(row=2, column=0)
        Label(self.inst, text="Enter a series of moves separated by a space").grid(row=3, column=0)
        Label(self.inst, text="This can be one move (R) or many (L' F U)").grid(row=4, column=0)
        bBut1 = Button(self.inst, text="Back", command=lambda: self.switchInt(self.main, self.inst))
        bBut1.grid(row=5, column=0)

#Puzzle Move Guide Page
    def MoveGuide(self):
        mvLabel = Label(self.movG, text="Rubiks Cube Move Guide", font='bold')
        mvLabel.grid(row=0, column=0)
        Label(self.movG, text="A Rubiks cube move notation is based on layers").grid(row=1, column=0)
        Label(self.movG, text="Center pieces are in the same location").grid(row=2, column=0)
        Label(self.movG, text="All other pieces of 2-3 colors move around centers").grid(row=3, column=0)
        basePath = Path(__file__).parent
        fullSolveload = Image.open((basePath / "Resources/Base.PNG").resolve())
        fullSolveload = fullSolveload.resize((100, 100), Image.ANTIALIAS)
        fullSolve = ImageTk.PhotoImage(fullSolveload)
        solveImg = Label(self.movG, image=fullSolve)
        solveImg.image = fullSolve
        solveImg.grid(row=4, column=0)
        nBut1 = Button(self.movG, text="Next", command=lambda: self.switchInt(self.movG2, self.movG))
        nBut1.grid(row=5, column=0)

    def MoveGuide2(self):
        mvLabel = Label(self.movG2, text="Rubiks Cube Move Guide", font='bold')
        mvLabel.grid(row=0, column=0)
        Label(self.movG2, text="An R move for instance rotates the right layer").grid(row=1, column=0)

    def MoveGuide3(self):
        pass