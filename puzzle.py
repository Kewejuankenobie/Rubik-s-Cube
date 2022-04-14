# Class describing the puzzle
from tile import *

class puzzle:
    seed = 0
    #Makes a puzzle that the computer understands
    def __init__(self, type):
        self.type = type
        self.cubeMatrix = []
        # Makes a cube represented as a 3D matrix with peice types
        for d in range(type):
            depth = []
            for h in range(type):
                height = []
                for l in range(type):
                    height.append(tile(d, h, l, ["y", "m", "b", "r", "g", "w"])) #Now color order based on perspective

                depth.append(height)
            self.cubeMatrix.append(depth)

    def getState(self)-> list:
        return self.cubeMatrix

    def getSide(self, posAxis)-> tuple: #(axis, side)
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

    #Debating on how to impliment a scramble
    def scramble(self, type)-> str:
        pass

    def doMove(self, move): # Add something so when in 3D space, can do it based on reletive rotation
        def getMove(m)-> tuple:
            match m:
                case "R":
                    return ([2, 2], -1)
                case "R'":
                    return ([2, 2], 1)
                case "L":
                    return ([2, 0], 1)
                case "L'":
                    return ([2, 0], -1)
                case "M":
                    return ([2, 1], 1)
                case "M'":
                    return ([2, 1], -1)
                case "F":
                    return ([1, 2], -1)
                case "F'":
                    return ([1, 2], 1)
                case "B":
                    return ([1, 0], 1)
                case "B'":
                    return ([1, 0], -1)
                case "S":
                    return ([1, 1], 1)
                case "S'":
                    return ([1, 1], -1)
                case "U":
                    return ([0, 2], 1)
                case "U'":
                    return ([0, 2], -1)
                case "D":
                    return ([0, 0], -1)
                case "D'":
                    return ([0, 0], 1)
                case "E":
                    return ([0, 1], -1)
                case "E'":
                    return ([0, 1], 1)
                #Cube Rotations
                case "X":
                    return ([2, 4], -1)
                case "X'":
                    return ([2, 4], 1)
                case "Y":
                    return ([0, 4], 1)
                case "Y'":
                    return ([0, 4], -1)
                case "Z":
                    return ([1, 4], -1)
                case "Z'":
                    return ([1, 4], 1)

        moveList = "R L M F B S U D E X Y Z R' L' M' F' B' S' U' D' E' X' Y' Z'"
        moveList = moveList.split(" ")
        #Get side
        if move in moveList:
            moveInProgress = getMove(move)
            #For Cube Rotation
            if moveInProgress[0][1] == 4:
                for s in range(3):
                    moveInProgress[0][1] = s
                    side = self.getSide(moveInProgress[0])
                    self.rotateCube(side[0], moveInProgress, side[1])
            #For individual layer
            else:
                side = self.getSide(moveInProgress[0])
                self.rotateCube(side[0], moveInProgress, side[1])
            #get side, rotate cube, print  right at the end

        else:
            print("Enter a valid move")
        #Move side list, change rotation, if = 2pi, change back to 0
        #Replace original pieces

    def rotateCube(self, side, dir, pos): # rotates the actual side
        #Rotates Side
        multiplyer = dir[1] #will be 1 or -1 for itterating through the list via multiplying

        # R moves 1 to 5, 5 to 6, 6 to 3, 3 to 1
        # U moves 2 to 3, 3 to 4, 4 to 5, 5 to 2
        # F moves 1 to 2, 2 to 6, 6 to 4, 4 to 1
        # Use cube rotation moves for rotating cube, makes easy

        #Sets colors of cube depending on move
        for row in side:
            for piece in row:
                dupeColor = [c for c in piece.color]
                if dir[0][0] == 2:
                    if dir[1] == -1:
                        piece.color[4] = dupeColor[0]
                        piece.color[5] = dupeColor[4]
                        piece.color[2] = dupeColor[5]
                        piece.color[0] = dupeColor[2]
                    elif dir[1] == 1:
                        piece.color[2] = dupeColor[0]
                        piece.color[5] = dupeColor[2]
                        piece.color[4] = dupeColor[5]
                        piece.color[0] = dupeColor[4]
                elif dir[0][0] == 1:
                    if dir[1] == -1:
                        piece.color[1] = dupeColor[0]
                        piece.color[5] = dupeColor[1]
                        piece.color[3] = dupeColor[5]
                        piece.color[0] = dupeColor[3]
                    elif dir[1] == 1:
                        piece.color[3] = dupeColor[0]
                        piece.color[5] = dupeColor[3]
                        piece.color[1] = dupeColor[5]
                        piece.color[0] = dupeColor[1]
                elif dir[0][0] == 0:
                    if dir[1] == -1:
                        piece.color[4] = dupeColor[1]
                        piece.color[3] = dupeColor[4]
                        piece.color[2] = dupeColor[3]
                        piece.color[1] = dupeColor[2]
                    elif dir[1] == 1:
                        piece.color[2] = dupeColor[1]
                        piece.color[3] = dupeColor[2]
                        piece.color[4] = dupeColor[3]
                        piece.color[1] = dupeColor[4]

            #Rearange Matrix by finding transpose and reversing the order of each row (Linear Algebra)
        for d in range(2 - dir[1]):
            for i in range(3):
                for j in range(i):
                    temporaryMatrix = side[i][j]
                    side[i][j] = side[j][i]
                    side[j][i] = temporaryMatrix
            for i in range(3):
                side[i].reverse()

        #Put rotated side back into original cube matrix
        #Do for depending on axis, it changes like getting the side
        for d in enumerate(self.cubeMatrix):
            depth = d[0]
            for h in enumerate(d[1]):
                height = h[0]
                for l in enumerate(h[1]):
                    length = l[0]
                    if [depth, height, length] in pos:
                        self.cubeMatrix[depth][height][length] = side[0][0]
                        side[0].pop(0)
                        if len(side[0]) == 0:
                            side.pop(0)