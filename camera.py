import numpy as np

camerapos = [0, 0, 0, 1]
right = [1, 0, 0, 1]
up = [0, 1, 0, 1]
forward = [0, 0, 1, 1]


def translate_matrix(cpos):
    x, y, z, w = cpos
    return np.array([
        [1, 0, 0, -x],
        [0, 1, 0, -y],
        [0, 0, 1, -z],
        [0, 0, 0, 1]
    ])


def rotate_matrix(right, forward, up):
    rx, ry, rz, w = right
    fx, fy, fz, w = forward
    ux, uy, uz, w = up
    return np.array([
        [rx, ux, fx, 0],
        [ry, uy, fy, 0],
        [rz, uz, fz, 0],
        [0, 0, 0, 1]
    ])


def camera_matrix(self):
    return self.translate_matrix() @ self.rotate_matrix()