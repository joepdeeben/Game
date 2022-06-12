import pygame as pg
import math
import numpy as np
import keyboard
from camera import *
from matrices import *
from object3d import *
from projection import *


width, height = 640, 1280
fov_v = np.pi/4
fov_h = fov_v * (width / height)
aspect = width/height
f = 100
n = 0.1


cube = []
for x in (-1, 1):
    for y in (-1, 1):
        for z in (-1, 1):
            cube.append(np.matrix([x, y, z, 1]))


for i in cube:
    print(i)


pg.init()
run = True
clock = pg.time.Clock()
surface = pg.surface.Surface((height, width))
camerapos = np.array([0, 0, 0, 1])


cameramatrix = np.matrix([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [-camerapos[0], -camerapos[1], -camerapos[2], 1]
    ])


scaler = 1
angle = 0
while run:
    clock.tick(60)



    if keyboard.is_pressed('up arrow'):
        camerapos[1] -= 1.1
    if keyboard.is_pressed('down arrow'):
        camerapos[1] += 1.1
    if keyboard.is_pressed('left arrow'):
        camerapos[0] -= 1.1
    if keyboard.is_pressed('right arrow'):
        camerapos[0] += 1.1
    if keyboard.is_pressed('w'):
        scaler += .1
    if keyboard.is_pressed('s'):
        scaler -= .1
    if keyboard.is_pressed('a'):
        scaler += .1
    if keyboard.is_pressed('d'):
        scaler -= .1
    print(camerapos[0])
    print(camerapos[1])
    display = pg.display.set_mode((height, width))
    display.fill((255, 255, 255))
    for i in cube:
       print(i)
       i = np.dot(i, translate((5, 6, -2)))
       i = i.reshape(4, 1)
       print(i)
       i = np.dot(cameramatrix, i)
       print(i)
       i = twod(i)
       i = i.reshape(1, 4)
       x = i[0,0] + (height/2)
       y = i[0,1] + (width/2)
       pg.draw.circle(display, (0, 0, 0), (x,y), radius=5)
    camerapos.reshape(1, 4)
    pg.display.flip()




