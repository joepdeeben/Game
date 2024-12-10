import pygame
import pygame as pg
import numpy as np
from matrices import *
import keyboard
from resources.world import *

pg.init()




def interpreter(worldmap):
    objectcoordinates = []
    object = []
    z = 2000
    x = 0
    for zaxis in worldmap:
        x = 0
        for xaxis in zaxis:
            if xaxis == 1:
                object.append([x, 300, z, 1])
                object.append([x + 200, 300, z, 1])
                object.append([x + 200, -300, z, 1])
                object.append([x, -300, z, 1])
                object.append([x, 300, z, 1])
                objectcoordinates.append(object)
                object = []
            elif xaxis == 2:
                object.append([x, 300, z, 1])
                object.append([x, 300, z - 200, 1])
                object.append([x, -300, z - 200, 1])
                object.append([x, -300, z, 1])
                object.append([x, 300, z, 1])
                objectcoordinates.append(object)
                object = []

            x += 200
        z -= 200
    return objectcoordinates



def raycaster(objectcoordinates, res):

    t = res[0] / np.dot(objectcoordinates, [0, 0, 1, 0])
    if t < 0:
        return objectcoordinates * 0
    else:
        scaled = objectcoordinates * t
        return scaled

def drawer(points, camerapos, cameradirection, res):
    for point in points:
        transformed_points = []  # Store the projected 2D points for each rectangle

        for i in point:
            # Apply transformations
            i = i + camerapos
            i = rotate_y(a) @ i
            i = i - camerapos
            i = i + camerapos
            i = raycaster(i, res)

            # Skip invalid points
            if np.array_equal(np.absolute(i), [0, 0, 0, 0]):
                continue

            # Map 3D points to 2D screen coordinates
            x = i[0] + res[0] / 2
            y = i[1] + res[1] / 2

            transformed_points.append((x, y))
        print(transformed_points)
        # Fill the rectangle if it has enough points
        if len(transformed_points) >= 4: # Minimum points for a filled rectangle
            pg.draw.polygon(background, (0, 128, 255), transformed_points)  # Fill with blue color


        # Draw edges of the rectangle
        for j in range(len(transformed_points)):
            start = transformed_points[j]
            end = transformed_points[(j + 1) % len(transformed_points)]  # Loop back to the start
            pg.draw.line(background, black, start, end, 6)

width, height = 1920, 1080
black = (0, 0, 0)
white = (255, 255, 255)
run = True



fps = pg.time.Clock()


np.set_printoptions(suppress=True)


a = 0

worldmap_interpreted = interpreter(world)


camerapos = np.array([0, 0, 0, 0])
cameradirection = np.array([0, 0, 1, 0])

print(worldmap_interpreted)

background = pg.display.set_mode((width, height))
while run:
    for event in pg.event.get():  # Handle events
        if event.type == pg.QUIT:
            run = False  # Quit the loop when the window is closed
    fps.tick(60)

    if keyboard.is_pressed('left arrow'):
        a -= 0.02
        cameradirection = rotate_y(-a) @ np.array([0, 0, 1, 0])
    if keyboard.is_pressed('up arrow'):
        camerapos = camerapos - (15 * cameradirection)

    if keyboard.is_pressed('down arrow'):
        camerapos = camerapos + (15 * cameradirection)

    if keyboard.is_pressed('right arrow'):
        a += 0.02
        cameradirection = rotate_y(-a) @ np.array([0, 0, 1, 0])

    background.fill(color=white)


    drawer(worldmap_interpreted,camerapos, cameradirection, (width, height))
    pg.display.flip()


