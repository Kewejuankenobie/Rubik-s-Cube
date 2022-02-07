#Class describing the puzzle
class puzzle:
    seed = 0
    def __init__(self, type):
        self.type = type
        self.cubeMatrix = []
        #Makes a cube represented as a 3D matrix
        for i in range(type):
            xY = []
            for j in range(type):
                xZ = []
                for k in range(type):
                    xZ.append("tile")
                xY.append(xZ)
            self.cubeMatrix.append(xY)
        #Make cube surface with different tile types and attach it to the 3d cube (Like attaching stickers)
        #Do it in rings with front, center, then back. Do not include core of cube.
        #Front
        tileDict = {"corner": [], "edge": [], "center": []}
        #Front Face
        for face in enumerate(self.cubeMatrix):
            for row in enumerate(face[1]):
                for column in enumerate(row[1]):
                    if face[0] == 0:
                        print("0")
                        pass
                    if face == 1:
                        #center
                        pass
        print(self.cubeMatrix)

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

#Actual Window
class game:
    pass

def main():
    puzzle1 = puzzle(3)

if __name__ == '__main__':
    main()
