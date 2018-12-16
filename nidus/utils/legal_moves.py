"""
Legal moves from position.
"""

import numpy as np


def legal_moves(pos, state):

    legal = np.ones(shape = (4,))

    zeros = np.argwhere(state == 0)

    if (pos[0] == 0) | (~np.equal(zeros, pos - np.array([1, 0])).all(1).any()):
        legal[0] = 0
    if (pos[1] == (state.shape[1] - 1)) | (~np.equal(zeros, pos + np.array([0, 1])).all(1).any()):
        legal[1] = 0
    if (pos[0] == (state.shape[0] - 1)) | (~np.equal(zeros, pos + np.array([1, 0])).all(1).any()):
        legal[2] = 0
    if (pos[1] == 0) | (~np.equal(zeros, pos - np.array([0, 1])).all(1).any()):
        legal[3] = 0

    return legal
