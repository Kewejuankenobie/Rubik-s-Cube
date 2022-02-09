# Class describing the puzzle
class puzzle:
    seed = 0

    def __init__(self, type):
        self.type = type
        self.cubeMatrix = []
        # Makes a cube represented as a 3D matrix with peice types
        for d in range(type):
            depth = []
            for h in range(type):
                height = []
                for l in range(type):
                    if d == 0 or d == type - 1:
                        if (l == 0 or l == type - 1) and (h == 0 or h == type - 1):
                            height.append("corner")
                        elif l == 1 and h == 1:
                            height.append("center")
                        else:
                            height.append("edge")
                    else:
                        if (l == 0 or l == type - 1) and (h == 0 or h == type - 1):
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


# Tile class as super with different types as a sub class
class tile:
    colors = {"side1": "", "side2": "" , "side3" : ""}
    rotationVector = (0, 0, 0)
    def __init__(self, depth, height, length):
        self.depth = depth
        self.height = height
        self.length = length


class edge(tile):
    def __init__(self, depth, height, length):
        super().__init__(depth, height, length)
        if self.depth == 0:
            self.colors["side1"] = "green"
        elif self.depth == 2:
            self.colors["side1"] = "blue"
        else:
            pass
        print(self.colors)



class center(tile):
    pass


class corner(tile):
    pass


# Actual Window
class game:
    pass


def main():
    puzzle1 = puzzle(3)
    e = edge(0, 0, 1)


if __name__ == '__main__':
    main()
