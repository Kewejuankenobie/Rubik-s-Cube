from puzzle import *
import engine

def main():
    newGame = engine.game()
    newGame.makeCube()
    newGame.quit()
    puzzle1 = puzzle(3)
    run = True
    while run:
        inputMove = input("Enter a Move in the format R, B', E, ect: ")
        if inputMove == "exit":
            run = False
        else:
            puzzle1.doMove(inputMove)
    print("Program Done")



if __name__ == '__main__':
    main()
