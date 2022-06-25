from OpenGL.GL import *
from OpenGL.GLUT import *


def drawPoints(x, y):
    glPointSize(2.0)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def midPointCircle(X, Y, r):
    d = 1 - r
    x = 0
    y = r
    while x <= y:
        x += 1
        if d < 0:
            d += 2 * x + 1
        else:
            y -= 1
            d += 2 * (x - y) + 1
        drawPoints(X + x, Y + y)
        drawPoints(X - x, Y + y)
        drawPoints(X + x, Y - y)
        drawPoints(X - x, Y - y)
        drawPoints(X + y, Y + x)
        drawPoints(X - y, Y + x)
        drawPoints(X + y, Y - x)
        drawPoints(X - y, Y - x)


def midPointCircleLine(X, Y, r):
    d = 1 - r
    x = 0
    y = r
    while x <= y:
        x += 1
        if d < 0:
            d += 2 * x + 1
        else:
            y -= 1
            d += 2 * (x - y) + 1
        drawPoints(X + y, Y + x)
        drawPoints(X + y, Y - x)


def drawCircles():
    midPointCircle(200, 200, 50)
    midPointCircle(200, 300, 50)
    midPointCircleLine(200, 250, 150)


# --------------------------------------------------------


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 1.0)
    drawCircles()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab 3 Bonus")
glutDisplayFunc(showScreen)

glutMainLoop()
