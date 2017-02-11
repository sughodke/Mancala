import random

from autoplayer import RandomAP
from board import Board

b = Board()

# game loop
player = [b.PLAYER_A, b.PLAYER_B][random.randint(0, 1)]
while not b.is_game_over():
    m = RandomAP.pick_move(player, b)
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
