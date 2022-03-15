import math
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

def clearScreen():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

def screen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

def main():
    vec1 = Vector3(3, 4, 5, 1, 2, 1)
    print(vec1.magnitude())

if __name__ == "__main__":
    main()

