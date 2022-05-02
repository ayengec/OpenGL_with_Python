# ayengec
# OpenGL with Python
# github.com/ayengec
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_line_strip():

    glEnable(GL_LINE_SMOOTH)
    glViewport(0, 0, 1024, 768)
    glClearColor(0,0,0,0)
    glPointSize(30.0)
    glColor4ub(255, 127, 0, 255)

    glLineWidth(4.0)
    glBegin(GL_LINE_STRIP)
    ###
    glVertex2f(0.5, -0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(-0.5, 0.5)
    glVertex2f(-0.5, -0.5)
    ###
    glVertex2f(0.25, -0.25)
    glVertex2f(0.25, 0.25)
    glVertex2f(-0.25, 0.25)
    glVertex2f(-0.25, -0.25)

    glEnd()     # every drawing statements must be between glBegin and glEnd

    glFlush()   # force execution of GL commands in finite time. It is needed for OpenGL engines on PC

def main():
    glutInit() # initialize GLUT library
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA) # initial display mode : with Bit mask to select a single buffered window and bit mask to select an RGBA mode window
    glutInitWindowSize(1024,768)
    glutCreateWindow("ayengec_line_strip")  # creates "Square" named window

    glutDisplayFunc(draw_line_strip)    # after created window, which shapes will be rendered
    glutMainLoop()

if __name__ == "__main__":
    main()
