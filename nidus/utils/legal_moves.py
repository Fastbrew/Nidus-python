"""
Legal moves from position.
"""

import numpy as np


def legal_moves(pos, state):

    legal = np.ones(shape = (4,))

    if pos[0] == 0:
        legal[0] = 0
    if pos[1] == (state.shape[1] - 1):
        legal[1] = 0
    if pos[0] == (state.shape[0] - 1):
        legal[2] = 0
    if pos[1] == 0:
        legal[3] = 0

    return legal
