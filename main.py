import pygame as pg
import numpy as np
import keyboard
import matrices
from matrices import *

pg.init()

width, height = 1280, 640
black = (0, 0, 0)
white = (255, 255, 255)
run = True


fps = pg.time.Clock()



points = []
for x in (-100, 100):
    for y in (-100, 100):
        for z in (-100, 100):
            points.append(np.matrix([x, y, z, 1]))
x = 0
y = 0
z = 1

while run:
    fps.tick(60)
    background = pg.display.set_mode((width, height))
    background.fill(color=white)
    if keyboard.is_pressed('a'):
        x -= 20
    if keyboard.is_pressed('d'):
        x += 20
    if keyboard.is_pressed('w'):
        y -= 20
    if keyboard.is_pressed('s'):
        y += 20
    if keyboard.is_pressed('up arrow'):
        z += 0.1
    if keyboard.is_pressed('down arrow'):
        z -= 0.1
    for i in points:
        i = i.reshape(4, 1)
        print(i)
        i = matrices.translate(x, y, z, i)
        print(i)
        i = matrices.scale(z, i)
        print(i)
        i = np.dot(display, i)
        print(i)
        i = i.reshape(1, 4)
        print(i)
        xpos = i[0, 0] + width/2
        ypos = i[0, 1] + height/2
        print(xpos)
        print(ypos)
        pg.draw.circle(background, black, (xpos, ypos), radius=5)

    pg.display.flip()


