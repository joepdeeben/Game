import numpy
import pygame as pg
import numpy as np
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
        for point in points:
            count = 0
            lastx = 0
            lasty = 0
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
                x = i[0] + 320
                y = i[1] + 320



                pg.draw.circle(background, black, (x, y), radius=3)
                if count > 1:
                    pg.draw.line(background, black, (lastx, lasty), (x, y), 2)

                lastx = x
                lasty = y

width, height = 640, 640
black = (0, 0, 0)
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

    if camerapos[1] > 0:
        velocity -= 0.01 * timeinair
        timeinair += 1
    elif camerapos[1] <= 0:
        velocity = 0
        camerapos[1] = 0

    if keyboard.is_pressed('space'):
        velocity = 200

    camerapos[1] += velocity / 5
    print(camerapos)

    if keyboard.is_pressed('left arrow'):
        a -= 0.02
        cameradirection = rotate_y(-a) @ np.array([0, 0, 1, 0])
    if keyboard.is_pressed('a'):
        camerapos = camerapos - numpy.append((15 * np.cross(numpy.delete(cameradirection, 3), np.array([0, 1, 0]))), 0)
        print(camerapos)
    if keyboard.is_pressed('d'):
        camerapos = camerapos + numpy.append((15 * np.cross(numpy.delete(cameradirection, 3), np.array([0, 1, 0]))), 0)
        print(camerapos)
    if keyboard.is_pressed('w'):
        camerapos = camerapos - (15 * cameradirection)
        print(camerapos)
    if keyboard.is_pressed('s'):
        camerapos = camerapos + (15 * cameradirection)
        print(camerapos)
    if keyboard.is_pressed('right arrow'):
        a += 0.02
        cameradirection = rotate_y(-a) @ np.array([0, 0, 1, 0])
    if keyboard.is_pressed('up arrow'):
        b += 0.02
    if keyboard.is_pressed('down arrow'):
        b -= 0.02

    background = pg.display.set_mode((width, height))
    background.fill(color=white)

    drawer(worldmap_interpreted,camerapos, cameradirection)

    pg.display.flip()




