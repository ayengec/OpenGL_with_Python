# ayengec
# github OpenGL examples with python
# github.com/ayengec

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_lines():
    glClear(GL_COLOR_BUFFER_BIT)   # we declare which buffer we want to clear

    glBegin(GL_LINES)              # starts to draw with its parameter line? point? triangle? polygon? etc...

    # First line
    glColor3f(0.5, 0.5, 0.0)       # color of the line in RGB mode
    glVertex2f(0.875, 1)           # start vertex:  x and y coordinates
    glVertex2f(-0.750, -0.5)       # end vertex  :  x and y coordinates

    # Second line
    glColor3f(0.0, 1.0, 0.2)
    glVertex2f(0.6, 0.3)
    glVertex2f(-4, -0.5)

    # Third line
    glColor3f(1, 0.0, 0.0)
    glVertex2f(0.1, -0.7)
    glVertex2f(1, -0.2)

    glEnd()        # every drawing statements must be between glBegin and glEnd

    glFlush()      # force execution of GL commands in finite time

if __name__ == "__main__":
    glutInit() # initialize GLUT library
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA) # initial display mode : with Bit mask to select a single buffered window and bit mask to select an RGBA mode window

    glutCreateWindow("ayengec_lines")  # creates "Square" named window
    gluOrtho2D(-1.0, 1.0,-1.0, 1.0)  # left, right, bottom, up  =>float coordinate ranges in [-1:1]:  
    glClearColor(0.2, 0.2, 0.2, 1.0) # red, green, blue, alpha  # To see different background color as GREY

    glutDisplayFunc(draw_lines)       # after created window, which shapes will be rendered

    glutMainLoop()