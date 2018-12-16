"""
Example of random Nidus game.
"""

from .environment.board import Board


def main():

    b = Board(dims = (20, 20), players = 2)
    b.new_game()

    s = b.__state__()
    print(str(s))

    b.new_turn()

    return
if __name__ == '__main__':
    main()
