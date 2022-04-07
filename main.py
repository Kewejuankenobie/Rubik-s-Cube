from puzzle import *
from InputTK import *
import engine
from time import sleep

def newCube(g, p):
    for d in enumerate(p):
        for h in enumerate(d[1]):
            for l in enumerate(h[1]):
                g.makeCube([d[0], h[0], l[0]], l[1])

def displayMove(p, m, g):
    p.doMove(m)
    newCube(g, p.getState())
    g.updateDisplay()

def main():
    allCubes = False
    run = True
    puzzle1 = puzzle(3)

    newGame = engine.game()
    newCube(newGame, puzzle1.getState())
    newGame.updateDisplay()
    inputWindow = window()


    #T Perm
    '''displayMove(puzzle1, "R", newGame)
    displayMove(puzzle1, "U", newGame)
    displayMove(puzzle1, "R'", newGame)
    displayMove(puzzle1, "U'", newGame)
    displayMove(puzzle1, "R'", newGame)
    displayMove(puzzle1, "F", newGame)
    displayMove(puzzle1, "R", newGame)
    displayMove(puzzle1, "R", newGame)
    displayMove(puzzle1, "U'", newGame)
    displayMove(puzzle1, "R'", newGame)
    displayMove(puzzle1, "U'", newGame)
    displayMove(puzzle1, "R", newGame)
    displayMove(puzzle1, "U", newGame)
    displayMove(puzzle1, "R'", newGame)
    displayMove(puzzle1, "F'", newGame)
    #puzzle1.doMove("Z")
    #puzzle1.doMove("F")'''


    while run:
        key = inputWindow.loopInput()
        if key != None:
            displayMove(puzzle1, key, newGame)
            key = None
        newGame.loopGame()
        #Other code to update
        #This has to be done in the gui or it won't work



if __name__ == '__main__':
    main()
