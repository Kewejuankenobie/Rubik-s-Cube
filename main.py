#Class describing the puzzle
class puzzle:
    seed = 0
    def __init__(self, type):
        self.type = type
        self.cubeMatrix = []
        #Makes a 3x3x3 cube represented as a 3D matrix
        for i in range(type):
            xY = []
            for j in range(type):
                xZ = []
                for k in range(type):
                    xZ.append("tile")
                xY.append(xZ)
            self.cubeMatrix.append(xY)
        print(self.cubeMatrix)
        #Make cube surface and attach it to matrix

    def scramble(self, type):
        pass

    def doMove(self, move, type):
        pass

    def rotateCube(self, dir, type):
        pass

#Tile class as super with different types as a sub class
class tile:
    pass

class edge(tile):
    pass

class center(tile):
    pass

class corner(tile):
    pass



def main():
    puzzle1 = puzzle(3)

if __name__ == '__main__':
    main()
