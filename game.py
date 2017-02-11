import random

from board import Board
from move import Move

b = Board()

# game loop
player = [b.PLAYER_A, b.PLAYER_B][random.randint(0, 1)]
while not b.is_game_over():
    while True:
        try:
            m = Move(player, random.randint(0, 5), b)
            break
        except Exception:
            pass

    b.make_move(m)

    if not m.bonus_turn:
        player = b.opposite_player(player)
    else:
        print('Player {} got an extra turn!'.format(player))

    print(b)

print('Player {} won with {} to {}'.format(
    b.winning_player(), b.score_of(b.winning_player()),
    b.score_of(b.opposite_player(b.winning_player()))
))
