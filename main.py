import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
from world import input_assembler, worldmap

width, height = 1920, 1080
np.set_printoptions(suppress=True)

worldmap_interpreted = input_assembler(worldmap)

sens = 0.005
sprint_speed = 0.01

def drawer(points):
    # Simply draw the triangles assuming that the current modelview and projection are set
    # We'll trust OpenGL to handle the perspective now.
    for point in points:
        if len(point) == 3:
            glBegin(GL_TRIANGLES)
            glColor3f(0.0, 0.5, 1.0)  # Blue color
            for vertex in point:
                # vertex is expected to be a [x, y, z, w]-like array; just use x,y,z
                glVertex3f(vertex[0], vertex[1], vertex[2])
            glEnd()

def main():
    # Initialize GLFW
    if not glfw.init():
        raise Exception("GLFW can't be initialized")

    window = glfw.create_window(1080, 1080, "OpenGL + GLFW Example", None, None)
    if not window:
        glfw.terminate()
        raise Exception("GLFW window can't be created")

    glfw.make_context_current(window)
    glfw.set_input_mode(window, glfw.CURSOR, glfw.CURSOR_DISABLED)
    last_mouse_pos = glfw.get_cursor_pos(window)

    glClearColor(1, 1, 1, 1.0)
    glEnable(GL_DEPTH_TEST)

    # Setup basic perspective
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Set a simple perspective: fov 60, aspect ratio, near 0.1, far 100.
    gluPerspective(60, width / float(height), 0.1, 100.0)

    camerapos = np.array([0.0, 0.0, 0.0])
    x_rotation = 0.0
    y_rotation = 0.0
    MAX_Y_ROTATION = np.pi / 2
    MIN_Y_ROTATION = -np.pi / 2

    # Main loop
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Get mouse position and calculate deltas
        mouse_x, mouse_y = glfw.get_cursor_pos(window)
        dx, dy = mouse_x - last_mouse_pos[0], mouse_y - last_mouse_pos[1]
        last_mouse_pos = (mouse_x, mouse_y)

        # Update rotations
        x_rotation -= dx * sens
        y_rotation += dy * sens
        y_rotation = max(MIN_Y_ROTATION, min(MAX_Y_ROTATION, y_rotation))

        # Handle movement input using GLFW
        # forward/backward
        forward = 0.0
        if glfw.get_key(window, glfw.KEY_W) == glfw.PRESS:
            forward = -1.0
        if glfw.get_key(window, glfw.KEY_S) == glfw.PRESS:
            forward = 1.0

        if glfw.get_key(window, glfw.KEY_LEFT_SHIFT) == glfw.PRESS:
            sprint_speed = 0.02
        else:
            sprint_speed = 0.01
        # strafe left/right
        strafe = 0.0
        if glfw.get_key(window, glfw.KEY_D) == glfw.PRESS:
            strafe = 1.0
        if glfw.get_key(window, glfw.KEY_A) == glfw.PRESS:
            strafe = -1.0

        # Apply camera movement
        # Calculate direction vectors based on x_rotation
        # We'll rotate a base vector [0,0,1] for forward and [1,0,0] for side.
        # Using simple trigonometry:
        # forward vector (in XZ plane) from x_rotation:
        # x_rotation here acts like yaw around Y-axis, so:
        forward_vec = np.array([np.sin(x_rotation), 0, np.cos(x_rotation)])
        side_vec = np.array([np.cos(x_rotation), 0, -np.sin(x_rotation)])

        camerapos += forward * sprint_speed * forward_vec
        camerapos += strafe * sprint_speed * side_vec

        # Set modelview matrix
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # Rotate the scene according to the camera rotations
        # Note: In many setups, x_rotation is yaw (rotate around Y) and y_rotation is pitch (rotate around X)
        glRotatef(np.degrees(y_rotation), 1, 0, 0)  # pitch
        glRotatef(-np.degrees(x_rotation), 0, 1, 0) # yaw
        glTranslatef(-camerapos[0], -camerapos[1], -camerapos[2])

        # Draw the world
        drawer(worldmap_interpreted)

        # Swap buffers and poll events
        glfw.swap_buffers(window)
        glfw.poll_events()
        glFlush()

    # Terminate GLFW
    glfw.terminate()

if __name__ == "__main__":
    main()
