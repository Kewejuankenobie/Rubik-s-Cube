# Tile class as super with different types as a sub class
#Remake so each piece looks same based on perspective, maybe different states
class tile:
    # In Radians with the default being front right bottom facing
    def __init__(self, depth, height, length, color):
        self.depth = depth
        self.height = height
        self.length = length
        self.color = color#Make into list of colors in correct order
    def __repr__(self):
        return str(self.color)

#Rotation, 0 axis is up and down, 1 axis is front and back, 2 axis is left and right

if __name__ == "__main__":
    print("This is the tile class")