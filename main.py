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

    def scramble(self, type):
        pass

    def doMove(self, move, type):
        pass

    def rotateCube(self, dir, type):
        pass


# Tile class as super with different types as a sub class
class tile:
    # In Radians with the default being front right bottom facing
    def __init__(self, depth, height, length):
        self.depth = depth
        self.height = height
        self.length = length
        self.colors = {"side1": "", "side2": "", "side3": ""}
        self.rotationVector = [0.0, 0.0, 0.0]


class edge(tile):
    def __init__(self, depth, height, length):
        super().__init__(depth, height, length)
        #For side 1
        if self.depth == 0:
            self.colors["side1"] = "green"
        elif self.depth == 2:
            self.colors["side1"] = "blue"
        else:
            if self.height == 0 or self.height == 2:
                if self.length == 0:
                    self.colors["side1"] = "orange"
                elif self.length == 2:
                    self.colors["side1"] = "red"

        #Side 2
        #if self.depth == 0 or self.depth == 2:
        if self.height == 0:
            self.colors["side2"] = "white"
        elif self.height == 2:
            self.colors["side2"] = "yellow"
        else:
            if self.length == 0:
                self.colors["side2"] = "orange"
            elif self.length == 2:
                self.colors["side2"] = "red"

    def __repr__(self):
        return f"Color {self.colors}, Rotation: {self.rotationVector}"



class center(tile):
    def __init__(self, depth, height, length):
        super().__init__(depth, height, length)
        if self.depth == 0:
            self.colors["side1"] = "green"
        elif self.depth == 2:
            self.colors["side1"] = "blue"
        else:
            if self.height == 0:
                self.colors["side1"] = "white"
            elif self.height == 2:
                self.colors["side1"] = "yellow"
            else:
                if self.length == 0:
                    self.colors["side1"] = "orange"
                elif self.length == 2:
                    self.colors["side1"] = "red"
    def __repr__(self):
        return f"Color {self.colors}, Rotation: {self.rotationVector}"


class corner(tile):
    def __init__(self, depth, height, length):
        super().__init__(depth, height, length)
        #Side 1
        if self.depth == 0:
            self.colors["side1"] = "green"
        elif self.depth == 2:
            self.colors["side1"] = "blue"
        #Side 2
        if self.height == 0:
            self.colors["side2"] = "white"
        elif self.height == 2:
            self.colors["side2"] = "yellow"
        #Side 3
        if self.length == 0:
            self.colors["side3"] = "orange"
        elif self.length == 2:
            self.colors["side3"] = "red"
    def __repr__(self):
        return f"Color {self.colors}, Rotation: {self.rotationVector}"


# Actual Window
class game:
    pass


def main():
    puzzle1 = puzzle(3)


if __name__ == '__main__':
    main()
