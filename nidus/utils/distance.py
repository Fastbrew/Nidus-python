"""
Distance metric used for attacking. (Manhattan distance)
"""

import numpy as np


def distance(a, b):
    return np.abs(a-b).sum(axis = 1)
