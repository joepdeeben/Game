import numpy as np
import matrices
import math

height, width = 640, 1280
fov_v = np.pi/4
fov_h = fov_v * (width / height)
aspect = width/height
f = 100
n = 0.1

def Project(obj):
    projectionm = np.matrix([
        [(1/(aspect * (math.tan((fov_v/2))))), 0, 0, 0],
        [0, 1/(math.tan((fov_v/2))), 0, 0],
        [0, 0, -((f+n) / (f-n)), -1],
        [0, 0, -((2*f*n)/(f-n)), 0]
    ])
    return np.dot(projectionm, obj)