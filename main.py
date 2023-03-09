import pygame
import pygame as pg
import numpy as np
from matrices import *
import keyboard

pg.init()

#reejtreesing

width, height = 640, 640
black = (0, 0, 0)
white = (255, 255, 255)
run = True



fps = pg.time.Clock()



points = []
points.append(np.array([-300, -300, 1280, 1]))
points.append(np.array([-300, 300, 1280, 1]))
points.append(np.array([300, 300, 1280, 1]))
points.append(np.array([300, -300, 1280, 1]))

points2 = []
points2.append(np.array([300, 300, 1280, 1]))
points2.append(np.array([300, -300, 1280, 1]))
points2.append(np.array([300, -300, 840, 1]))
points2.append(np.array([300, 300, 840, 1]))
points2.append(np.array([300, 300, 1280, 1]))


objectlist = [points, points2]

np.set_printoptions(suppress=True)

def raycaster(objectcoordinates):

    t = 640 / np.dot(objectcoordinates, [0, 0, 1, 0])
    scaled = objectcoordinates * t
    return scaled

a = 0
m = 0



camerapos = np.array([0, 0, 0, 0])
cameradirection = np.array([0, 0, 1, 0])

def draw_points(points, camerapos, cameradirection):
    count = 0
    print(points)
    for object in objectlist:
        for i in object:
            print(i)
            print(camerapos)
            i = i + camerapos
            i = rotate_y(a) @ i

            print(cameradirection)
            i = i - camerapos


            i = i + camerapos
            i = raycaster(i)
            count += 1

            x = i[0] + 320
            y = i[1] + 320

            pg.draw.circle(background, black, (x, y), radius=3)
            if count > 1:
                pg.draw.line(background, black, (lastx, lasty), (x, y), 2)

            lastx = x
            lasty = y

while run:
    fps.tick(60)

    if keyboard.is_pressed('left arrow'):
        a -= 0.01
        cameradirection = rotate_y(-a) @ np.array([0, 0, 1, 0])
    if keyboard.is_pressed('up arrow'):
        camerapos = camerapos - (10 * cameradirection)
        print(camerapos)
    if keyboard.is_pressed('down arrow'):
        camerapos = camerapos + (10 * cameradirection)
        print(camerapos)
    if keyboard.is_pressed('right arrow'):
        a += 0.01
        cameradirection = rotate_y(-a) @ np.array([0, 0, 1, 0])

    background = pg.display.set_mode((width, height))
    background.fill(color=white)

    draw_points(points,camerapos, cameradirection)
    pg.display.flip()


