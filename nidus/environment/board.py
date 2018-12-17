"""
Board (game state) object for Nidus.
"""

import numpy as np

from ..utils.distance import distance
from ..utils.legal_moves import legal_moves
from ..utils.move_unit import move_unit
from ..units import units


## Should be exposed via utils
def new_unit():

    unit = np.random.choice(units.UNITS)()

    return unit

class Board(object):
    def __init__(self, dims = (20, 20), players = 2, new_game = False):
        
        assert players in [2, 4]

        if players == 2:
            assert dims[1] % 2 == 0

        elif players == 4:
            assert dims[1] % 2 == 0
            assert dims[0] % 2 == 0

        self.dims = dims
        self.players = players
        self.player = 1
        
        if new_game:
            self.__new__()

        pass

    def iter_player(self):

        if self.player < self.players:
            self.player += 1
        else:
            self.player = 1

        return

    def __state__(self):
        return np.copy(self.state)

    def new_game(self):
        
        state = np.zeros(shape = self.dims)
        self.unit = 1

        self.stats = {}
        self.units = {}
        for player in range(1, self.players + 1):
            self.stats[player] = {'units': []}

        pos_x = (int(state.shape[1] / 2) - 1, int(state.shape[1] / 2))

        for pos in pos_x:

            state[0, pos] = self.unit

            self.stats[self.player]['units'].append(self.unit)
            self.units[self.unit] = new_unit()
            self.unit += 1

            self.iter_player()

            state[-1, pos] = self.unit
            
            self.stats[self.player]['units'].append(self.unit)
            self.units[self.unit] = new_unit()
            self.unit += 1

            self.iter_player()

            if self.players == 4:

                state = state.T

                state[0, pos] = self.unit
                
                self.stats[self.player]['units'].append(self.unit)
                self.units[self.unit] = new_unit()
                self.unit += 1

                self.iter_player()

                state[-1, pos] = self.unit
                
                self.stats[self.player]['units'].append(self.unit)
                self.units[self.unit] = new_unit()
                self.unit += 1

                self.iter_player()

                state = state.T

        self.state = state

        return

    def new_turn(self):

        probabilities = np.array([i.experience for i in self.units.values()])
        probabilities = np.exp(probabilities - probabilities.max()) / np.exp(probabilities - probabilities.max()).sum(axis = 0)

        order = np.random.choice(list(self.units.keys()),
                size = len(self.units),
                replace = False,
                p = probabilities)

        for unit in order:

            old_pos = np.argwhere(self.state == unit)[0]

            legal = legal_moves(old_pos, self.state)

            rand = np.random.uniform(size = (4,))

            movement = legal * rand
            cardinal = np.argwhere(movement == movement.max())[0]

            new_pos = move_unit(old_pos, cardinal)

            self.state[tuple(old_pos)] = 0
            self.state[tuple(new_pos)] = unit

        return
