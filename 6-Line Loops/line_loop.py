# ayengec
# OpenGL with Python
# github.com/ayengec
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_line_loop():

	glEnable(GL_LINE_SMOOTH)
	glViewport(0, 0, 1024, 768)	# select viewport on windows
	glClearColor(0,0,0,0)

	glPointSize(7.0)
	glColor4ub(255, 127, 0, 255)

	glLineWidth(1.0)
	glBegin(GL_LINE_LOOP)
	### to draw 6-8-10 triangle:
	glVertex2f(0.6, 0.0)
	glVertex2f(0.6, 0.8)
	glVertex2f(0.0, 0.0)

	glEnd() # every drawing statements must be between glBegin and glEnd

	glBegin(GL_POINTS)
	glColor4ub(255,0,0,255) # 1ST VERTEX RED
	glVertex2f(0.6, 0.0)

	glColor4ub(0,255,0,255) # 2ND VERTEX GREEN
	glVertex2f(0.6, 0.8)

	glColor4ub(0,0,255,255) # 3RD VERTEX BLUE
	glVertex2f(0.0, 0.0)

	glEnd()	# every drawing statements must be between glBegin and glEnd

	glFlush()	# force execution of GL commands in finite time. It is needed for OpenGL engines on PC

def main():

	glutInit() # initialize GLUT library
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA) # initial display mode : with Bit mask to select a single buffered window and bit mask to select an RGBA mode window
	glutInitWindowSize(1024,768)	# to create 1024x768 pixel window
	glutCreateWindow("ayengec_line_loop")	# creates "Square" named window

	glutDisplayFunc(draw_line_loop)	# after created window, which shapes will be rendered
	glutMainLoop()

if __name__ == "__main__":
	main() 
