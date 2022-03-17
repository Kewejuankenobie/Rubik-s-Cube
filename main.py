from puzzle import *
import engine
from time import sleep

def main():
    allCubes = False
    run = True
    puzzle1 = puzzle(3)
    newGame = engine.game()
    for d in enumerate(puzzle1.getState()):
        for h in enumerate(d[1]):
            for l in enumerate(h[1]):
                newGame.makeCube([d[0], h[0], l[0]])
                sleep(1)
    while run:
        newGame.allowQuit()
        #Other code to update
        #This has to be done in the gui or it won't work
        '''inputMove = input("Enter a Move in the format R, B', E, ect: ")
        if inputMove == "exit":
            run = False
        else:
            puzzle1.doMove(inputMove)'''
    print("Program Done")



if __name__ == '__main__':
    main()
