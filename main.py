import pygame as pg
import numpy as np
import pygame.event
import pygame.gfxdraw
from matrix_functions import *
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
            elif xaxis == 3:
                object.append([x, 300, z + 200, 1])
                object.append([x, 300, z - 200, 1])
                object.append([x, -300, z - 200, 1])
                object.append([x, -300, z + 200, 1])
                object.append([x, 300, z + 200, 1])
                objectcoordinates.append(object)
                object = []

            x += 200
        z -= 200
    return objectcoordinates



def raycaster(objectcoordinates):

    t = 640 / np.dot(objectcoordinates, [0, 0, 1, 0])
    if t < 0:
        return objectcoordinates * 0
    else:
        scaled = objectcoordinates * t
        return scaled

def drawer(points, camerapos, cameradirection):
        coordinates_for_polygon = []
        for point in points:
            count = 0
            lastx = 0
            lasty = 0

            coordinates_for_polygon = []

            for i in point:

                i = i + camerapos
                i = rotate_y(a) @ i
                i = rotate_x(b) @ i

                i = i - camerapos

                i = i + camerapos
                i = raycaster(i)

                count += 1

                if np.array_equal(np.absolute(i), [0, 0, 0, 0]):
                    break
                x = i[0] + 960
                y = i[1] + 540

                coordinates_for_polygon.append([x, y])

                pg.draw.circle(background, black, (x, y), radius=3)
                if count > 1:
                    pg.draw.line(background, black, (lastx, lasty), (x, y), 3)

                lastx = x
                lasty = y
            try:
                pygame.gfxdraw.filled_polygon(background, [(coordinates_for_polygon[0]), (coordinates_for_polygon[1]), (coordinates_for_polygon[2])], yellow)
                pygame.gfxdraw.filled_polygon(background, [(coordinates_for_polygon[2]), (coordinates_for_polygon[3]), (coordinates_for_polygon[0])], yellow)
            except:
                pass

width, height = 1920, 1080
black = (0, 0, 0)
yellow = (252, 227, 3)
white = (255, 255, 255)
run = True



fps = pg.time.Clock()


np.set_printoptions(suppress=True)


a = 0
b = 0

worldmap_interpreted = interpreter(world)


camerapos = np.array([0, 0, 0, 0])
cameradirection = np.array([0, 0, 1, 0])

print(worldmap_interpreted)

timeinair = 0
velocity = 0

while run:
    fps.tick(60)

    mousemove = pg.mouse.get_rel()
    pg.mouse.set_visible(False)
    pg.event.set_grab(True)

    if camerapos[1] >= 0:
        velocity -= 0.5 * timeinair
        timeinair += 1
    elif camerapos[1] < 0:
        velocity = 0
        timeinair = 0
        camerapos[1] = 0

    if keyboard.is_pressed('space') and camerapos[1] < 2:
        velocity = 100
        camerapos[1] = -0.01

    camerapos[1] += velocity / 5


    if keyboard.is_pressed('a'):
        camerapos = camerapos - np.append((15 * np.cross(np.delete(cameradirection, 3), np.array([0, 1, 0]))), 0)

    if keyboard.is_pressed('d'):
        camerapos = camerapos + np.append((15 * np.cross(np.delete(cameradirection, 3), np.array([0, 1, 0]))), 0)

    if keyboard.is_pressed('w'):
        camerapos = camerapos - (15 * cameradirection)

    if keyboard.is_pressed('s'):
        camerapos = camerapos + (15 * cameradirection)

    a += (mousemove[0] * 0.01)
    cameradirection = rotate_y(-a) @ np.array([0, 0, 1, 0])

    b -= mousemove[1] * 0.01


    if keyboard.is_pressed('escape'):
        break
    background = pg.display.set_mode((width, height))
    background.fill(color=white)



    drawer(worldmap_interpreted,camerapos, cameradirection)

    pg.display.flip()




