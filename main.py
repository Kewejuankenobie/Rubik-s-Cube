# Class describing the puzzle
import math

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
                            print(d, h, l)
                            height.append(edge(d, h, l))
                    else:
                        if (l == 0 or l == type - 1) and (h == 0 or h == type - 1):
                            height.append(edge(d, h, l))
                        elif l == 1 and h == 1:
                            height.append("core")
                        else:
                            height.append("center")

                depth.append(height)
            self.cubeMatrix.append(depth)

        print(self.cubeMatrix[0][0][1])

    def scramble(self, type):
        pass

    def doMove(self, move, type):
        pass

    def rotateCube(self, dir, type):
        pass


# Tile class as super with different types as a sub class
class tile:
    colors = {"side1": "", "side2": "" , "side3" : ""}
    rotationVector = [0.0, 0.0, 0.0] # In Radians with the default being front right bottom facing
    def __init__(self, depth, height, length):
        self.depth = depth
        self.height = height
        self.length = length


class edge(tile):
    def __init__(self, depth, height, length):
        super().__init__(depth, height, length)
        #For side 1
        if self.depth == 0:
            self.colors["side1"] = "green"
            self.rotationVector[0] = 0.0
        elif self.depth == 2:
            self.colors["side1"] = "blue"
            self.rotationVector[0] = math.pi
        else:
            if self.height == 0 or self.height == 2:
                if self.length == 0:
                    self.colors["side1"] = "orange"
                    self.rotationVector[0] = (3 * math.pi) / 2
                elif self.length == 2:
                    self.colors["side1"] = "red"
                    self.rotationVector[0] = math.pi / 2

        #Side 2
        #if self.depth == 0 or self.depth == 2:
        if self.height == 0:
            self.colors["side2"] = "white"
            self.rotationVector[1] = 0.0
        elif self.height == 2:
            self.colors["side2"] = "yellow"
            self.rotationVector[1] = math.pi
        else:
            if self.length == 0:
                self.colors["side2"] = "orange"
                self.rotationVector[1] = math.pi / 2
            elif self.length == 2:
                self.colors["side2"] = "red"
                self.rotationVector[1] = (3 * math.pi) / 2

    def __repr__(self):
        return f"Color {self.colors}, Rotation: {self.rotationVector}"



class center(tile):
    pass


class corner(tile):
    pass


# Actual Window
class game:
    pass


def main():
    puzzle1 = puzzle(3)
    e = edge(0, 1, 2)
    print(e)
    print(edge(1, 2, 0))


if __name__ == '__main__':
    main()
