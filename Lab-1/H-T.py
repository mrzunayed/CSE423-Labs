from OpenGL.GL import *
from OpenGL.GLUT import *

"""
Drawing H or T based on Student ID
"""


def draw_Points(x, y):
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def draw_DDA(x1, y1, x2, y2):
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(x1, y1)

    m = (y2 - y1) / (x2 - x1)
    while x1 < x2:
        x1 += 1
        y1 += m
        glVertex2f(x1, round(y1))
    glEnd()


def draw_Dash(x, y1, y2):
    for i in range(y1, y2, -10):
        draw_Points(x, i)


def draw_tail():
    draw_DDA(200, 350, 300, 350)
    draw_Dash(250, 350, 225)


def draw_head():
    draw_DDA(200, 290, 300, 290)
    draw_Dash(200, 350, 225)
    draw_Dash(300, 350, 225)


def toss(sid):
    if int(sid[-1]) % 2 == 0:
        draw_tail()
    else:
        draw_head()


# ------------------------------------------------

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
    toss(input("Student ID: "))
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab 1 Task 3")
glutDisplayFunc(showScreen)

glutMainLoop()
