# Tile class as each individual piece of the cube
#Each piece looks same based on perspective, different color list
#No need for rotation
class tile:
    # In Radians with the default being front right bottom facing
    def __init__(self, depth, height, length, color):
        self.depth = depth
        self.height = height
        self.length = length
        self.color = color#Make into list of colors in correct order
    def __repr__(self):
        return str(self.color)