# ayengec
# github OpenGL examples with python
# github.com/ayengec

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def draw_circle():
    glClear(GL_COLOR_BUFFER_BIT)   # we declare which buffer we want to clear

    glColor3f(0.1, 0.2, 0.9)
    glPointSize(15.0)

    glBegin(GL_POINTS)

    glVertex2f(0.8,0.75)   #upper-right corner
    glVertex2f(-0.4,-0.3) #lower-left corner
    glVertex2f(0.5,0.5)
    glVertex2f(0.0,0.0)


    glEnd()        # every drawing statements must be between glBegin and glEnd

    glFlush()      # force execution of GL commands in finite time

if __name__ == "__main__":
    glutInit() # initialize GLUT library
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA) # initial display mode : with Bit mask to select a single buffered window and bit mask to select an RGBA mode window

    glutCreateWindow("ayengec_lines")  # creates "Square" named window
    gluOrtho2D(-1.0, 1.0,-1.0, 1.0)  # left, right, bottom, up  =>float coordinate ranges in [-1:1]:  
    glClearColor(0.2, 0.2, 0.2, 1.0) # red, green, blue, alpha  # To see different background color as GREY

    glutDisplayFunc(draw_circle)       # after created window, which shapes will be rendered

    glutMainLoop()