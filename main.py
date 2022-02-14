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
                            height.append(center(d, h, l))
                        else:
                            print(d, h, l)
                            print(edge(d,h,l))
                            e = edge(d, h, l)
                            height.append(e)
                    else:
                        if (l == 0 or l == type - 1) and (h == 0 or h == type - 1):
                            print(edge(d, h, l))
                            e = edge(d, h, l)
                            height.append(e)
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
    def __init__(self, depth, height, length):
        super().__init__(depth, height, length)
        if self.depth == 0:
            self.colors["side1"] = "green"
            self.rotationVector[0] = 0.0
        elif self.depth == 2:
            self.colors["side1"] = "blue"
            self.rotationVector[0] = math.pi
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
    pass


# Actual Window
class game:
    pass


def main():
    puzzle1 = puzzle(3)
    cList = []
    e = edge(0, 1, 2)
    cList.append(e)
    e2 = edge(1, 2, 0)
    cList.append(e2)
    print(cList)


if __name__ == '__main__':
    main()
