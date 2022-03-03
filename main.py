# Class describing the puzzle
import math
from tile import tile, corner, edge, center

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
                            height.append(tile(d, h, l))
                        else:
                            height.append(center(d, h, l))

                depth.append(height)
            self.cubeMatrix.append(depth)
        print(self.cubeMatrix)

    def getSide(self, posAxis): #(axis, side)
        #included pieces
        piecesToMove2D = []
        piecePositionsList = []
        #Use for U, D, and E
        if posAxis[0] == 0:
            for d in self.cubeMatrix:
                depth = self.cubeMatrix.index(d)
                piecesToMove = []
                for h in enumerate(d):
                    if h[0] == posAxis[1]:
                        height = d.index(h[1])
                        for l in h[1]:
                            length = h[1].index(l)
                            piecesToMove.append(l)
                            piecePositionsList.append([depth, height, length])
                piecesToMove2D.append(piecesToMove)

        #Use for F, B, and S
        elif posAxis[0] == 1:
            for d in enumerate(self.cubeMatrix):
                if d[0] == posAxis[1]:
                    depth = self.cubeMatrix.index(d[1])
                    for h in d[1]:
                        height = d[1].index(h)
                        piecesToMove = []
                        for l in h:
                            length = h.index(l)
                            piecesToMove.append(l)
                            piecePositionsList.append([depth, height, length])
                        piecesToMove2D.append(piecesToMove)


        #Use for R, L, and M
        elif posAxis[0] == 2:
            for d in self.cubeMatrix:
                depth = self.cubeMatrix.index(d)
                piecesToMove = []
                for h in d:
                    height = d.index(h)
                    for l in enumerate(h):
                        if l[0] == posAxis[1]:
                            length = h.index(l[1])
                            piecesToMove.append(l[1])
                            piecePositionsList.append([depth, height, length])
                piecesToMove2D.append(piecesToMove)
        return (piecesToMove2D, piecePositionsList)

    def scramble(self, type):
        pass

    def doMove(self, move): # Add something so when in 3D space, can do it based on reletive rotation
        def getMove(m):
            match m:
                case "R":
                    return ((2, 2), -1)
                case "R'":
                    return ((2, 2), 1)
                case "L":
                    return ((2, 0), 1)
                case "L'":
                    return ((2, 0), -1)
                case "M":
                    return ((2, 1), 1)
                case "M'":
                    return ((2, 1), -1)
                case "F":
                    return ((1, 0), 1)
                case "F'":
                    return ((1, 0), -1)
                case "B":
                    return ((1, 2), -1)
                case "B'":
                    return ((1, 2), 1)
                case "S":
                    return ((1, 2), 1)
                case "S'":
                    return ((1, 2), -1)
                case "U":
                    return ((0, 0), -1)
                case "U'":
                    return ((0, 0), 1)
                case "D":
                    return ((0, 2), 1)
                case "D'":
                    return ((0, 2), -1)
                case "E":
                    return ((0, 1), 1)
                case "E'":
                    return ((0, 1), -1)

        moveList = "R L M F B S U D E R' L' M' F' B' S' U' D' E'"
        moveList = moveList.split(" ")
        #Get side
        if move in moveList:
            moveInProgress = getMove(move)
            side = self.getSide(moveInProgress[0])
            self.rotateCube(side, moveInProgress)
            print(self.cubeMatrix)
            #get side, rotate cube, print  right at the end

        else:
            print("Enter a valid move")
        #Move side list, change rotation, if = 2pi, change back to 0
        #Replace original pieces


    def rotateCube(self, side, dir): # rotates the actual side
        for h in side:
            for l in h:
                l.rotation[dir[0][0]] += dir[1] * math.pi / 2
                if l.rotation[dir[0][0]] >= 2 * math.pi or l.rotation[2] <= -2 * math.pi:
                    l.rotation[dir[0][0]] = 0.0
            #Rearange Matrix by finding transpose and reversing the order of each row (Linear Algebra)
        print(side)
        for d in range(2 - dir[1]):
            for i in range(3):
                for j in range(i):
                    temporaryMatrix = side[i][j]
                    side[i][j] = side[j][i]
                    side[j][i] = temporaryMatrix
            for i in range(3):
                side[i].reverse()
        print(side)
        #Put rotated side back into original cube matrix
        #Do for depending on axis, it changes like getting the side
        if dir[0][0] == 0:
            for d in self.cubeMatrix:
                for h in enumerate(d):
                    if h[0] == dir[0][1]:
                        for l in h[1]:
                            l = side
        elif dir[0][0] == 1:
            pass
        else:
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
    puzzle1.doMove("R")
    #puzzle1.doMove("B")
    #puzzle1.doMove("U")


if __name__ == '__main__':
    main()
