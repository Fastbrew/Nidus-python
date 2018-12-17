"""
Example of random Nidus game.
"""

from .environment.board import Board

import time


def main():

    b = Board(dims = (10, 10), players = 2)
    b.new_game()

    while True:

        s = b.__state__()
        print(str(s))

        time.sleep(1)

        b.new_turn()

    return
if __name__ == '__main__':
    main()
