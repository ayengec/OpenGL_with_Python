# ayengec
# github OpenGL examples with python
# github.com/ayengec

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_circle():
    glClear(GL_COLOR_BUFFER_BIT)   # we declare which buffer we want to clear

    glColor3f(0.1, 0.9, 0.1)

    glBegin(GL_POLYGON)#begin drawing of polygon

    glVertex3f(-0.5,0.5,0.0)    #first vertex
    glVertex3f(0.5,0.5,0.0)     #second vertex
    glVertex3f(1.0,0.0,0.0)     #third vertex
    glVertex3f(0.5,-0.5,0.0)    #fourth vertex
    glVertex3f(-0.5,-0.5,0.0)   #fifth vertex
    glVertex3f(-1.0,0.0,0.0)    #sixth vertex

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