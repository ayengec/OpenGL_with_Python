# ayengec
# OpenGL GPU 
# Triangle Strip rasterization, LETTER 'A' with triangle strip and a line


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_line_strip():

    glViewport(0, 0, 1024, 768)
    glClearColor(0,0,0,0)
    glLineWidth(3.0)
    glBegin(GL_TRIANGLE_STRIP)

    glColor4ub(255, 0, 0, 255)
    glVertex2f(-0.06, 0.00)
    glVertex2f(-0.1,  0.00)
    glVertex2f(-0.06, 0.04)
    glVertex2f(-0.1,  0.04)
    glVertex2f(-0.06, 0.08)
    glVertex2f(-0.1,  0.08)
    glVertex2f(-0.06, 0.12)
    glVertex2f(-0.1,  0.12)
    glVertex2f(-0.06, 0.16)
    glVertex2f(-0.1,  0.16)
    glVertex2f(-0.06, 0.24)
    glVertex2f(-0.1, 0.24)
    glVertex2f(-0.06, 0.24)
    glVertex2f(-0.06, 0.28)
    glVertex2f(-0.02, 0.24)
    glVertex2f(-0.02, 0.28)
    glVertex2f( 0.02, 0.24)
    glVertex2f( 0.02, 0.28)
    glVertex2f( 0.06, 0.24)
    glVertex2f( 0.02, 0.16)
    glVertex2f( 0.06, 0.16)
    glVertex2f( 0.02, 0.12)
    glVertex2f( 0.06, 0.12)
    glVertex2f( 0.02, 0.08)
    glVertex2f( 0.06, 0.08)
    glVertex2f( 0.02, 0.04)
    glVertex2f( 0.06, 0.04)
    glVertex2f( 0.02, 0.00)
    glVertex2f( 0.06, 0.00)
    glEnd() # every drawing statements must be between glBegin and glEnd


    glLineWidth(14.0)
    glBegin(GL_LINES)
    glColor4ub(255, 255, 0, 255)
    glVertex2f(-0.06, 0.12)
    glVertex2f(0.02, 0.12)

    glEnd()


    glFlush()# force execution of GL commands in finite time. It is needed for OpenGL engines on PC


def main():

    glutInit() # initialize GLUT library
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA) # initial display mode : with Bit mask to select a single buffered window and bit mask to select an RGBA mode window
    glutInitWindowSize(1024,768)
    glutCreateWindow("ayengec_triangle_strip")# creates "Square" named with    
    glutDisplayFunc(draw_line_strip)# after created window, which shapes will be rendered
    glutMainLoop()

if __name__ == "__main__":
    main() 
