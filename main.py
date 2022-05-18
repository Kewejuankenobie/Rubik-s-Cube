from puzzle import *
from inputTK import *
import engine

#Makes new cube
def newCube(g, p):
    for d in enumerate(p):
        for h in enumerate(d[1]):
            for l in enumerate(h[1]):
                g.makeCube([d[0], h[0], l[0]], l[1])

#Displayes move on screen
def displayMove(p, m, g):
    p.doMove(m)
    newCube(g, p.getState())
    g.updateDisplay()

#Main function
def main():
    run = True
    puzzle1 = puzzle(3)

    newGame = engine.game()
    newCube(newGame, puzzle1.getState())
    newGame.updateDisplay()
    inputWindow = window()
    while run:
        inputWindow.loopWindow()
        key = inputWindow.returnInput()
        scramBool = inputWindow.canScramble
        if key != None:
            displayMove(puzzle1, key, newGame)
            key = None
        if scramBool:
            scramStr = puzzle1.scramble()
            for move in scramStr:
                displayMove(puzzle1, move, newGame)
            inputWindow.rmScramble()
        newGame.loopGame()

if __name__ == '__main__':
    main()