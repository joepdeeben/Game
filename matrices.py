import numpy as np


def translate(x, y, z, input):
    t = np.array([
    [1, 0, 0, x],
    [0, 1, 0, y],
    [0, 0, 1, z],
    [0, 0, 0, 1]
])
    return np.dot(t, input)

def scale(scale, input):
    s = np.array([
    [1 * scale, 0, 0, 0],
    [0, 1 * scale, 0, 0],
    [0, 0, 1 * scale, 0],
    [0, 0, 0, 1]
])
    return np.dot(s, input)

display = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 1, 0, 1]
])