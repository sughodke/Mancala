import copy
import random
from move import Move


class AutoPlayer:
    pass


class RandomAP(AutoPlayer):
    @classmethod
    def pick_move(cls, player, b):
        while True:
            try:
                m = Move(player, random.randint(0, 5), b)
                break
            except Exception:
                pass
        return m


class MaxAP(AutoPlayer):
    @classmethod
    def pick_move(cls, player, b):
        possible_moves = []
        for i in range(0, 6):
            try:
                m = Move(player, i, b)
                possible_moves.append(m)
            except Exception:
                pass

        prospective_boards = []  # [copy.copy(b)] * len(possible_moves)
        for move in possible_moves:
            prospective_board = copy.copy(b)
            prospective_board.make_move(move)
            prospective_boards.append(prospective_board)

        score_prospectives = [cls.score_board(board, player) for board in prospective_boards]
        winning_move = score_prospectives.index(max(score_prospectives))

        return possible_moves[winning_move]

    @classmethod
    def score_board(cls, board, player):
        return board.score_of(player)


class AdversarialAP(MaxAP):
    @classmethod
    def score_board(cls, board, player):
        my_side = getattr(board, '{}_side'.format(player.lower()))
        their_side = getattr(board, '{}_side'.format(board.opposite_player(player).lower()))
        return (sum(my_side()) - sum(their_side())) + \
            1.1 * (board.score_of(player) - board.score_of(board.opposite_player(player)))


class MinMaxAP(MaxAP):
    @classmethod
    def pick_move(cls, player, b):
        return super().pick_move(b.opposite_player(player), b)
