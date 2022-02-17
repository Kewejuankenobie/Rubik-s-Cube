# Class describing the puzzle
import math

# Tile class as super with different types as a sub class
class tile:
    # In Radians with the default being front right bottom facing
    def __init__(self, depth, height, length):
        self.depth = depth
        self.height = height
        self.length = length
        self.colors = {"side1": "", "side2": "", "side3": ""}
        self.rotation = [0.0, 0.0, 0.0]

#Rotation, 0 axis is up and down, 1 axis is front and back, 2 axis is left and right

class edge(tile):
    def __init__(self, depth, height, length):
        super().__init__(depth, height, length)
        #For side 1
        if self.depth == 0:
            self.colors["side1"] = "green"
            self.rotation[0] = 0.0
        elif self.depth == 2:
            self.colors["side1"] = "blue"
            self.rotation[0] = math.pi
        else:
            if self.height == 0 or self.height == 2:
                if self.length == 0:
                    self.colors["side1"] = "orange"
                    self.rotation[0] = (3 * math.pi) / 2
                elif self.length == 2:
                    self.colors["side1"] = "red"
                    self.rotation[0] = math.pi / 2
        #Side 2
        #if self.depth == 0 or self.depth == 2:
        if self.height == 0:
            self.colors["side2"] = "white"
            self.rotation[1] = 0
        elif self.height == 2:
            self.colors["side2"] = "yellow"
            self.rotation[1] = math.pi
        else:
            if self.length == 0:
                self.colors["side2"] = "orange"
                self.rotation[1] = math.pi / 2
            elif self.length == 2:
                self.colors["side2"] = "red"
                self.rotation[1] = (3 * math.pi) / 2
    def __repr__(self):
        return f"Color {self.colors}, Rotation: {self.rotation}"



class center(tile):
    def __init__(self, depth, height, length):
        super().__init__(depth, height, length)
        if self.depth == 0:
            self.colors["side1"] = "green"
            self.rotation[0] = 0.0
        elif self.depth == 2:
            self.colors["side1"] = "blue"
            self.rotation[0] = math.pi
        else:
            if self.height == 0:
                self.colors["side1"] = "white"
                self.rotation[2] = math.pi / 2
            elif self.height == 2:
                self.colors["side1"] = "yellow"
                self.rotation[2] = (3 * math.pi) / 2
            else:
                if self.length == 0:
                    self.colors["side1"] = "orange"
                    self.rotation[0] = (3 * math.pi) / 2
                elif self.length == 2:
                    self.colors["side1"] = "red"
                    self.rotation[0] = math.pi / 2
    def __repr__(self):
        return f"Color {self.colors}, Rotation: {self.rotation}"


class corner(tile):
    def __init__(self, depth, height, length):
        super().__init__(depth, height, length)
        #Side 1
        if self.depth == 0:
            self.colors["side1"] = "green"
            self.rotation[0] = 0.0
        elif self.depth == 2:
            self.colors["side1"] = "blue"
            self.rotation[0] = math.pi
        #Side 2
        if self.height == 0:
            self.colors["side2"] = "white"
            self.rotation[1] = 0.0
        elif self.height == 2:
            self.colors["side2"] = "yellow"
            self.rotation[1] = math.pi
        #Side 3
        if self.length == 0:
            self.colors["side3"] = "orange"
            self.rotation[2] = math.pi
        elif self.length == 2:
            self.colors["side3"] = "red"
            self.rotation[2] = 0.0
    def __repr__(self):
        return f"Color {self.colors}, Rotation: {self.rotation}"


#Actual puzzle
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
                            height.append(corner(d, h, l))
                        elif l == 1 and h == 1:
                            height.append(center(d, h, l))
                        else:
                            height.append(edge(d, h, l))
                    else:
                        if (l == 0 or l == type - 1) and (h == 0 or h == type - 1):
                            height.append(edge(d, h, l))
                        elif l == 1 and h == 1:
                            height.append("core")
                        else:
                            height.append(center(d, h, l))

                depth.append(height)
            self.cubeMatrix.append(depth)
        print(self.cubeMatrix)

    def getSide(self, axis, side):
        #included pieces
        piecesToMove = []
        #Use for U, D, and E
        if axis == 0:
            for d in self.cubeMatrix:
                for h in enumerate(d):
                    if h[0] == side:
                        for l in h[1]:
                            piecesToMove.append(l)

        #Use for F, B, and S
        elif axis == 1:
            for d in enumerate(self.cubeMatrix):
                print(d)
                if d[0] == side:
                    for h in d[1]:
                        for l in h:
                            piecesToMove.append(l)


        #Use for R, L, and M
        elif axis == 2:
            for d in self.cubeMatrix:
                for h in d:
                    for l in enumerate(h):
                        if l[0] == side:
                            piecesToMove.append(l[1])
        print(piecesToMove)

    def scramble(self, type):
        pass

    def doMove(self, move, type):
        moveList = "RLMFBSUDER'L'M'F'B'S'U'D'E'"
        #Get side
        #Move side list, change rotation, if = 2pi, change back to 0
        #Replace original pieces


    def rotateCube(self, dir, type):
        pass


# Actual Window
class game:
    #Create window
    #Create Puzzle from init parameters
    #Make puzzle in 3D
    #Other functionality
    pass


def main():
    puzzle1 = puzzle(3)
    puzzle1.getSide(0, 0)


if __name__ == '__main__':
    main()
