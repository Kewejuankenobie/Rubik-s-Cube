import math

# Tile class as super with different types as a sub class
class tile:
    # In Radians with the default being front right bottom facing
    def __init__(self, depth, height, length):
        self.depth = depth
        self.height = height
        self.length = length
        self.colors = {"s1": "", "s2": "", "s3": ""}
        self.rotation = [0.0, 0.0, 0.0]
    def __repr__(self):
        return "Undefined Or Core"

#Rotation, 0 axis is up and down, 1 axis is front and back, 2 axis is left and right

class edge(tile):
    def __init__(self, depth, height, length):
        super().__init__(depth, height, length)
        #For side 1
        if self.depth == 0:
            self.colors["s1"] = "g"
            self.rotation[0] = 0.0
        elif self.depth == 2:
            self.colors["s1"] = "b"
            self.rotation[0] = math.pi
        else:
            if self.height == 0 or self.height == 2:
                if self.length == 0:
                    self.colors["s1"] = "o"
                    self.rotation[0] = (3 * math.pi) / 2
                elif self.length == 2:
                    self.colors["s1"] = "r"
                    self.rotation[0] = math.pi / 2
        #Side 2
        #if self.depth == 0 or self.depth == 2:
        if self.height == 0:
            self.colors["s2"] = "w"
            self.rotation[1] = 0
        elif self.height == 2:
            self.colors["s2"] = "y"
            self.rotation[1] = math.pi
        else:
            if self.length == 0:
                self.colors["s2"] = "o"
                self.rotation[1] = math.pi / 2
            elif self.length == 2:
                self.colors["s2"] = "r"
                self.rotation[1] = (3 * math.pi) / 2
    def __repr__(self):
        return f"(Color {self.colors}, Rotation: {self.rotation})"



class center(tile):
    def __init__(self, depth, height, length):
        super().__init__(depth, height, length)
        if self.depth == 0:
            self.colors["s1"] = "g"
            self.rotation[0] = 0.0
        elif self.depth == 2:
            self.colors["s1"] = "b"
            self.rotation[0] = math.pi
        else:
            if self.height == 0:
                self.colors["s1"] = "w"
                self.rotation[2] = math.pi / 2
            elif self.height == 2:
                self.colors["s1"] = "y"
                self.rotation[2] = (3 * math.pi) / 2
            else:
                if self.length == 0:
                    self.colors["s1"] = "o"
                    self.rotation[0] = (3 * math.pi) / 2
                elif self.length == 2:
                    self.colors["s1"] = "r"
                    self.rotation[0] = math.pi / 2
    def __repr__(self):
        return f"(Color {self.colors}, Rotation: {self.rotation})"


class corner(tile):
    def __init__(self, depth, height, length):
        super().__init__(depth, height, length)
        #Side 1
        if self.depth == 0:
            self.colors["s1"] = "g"
            self.rotation[0] = 0.0
        elif self.depth == 2:
            self.colors["s1"] = "b"
            self.rotation[0] = math.pi
        #Side 2
        if self.height == 0:
            self.colors["s2"] = "w"
            self.rotation[1] = 0.0
        elif self.height == 2:
            self.colors["s2"] = "y"
            self.rotation[1] = math.pi
        #Side 3
        if self.length == 0:
            self.colors["s3"] = "o"
            self.rotation[2] = math.pi
        elif self.length == 2:
            self.colors["s3"] = "r"
            self.rotation[2] = 0.0
    def __repr__(self):
        return f"(Color {self.colors}, Rotation: {self.rotation})"

if __name__ == "__main__":
    print("This is the tile class")