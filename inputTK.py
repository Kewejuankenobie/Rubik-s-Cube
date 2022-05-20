from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from pathlib import Path

#New Tkinter Window
class window:
    #Creates a frame for each user interface, initializes all of them, and displays the main page
    def __init__(self):
        self.game = Tk()
        self.game.title("Rubix Cube Controller")
        self.game.geometry("350x350")
        self.basePath = Path(__file__).parent
        self.main = Frame(self.game)
        self.inst = Frame(self.game)
        self.movG = Frame(self.game)
        self.movG2 = Frame(self.game)
        self.movG3 = Frame(self.game)
        self.movG4 = Frame(self.game)
        self.MainPage()
        self.Instructions()
        self.MoveGuide()
        self.MoveGuide2()
        self.MoveGuide3()
        self.MoveGuide4()
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

#Handles switching the interface by unrendering the current frame and rendering a new one
    def switchInt(self, destination, current):
        current.pack_forget()
        destination.pack()

#Main Page where most action happens
    def MainPage(self):
        self.m = StringVar()
        self.savedKey = ""
        self.canScramble = False
        self.isReturnKeyPressed = False
        #Top Buttons
        contInst = Button(self.main, text="Controller Instructions", command=lambda: self.switchInt(self.inst, self.main))
        contInst.grid(row=0, column=0, sticky="ew")
        mvInst = Button(self.main, text="Rubiks Cube Move Guide", command=lambda: self.switchInt(self.movG, self.main))
        mvInst.grid(row=0, column=1, sticky="ew")
        spacer1 = Label(self.main, text="")
        spacer1.grid(row=1, column=0, pady=20)
        #Move Entry
        moveLabel = Label(self.main, text="Enter Moves")
        moveLabel.grid(row=2, column=1)
        move = Entry(self.main, width=20, textvariable=self.m)
        move.grid(row=3, column=1, padx=20)
        #Bind Enter key to doing a move
        self.game.bind("<Return>", lambda event: self.updateMove(event, move.get()))
        # Scramble Button
        scrambleBtn = Button(self.main, text="Scramble Puzzle", command=self.scrambleCommand)
        scrambleBtn.grid(row=3, column=0, padx=20)
        #Small Move Reference
        Label(self.main, text="Move Reference").grid(row=4, column=0, pady=20)
        Label(self.main, text="").grid(row=4, column=1)
        Label(self.main, text="Rotation Around X:").grid(row=5, column=0)
        Label(self.main, text="R R\' L L\' M M\'").grid(row=5, column=1)
        Label(self.main, text="Rotation Around Y:").grid(row=6, column=0)
        Label(self.main, text="U U\' D D\' E E\'").grid(row=6, column=1)
        Label(self.main, text="Rotation Around Z:").grid(row=7, column=0)
        Label(self.main, text="F F\' B B\' S S\'").grid(row=7, column=1)
        Label(self.main, text="Cube Rotations:").grid(row=8, column=0)
        Label(self.main, text="X X\' Y Y\' Z Z\'").grid(row=8, column=1)
        Cload = Image.open((self.basePath / "Resources/Coord.PNG").resolve())
        Cload = Cload.resize((70, 70), Image.ANTIALIAS)
        CFin = ImageTk.PhotoImage(Cload)
        CImg = Label(self.main, image=CFin)
        CImg.image = CFin
        CImg.grid(row=9, column=1)

#Controller Instructions Page
    def Instructions(self):
        InLabel = Label(self.inst, text="How To Use The Controller", font='bold')
        InLabel.grid(row=0, column=0)
        Label(self.inst, text="Press the scramble button to scramble the cube").grid(row=1, column=0)
        Label(self.inst, text="This generates a random 25 move scramble").grid(row=2, column=0)
        Label(self.inst, text="Enter a series of moves separated by a space").grid(row=3, column=0)
        Label(self.inst, text="This can be one move (R) or many (L' F U)").grid(row=4, column=0)
        bBut1 = Button(self.inst, text="Return To Controller", command=lambda: self.switchInt(self.main, self.inst))
        bBut1.grid(row=5, column=0)

#Puzzle Move Guide Page 1
    def MoveGuide(self):
        mvLabel = Label(self.movG, text="Rubiks Cube Move Guide", font='bold')
        mvLabel.grid(row=0, column=0)
        #Explination on Moves
        Label(self.movG, text="A Rubiks cube move notation is based on layers").grid(row=1, column=0)
        Label(self.movG, text="Center pieces are in the same location").grid(row=2, column=0)
        Label(self.movG, text="All other pieces of 2-3 colors move around centers").grid(row=3, column=0)
        #Loads an image in the Resources folder
        fullSolveload = Image.open((self.basePath / "Resources/Base.PNG").resolve())
        fullSolveload = fullSolveload.resize((100, 100), Image.ANTIALIAS)
        fullSolve = ImageTk.PhotoImage(fullSolveload)
        solveImg = Label(self.movG, image=fullSolve)
        solveImg.image = fullSolve
        solveImg.grid(row=4, column=0)
        #Next Button
        nBut1 = Button(self.movG, text="Next", command=lambda: self.switchInt(self.movG2, self.movG))
        nBut1.grid(row=5, column=0)

