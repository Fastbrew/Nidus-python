"""
Board (game state) object for Nidus.
"""

import numpy as np

from ..utils.distance import distance
from ..utils.legal_moves import legal_moves
from ..utils.move_unit import move_unit
from ..units import units


## Should be exposed via utils
def new_unit(owner_id):

    unit = np.random.choice(units.UNITS)(owner_id)

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
            self.new_game()

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

        self.graveyard = []
        self.winner = None

        self.stats = {}
        self.units = {}
        for player in range(1, self.players + 1):
            self.stats[player] = {'units': []}

        pos_x = (int(state.shape[1] / 2) - 1, int(state.shape[1] / 2))

        for pos in pos_x:

            state[0, pos] = self.unit

            self.stats[self.player]['units'].append(self.unit)
            self.units[self.unit] = new_unit(self.player)
            self.unit += 1

            self.iter_player()

            state[-1, pos] = self.unit
            
            self.stats[self.player]['units'].append(self.unit)
            self.units[self.unit] = new_unit(self.player)
            self.unit += 1

            self.iter_player()

            if self.players == 4:

                state = state.T

                state[0, pos] = self.unit
                
                self.stats[self.player]['units'].append(self.unit)
                self.units[self.unit] = new_unit(self.player)
                self.unit += 1

                self.iter_player()

                state[-1, pos] = self.unit
                
                self.stats[self.player]['units'].append(self.unit)
                self.units[self.unit] = new_unit(self.player)
                self.unit += 1

                self.iter_player()

                state = state.T

        self.state = state

        return

    def _attack(self):

        for unit in self.units:

            pos = np.argwhere(self.state == unit)[0]
            locs = np.argwhere((self.state != unit) & (self.state != 0))
            dists = distance(pos, locs)

            others = locs[np.where(dists <= self.units[unit].range, True, False)]

            if len(others) > 0:

                units = [self.state[tuple(other)] for other in others if self.units[self.state[tuple(other)]].owner_id != self.units[unit].owner_id]

                for u in units:

                    self.units[u].take_damage(np.random.randint(1, self.units[unit].strength + 1))

        return

    def _move(self):

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

    def _status(self):

        for unit in self.units:

            if not self.units[unit].is_alive():

                pos = np.argwhere(self.state == unit)[0]
                self.state[tuple(pos)] = 0

                self.graveyard.append(unit)

        for dead in self.graveyard:
            self.units.pop(dead, None)

        if len(self.units) == 0:
            self.winner = 0
            return

        check = set([unit.owner_id for unit in self.units.values()])
        if len(check) == 1:
            self.winner = list(check)[0]

        return

    def new_turn(self):

        self._attack()
        self._status()
        self._move()

        return
