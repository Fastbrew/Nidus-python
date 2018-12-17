"""
Function for moving unit.
"""

import numpy as np


def move_unit(old_pos, cardinal):

    if cardinal == 0:
        new_pos = old_pos - np.array([1, 0])

    elif cardinal == 1:
        new_pos = old_pos + np.array([0, 1])

    elif cardinal == 2:
        new_pos = old_pos + np.array([1, 0])

    elif cardinal == 3:
        new_pos = old_pos - np.array([0, 1])

    return new_pos

