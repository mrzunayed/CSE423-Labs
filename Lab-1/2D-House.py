from OpenGL.GL import *
from OpenGL.GLUT import *

"""
Drawing a 2D house
"""


def draw_Lines(x1, y1, x2, y2):
    glPointSize(5)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()


def draw_Triangle(x1, y1, x2, y2, x3, y3):
    glPointSize(5)
    glBegin(GL_TRIANGLES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()


def draw_House():
    # Roof
    draw_Triangle(330, 170, 400, 235, 424, 208)
    draw_Lines(400, 235, 225, 260)
    draw_Lines(225, 260, 195, 230)
    draw_Lines(195, 230, 330, 170)

    # Side 1
    draw_Lines(340, 180, 338, 103)
    draw_Lines(338, 103, 383, 136)
    draw_Lines(383, 136, 416, 210)

    # Side 2
    draw_Lines(338, 103, 245, 165)
    draw_Lines(245, 165, 200, 225)

    # Lawn
    draw_Lines(228, 187, 200, 178)
    draw_Lines(200, 178, 340, 70)
    draw_Lines(340, 70, 425, 150)
    draw_Lines(425, 150, 400, 160)

    # Door
    draw_Lines(310, 120, 290, 180)
    draw_Lines(290, 180, 325, 165)
    draw_Lines(325, 165, 330, 110)

    # Window 1
    draw_Lines(357, 140, 385, 154)
    draw_Lines(385, 154, 396, 187)
    draw_Lines(396, 187, 362, 173)
    draw_Lines(362, 173, 357, 140)

    # Window 2
    draw_Lines(245, 180, 290, 154)
    draw_Lines(290, 154, 280, 187)
    draw_Lines(280, 187, 230, 210)
    draw_Lines(230, 210, 245, 180)

# -------------------------------------------------------


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
    draw_House()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab 1 Task 2")
glutDisplayFunc(showScreen)

glutMainLoop()
