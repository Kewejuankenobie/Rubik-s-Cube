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
    def __repr__(self):
        return "Undefined Or Core"

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

if __name__ == "__main__":
    print("This is the tile class")