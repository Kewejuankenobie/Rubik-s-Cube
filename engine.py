import math
import pygame as pg
from pygame.locals import *
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class cube:
    def __init__(self, type, i, p):
        self.type = type
        self.i = i
        #Make verticies 0 to 1, 1 to 2, 2 to 3
        self.vertecies = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 0], [0, 0, 1], [1, 0, 1], [0, 1, 1], [1, 1, 1]]
        self.orgVertecies = self.vertecies
        for v in self.vertecies:
            #Oriented correctly now with green at front, red at right, white on top
            v[0] -= self.i[0]
            v[1] += self.i[1]
            v[2] += self.i[2]

        #Make lines
        self.lines = ((0, 1), (0, 2), (0, 4), (1, 5), (1, 3), (2, 3), (2, 6),
                 (3, 7), (4, 5), (4, 6), (5, 7), (6, 7)) #May not need

        self.quads = [(0, 1, 5, 4), (1, 3, 7, 5), (0, 1, 3, 2), (4, 5, 7, 6), (0, 2, 6, 4), (2, 3, 7, 6)]
        #create cube at that position

 # Solid Cube
        glBegin(GL_QUADS)
        for color in enumerate(p.color):
            match color[1]:
                case "y":
                    p.color[color[0]] = (1.0, 1.0, 0.0)
                case "m":
                    p.color[color[0]] = (1.0, 0.0, 1.0)
                case "b":
                    p.color[color[0]] = (0.0, 0.0, 1.0)
                case "r":
                    p.color[color[0]] = (1.0, 0.0, 0.0)
                case "g":
                    p.color[color[0]] = (0.0, 1.0, 0.0)
                case "w":
                    p.color[color[0]] = (1.0, 1.0, 1.0)
        for cubeQuad in enumerate(self.quads):
            match cubeQuad[0]:
                case 0:
                    glColor3f(p.color[0][0], p.color[0][1], p.color[0][2])  # color
                case 1:
                    glColor3f(p.color[1][0], p.color[1][1], p.color[1][2])
                case 2:
                    glColor3f(p.color[2][0], p.color[2][1], p.color[2][2])
                case 3:
                    glColor3f(p.color[3][0], p.color[3][1], p.color[3][2])
                case 4:
                    glColor3f(p.color[4][0], p.color[4][1], p.color[4][2])
                case 5:
                    glColor3f(p.color[5][0], p.color[5][1], p.color[5][2])

            for cubeVertex in cubeQuad[1]:

                glVertex3fv(self.vertecies[cubeVertex])  # Draw quads from points inputed
        glEnd()

        '''glBegin(GL_LINES)  # Tells start gl code and how to handle
        for cubeEdge in self.lines:
            for cubeVertex in cubeEdge:
                glColor(0, 0, 0)
                glVertex3fv(self.vertecies[cubeVertex])  # Draw lines between the points inputed
        glEnd()'''

class game:
    def __init__(self):
        self.canQuit = True
        pg.init()
        display = (500, 500)
        pg.display.set_mode(display, DOUBLEBUF | OPENGL)  # Sets display mode to openGL
        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)  # Sets up Camera
        glTranslatef(-1, -2, -10)  # Sets translation of the camera
        glRotatef(60, 0, 1, 0)  # Sets rotation of the camera
        glRotatef(15, 0, 0, 1)
        #glEnableClientState(GL_COLOR_ARRAY)
            # glRotatef(1, 3, 1, 1)
            # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #Clears color and depth
            # cube1 = cube("test", 1)
        pg.display.flip()  # Updates display
            # pg.time.wait(10) #How often updated

    def loopGame(self):
        for e in pg.event.get():  # Adds ability to quit and input text
            if e.type == pg.QUIT:
                pg.quit()
                quit()



    def makeCube(self, pos, piece):
        newCube = cube("test", pos, piece)

    def updateDisplay(self):
        pg.display.flip()


def main():
    new = game()
    newCube = new.makeCube([0, 0, 0], "l")
    new.updateDisplay()
    while True:
        new.loopGame()

if __name__ == "__main__":
    main()

