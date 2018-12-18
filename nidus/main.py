"""
Example of random Nidus game.
"""

from .environment.board import Board

import time


def main():

    b = Board(dims = (4, 4), players = 2)
    b.new_game()

    while b.winner is None:

        s = b.__state__()
        print(str(s))

        b.new_turn()

    s = b.__state__()
    print(str(s))

    print(b.winner)

    return
if __name__ == '__main__':
    main()
