import random

from board import Board


class Move:

    def __init__(self, player, offset, board):
        self.player = player
        self.offset = offset
        self.board = board

        self.slot = self.cnt = 0
        self.bonus_turn = False

        self.compute_props()
        self.validate()

    def validate(self):
        if self.offset > 6 or self.offset < 0:
            raise Exception('Invalid slot! ' + str(self))

        if self.cnt == 0:
            raise Exception('No pieces in slot! ' + str(self))

    def compute_props(self):
        """Interestingly this function can sit here or in Board"""
        self.slot = self.board.retrieve_slot_for(player) + self.offset
        self.cnt = self.board[self.slot]

        if self.slot == self.board.retrieve_slot_for(self.board.opposite_player(player)):
            self.bonus_turn = True

    def __str__(self):
        return 'Player {} with offset {}'.format(self.player, self.offset)

b = Board()

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

    print(b)

print('Player {} won with {} to {}'.format(
    b.winning_player(), b.score_of(b.winning_player()),
    b.score_of(b.opposite_player(b.winning_player()))
))
