import pygame as pg
import numpy as np

import matrices
from matrices import *

pg.init()

width, height = 1280, 640
black = (0, 0, 0)
white = (255, 255, 255)
run = True


fps = pg.time.Clock()



points = []
for x in (-10, 10):
    for y in (-10, 10):
        for z in (-10, 10):
            points.append(np.matrix([x, y, z, 1]))

while run:
    fps.tick(60)
    background = pg.display.set_mode((width, height))
    background.fill(color=white)
    for i in points:
        i = i.reshape(4, 1)
        print(i)
        i = matrices.translate(500, 10, 0, i)
        print(i)
        i = np.dot(display, i)
        i = i.reshape(1, 4)
        x = i[0, 0] + width/2
        y = i[0, 1] + height/2
        pg.draw.circle(background, black, (x, y), radius=5)

    pg.display.flip()


