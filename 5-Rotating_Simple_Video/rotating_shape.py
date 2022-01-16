# ayengec
# OpenGL rotating shape example for github
# 

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time

window = 0
 
FPS_RATE = 120    # it can be 60, 30 etc...
x_axis, y_axis, z_axis = 0.0, 0.0, 0.0
t0 = 0


def InitScreen(Width, Height): 
 
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0) 
        glDepthFunc(GL_LESS)     # specify the value used for depth buffer comparisons,  GL_LESS:Passes if the incoming depth value is less than the stored depth value.
        glEnable(GL_DEPTH_TEST)  # enable or disable server-side GL capabilities: 
        # GL_DEPTH_TEST:do depth comparisons and update the depth buffer. Note that even if the depth buffer exists and the depth mask is non-zero, 
        # the depth buffer is not updated if the depth test is disabled

        glShadeModel(GL_FLAT)   # selects flat or smooth shading
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()        # replace the current matrix with the identity matrix
        gluPerspective(60.0, float(Width)/float(Height), 0.5, 5.0)  
        # fovy: The field of view angle, in degrees, in the y-direction.
        # aspect: The aspect ratio that determines the field of view in the x-direction. The aspect ratio is the ratio of x (width) to y (height).
        # zNear: The distance from the viewer to the near clipping plane (always positive).
        # zFar: The distance from the viewer to the far clipping plane (always positive).

        glMatrixMode(GL_MODELVIEW)   # specify which matrix is the current matrix
 
def drawCubeGL():

        global x_axis,y_axis,z_axis, t0
 
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
 
        glLoadIdentity()
        glTranslatef(0.0,0.0,-4.0)   # multiply the current matrix by a translation matrix, specify the x, y, and z coordinates of a translation vector
 
        glRotatef(x_axis,1.0,0.0,0.0)
        glRotatef(y_axis,0.0,1.0,0.0)
        glRotatef(z_axis,0.0,0.0,1.0)
 
        # Draw Cube (multiple quads)
        glBegin(GL_QUADS)  # begin drawing of quads
 
        glColor3f(0.5,0.5,0.5)
        glVertex3f( 1.0, 1.0,-1.0)
        glVertex3f(-1.0, 1.0,-1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f( 1.0, 1.0, 1.0) 
 
        glColor3f(1.0,0.0,0.0)
        glVertex3f( 1.0,-1.0, 1.0)
        glVertex3f(-1.0,-1.0, 1.0)
        glVertex3f(-1.0,-1.0,-1.0)
        glVertex3f( 1.0,-1.0,-1.0) 
 
        glColor3f(0.0,1.0,0.0)
        glVertex3f( 1.0, 1.0, 1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f(-1.0,-1.0, 1.0)
        glVertex3f( 1.0,-1.0, 1.0)
 
        glColor3f(1.0,1.0,0.0)
        glVertex3f( 1.0,-1.0,-1.0)
        glVertex3f(-1.0,-1.0,-1.0)
        glVertex3f(-1.0, 1.0,-1.0)
        glVertex3f( 1.0, 1.0,-1.0)
 
        glColor3f(0.0,0.0,1.0)
        glVertex3f(-1.0, 1.0, 1.0) 
        glVertex3f(-1.0, 1.0,-1.0)
        glVertex3f(-1.0,-1.0,-1.0) 
        glVertex3f(-1.0,-1.0, 1.0) 
 
        glColor3f(1.0,1.0,1.0)
        glVertex3f( 1.0, 1.0,-1.0) 
        glVertex3f( 1.0, 1.0, 1.0)
        glVertex3f( 1.0,-1.0, 1.0)
        glVertex3f( 1.0,-1.0,-1.0)

        glEnd()
 
        x_axis = x_axis - 0.25
        z_axis = z_axis - 0.25

        t1 = time.process_time()
        print("t1 = ", t1)
        print("1 frame drawing time elapsed: " + str((t1-t0)*1000) + " ms")
        t0 = t1
        time.sleep(1/(1.05*FPS_RATE))
        fpstick2= time.process_time()
        print("fpstick2 = ", fpstick2+0.016)
        print("Frame Per Second: " + str(1/((fpstick2+1/(1.05*FPS_RATE))-t0)) + " fps") # FPS for every drawing process

        glutSwapBuffers()  # swaps the buffers of the current window if double buffered

def main():
 
        global window
 
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(1024,768)
        glutInitWindowPosition(250,320)

        window = glutCreateWindow('ayengec Python Moving Cube')
    
        glutDisplayFunc(drawCubeGL)
        glutIdleFunc(drawCubeGL)
        InitScreen(1024, 768)
        glutMainLoop()

 
if __name__ == "__main__":
        main() 
