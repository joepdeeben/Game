import pygame as pg
import math
import numpy as np
import matrices
from object3d import *



height, width = 640, 1280
fov_v = np.pi/4
fov_h = fov_v * (width / height)


def run(self):
    pg.init()
    screen = pg.display.set_mode((height, width))
    run = True
    clock = pg.time.Clock()
    surface = pg.surface.Surface((height, width))


class renderer:
      def __init__(self):
          self.fps = 60


      def create_objects(self):
          self.object = object3d(self)

