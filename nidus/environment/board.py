"""
Board (game state) object for Vein.
"""

import numpy as np

from ..utils.distance import distance
from ..utils.legal_moves import legal_moves
from ..units import units

print(units)


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
        for player in range(1, self.players + 1):
            self.stats[player] = {'units': {}}

        pos_x = (int(state.shape[1] / 2) - 1, int(state.shape[1] / 2))

        for pos in pos_x:

            state[0, pos] = self.unit

            self.stats[self.player]['units'][self.unit] = new_unit()
            self.unit += 1

            self.iter_player()

            state[-1, pos] = self.unit
            self.stats[self.player]['units'][self.unit] = new_unit()
            self.unit += 1

            self.iter_player()

            if self.players == 4:

                state = state.T

                state[0, pos] = self.unit
                self.stats[self.player]['units'][self.unit] = new_unit()
                self.unit += 1

                self.iter_player()

                state[-1, pos] = self.unit
                self.stats[self.player]['units'][self.unit] = new_unit()
                self.unit += 1

                self.iter_player()

                state = state.T

        self.state = state

        print(self.stats)

        return

    def new_turn(self):

        for player in self.stats:
            for unit in self.stats[player]['units']:
                pos = np.argwhere(self.state == unit)[0]
                legal = legal_moves(pos, self.state)

                print(unit)
                print(legal_moves(pos, self.state))
                print(pos)

        return