#Move Guide Page 2 about an example move
    def MoveGuide2(self):
        mvLabel = Label(self.movG2, text="Rubiks Cube Move Guide", font='bold')
        mvLabel.grid(row=0, column=0)
        Label(self.movG2, text="An R move for instance rotates the right layer 90 degrees").grid(row=1, column=0)
        Rload = Image.open((self.basePath / "Resources/RMove.PNG").resolve())
        Rload = Rload.resize((100, 100), Image.ANTIALIAS)
        RImg = ImageTk.PhotoImage(Rload)
        RLab = Label(self.movG2, image=RImg)
        RLab.image = RImg
        RLab.grid(row=2, column=0)
        Label(self.movG2, text="VS the original position").grid(row=3, column=0)
        fullSolveload = Image.open((self.basePath / "Resources/Base.PNG").resolve())
        fullSolveload = fullSolveload.resize((100, 100), Image.ANTIALIAS)
        fullSolve = ImageTk.PhotoImage(fullSolveload)
        solveImg = Label(self.movG2, image=fullSolve)
        solveImg.image = fullSolve
        solveImg.grid(row=4, column=0)
        nBut2 = Button(self.movG2, text="Next", command=lambda: self.switchInt(self.movG3, self.movG2))
        nBut2.grid(row=5, column=0)

#Move Guide Page 3 about opposite direction moves
    def MoveGuide3(self):
        mvLabel = Label(self.movG3, text="Rubiks Cube Move Guide", font='bold')
        mvLabel.grid(row=0, column=0)
        Label(self.movG3, text="Adding an apostrophe to R reverses the direction, hence R\'").grid(row=1, column=0)
        RiLoad = Image.open((self.basePath / "Resources/RiMove.PNG").resolve())
        RiLoad = RiLoad.resize((100, 100), Image.ANTIALIAS)
        RiImg = ImageTk.PhotoImage(RiLoad)
        RiLab = Label(self.movG3, image=RiImg)
        RiLab.image = RiImg
        RiLab.grid(row=2, column=0)
        Label(self.movG3, text="VS the original position").grid(row=3, column=0)
        fullSolveload = Image.open((self.basePath / "Resources/Base.PNG").resolve())
        fullSolveload = fullSolveload.resize((100, 100), Image.ANTIALIAS)
        fullSolve = ImageTk.PhotoImage(fullSolveload)
        solveImg = Label(self.movG3, image=fullSolve)
        solveImg.image = fullSolve
        solveImg.grid(row=4, column=0)
        nBut3 = Button(self.movG3, text="Next", command=lambda: self.switchInt(self.movG4, self.movG3))
        nBut3.grid(row=5, column=0)

#Move Guide Page 4 gives a more detailed move guide on what each move moves
    def MoveGuide4(self):
        mvLabel = Label(self.movG4, text="Rubiks Cube Move Guide", font='bold')
        mvLabel.grid(row=0, column=0)
        Label(self.movG4, text="Notation is identical to the official cubing notation").grid(row=1, column=0)
        Label(self.movG4, text="X axis moves:").grid(row=2, column=0)
        Label(self.movG4, text="R: Right layer, L: Left layer, M: Layer between R and L").grid(row=3, column=0)
        Label(self.movG4, text="Y axis moves:").grid(row=4, column=0)
        Label(self.movG4, text="U: Top layer, D: Bottom layer, E: Layer between U and D").grid(row=5, column=0)
        Label(self.movG4, text="Z axis moves:").grid(row=6, column=0)
        Label(self.movG4, text="F: Front layer, B: Back layer, S: Layer between F and B").grid(row=7, column=0)
        Label(self.movG4, text="Cube rotations:").grid(row=8, column=0)
        Label(self.movG4, text="X: X axis rotation, Y: Y axis rotation, Z: Z axis rotation").grid(row=9, column=0)
        Cload = Image.open((self.basePath / "Resources/Coord.PNG").resolve())
        Cload = Cload.resize((100, 100), Image.ANTIALIAS)
        CFin = ImageTk.PhotoImage(Cload)
        CImg = Label(self.movG4, image=CFin)
        CImg.image = CFin
        CImg.grid(row=10, column=0)
        nBut4 = Button(self.movG4, text="Return to Controller", command=lambda: self.switchInt(self.main, self.movG4))
        nBut4.grid(row=11, column=0)