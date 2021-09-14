# %matplotlib inline

# !/bin/env python

import matplotlib.pyplot as plt
import logging
import numpy as np
import py21cmfast as p21c

cosmo_params = p21c.CosmoParams()

print('Hello World')


def Gaussian(x, sigma=1, mu=0):
    return (1 / sigma / np.sqrt(2 * np.pi)) * (np.exp(-0.5 * (((x - mu) / sigma) ** 2)))


def distance_from_coordinate(box_length):
    index = np.arange(-0.5 * (box_length - 1), 0.5 * (box_length + 1))

    x_mesh, y_mesh, z_mesh = np.meshgrid(index, index, index, indexing='ij')

    distance = np.sqrt((x_mesh) ** 2 + (y_mesh) ** 2 + (z_mesh) ** 2)

    return distance


def random_voxel(box_length):
    np.random.seed()  # set seed to a randome number
    #     np.random.seed(4) ; np.random.rand(10)

    coordinate = np.random.randint(0, box_length, size=3)

    return coordinate
