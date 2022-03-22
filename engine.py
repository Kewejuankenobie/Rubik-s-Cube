import math
import pygame as pg
from pygame.locals import *
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class point():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getZ(self):
        return self.z

class Vector3():
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.firstPoint = point(x1, y1, z1)
        self.secondPoint = point(x2, y2, z2)
    def x(self):
        return self.secondPoint.getX() - self.firstPoint.getX()
    def y(self):
        return self.secondPoint.getY() - self.firstPoint.getY()
    def z(self):
        return self.secondPoint.getZ() - self.firstPoint.getZ()
    def magnitude(self):
        return math.sqrt(self.x() ** 2 + self.y() ** 2 + self.z() ** 2)

class cube:
    def __init__(self, type, i):
        self.type = type
        self.i = i
        #Make verticies 0 to 1, 1 to 2, 2 to 3
        self.vertecies = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 0], [0, 0, 1], [1, 0, 1], [0, 1, 1], [1, 1, 1]]
        self.orgVertecies = self.vertecies
        for v in self.vertecies:
            print(v)
            print(i)
            #Need to itterate correctly
            v[0] += i[0]
            v[1] += i[1]
            v[2] += i[2]

        #Make lines
        self.lines = ((0, 1), (0, 2), (0, 4), (1, 5), (1, 3), (2, 3), (2, 6),
                 (3, 7), (4, 5), (4, 6), (5, 7), (6, 7))

        self.quads = [(0, 1, 3, 2), (0, 1, 5, 4), (0, 2, 6, 4), (1, 3, 7, 5), (4, 5, 7, 6), (2, 3, 7, 6)]
        #create cube at that position

 # Solid Cube
        glBegin(GL_QUADS)
        r = 0.0
        b = 0.0
        g = 1.0
        for cubeQuad in self.quads:

            for cubeVertex in cubeQuad:
                glColor3f(r, g, b)  # color

                glVertex3fv(self.vertecies[cubeVertex])  # Draw quads from points inputed
        glEnd()

        glBegin(GL_LINES)  # Tells start gl code and how to handle
        for cubeEdge in self.lines:
            for cubeVertex in cubeEdge:
                glColor(0, 0, 0)
                glVertex3fv(self.vertecies[cubeVertex])  # Draw lines between the points inputed
        glEnd()


    def recolorSides(self):
        pass

class game:
    def __init__(self):
        self.canQuit = True
        pg.init()
        display = (500, 500)
        pg.display.set_mode(display, DOUBLEBUF | OPENGL)  # Sets display mode to openGL
        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)  # Sets up Camera
        glTranslatef(-2, -1, -8)  # Sets translation of the camera
        glRotatef(30, 1, 1, 0.5)  # Sets rotation of the camera
            # glRotatef(1, 3, 1, 1)
            # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #Clears color and depth
            # cube1 = cube("test", 1)
        pg.display.flip()  # Updates display
            # pg.time.wait(10) #How often updated

    def allowQuit(self):
        for event in pg.event.get():  # Adds ability to quit
            if event.type == pg.QUIT:
                pg.quit()
                quit()

    def makeCube(self, pos):
        self.canQuit = False
        #glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        #glLoadIdentity()
        newCube = cube("test", pos)
        #glutSwapBuffers()
        self.canQuit = True

    def updateDisplay(self):
        pg.display.flip()


def main():
    new = game()
    '''#vec1 = Vector3(3, 4, 5, 1, 2, 1)
    #print(vec1.magnitude())
    pg.init()
    display = (500, 500)
    pg.display.set_mode(display, DOUBLEBUF | OPENGL)  # Sets display mode to openGL
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)  # Sets up Camera
    glTranslatef(0.0, -1, -8)  # Sets translation of the camera
    glRotatef(30, 1, 1, 0)  # Sets rotation of the camera

    while True:
        # glRotatef(1, 3, 1, 1)
        # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #Clears color and depth
        cube1 = cube("test", 1)
        pg.display.flip()  # Updates display
        # pg.time.wait(10) #How often updated
        for event in pg.event.get():  # Adds ability to quit
            if event.type == pg.QUIT:
                pg.quit()
                quit()'''

if __name__ == "__main__":
    main()

