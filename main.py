#Class describing the puzzle
class puzzle:
    seed = 0
    def __init__(self, type):
        self.type = type
        self.cubeMatrix = []
        #Makes a cube represented as a 3D matrix with peice types
        for d in range(type):
            depth = []
            for h in range(type):
                height = []
                for l in range(type):
                    if d == 0 or d == 2:
                        if (l == 0 or l == 2) and (h == 0 or h == 2):
                            height.append("corner")
                        elif l == 1 and h == 1:
                            height.append("center")
                        else:
                            height.append("edge")
                    else:
                        if (l == 0 or l == 2) and (h == 0 or h == 2):
                            height.append("edge")
                        elif l == 1 and h == 1:
                            height.append("core")
                        else:
                            height.append("center")

                depth.append(height)
            self.cubeMatrix.append(depth)

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
