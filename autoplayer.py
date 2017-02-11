import random
from move import Move


class AutoPlayer:
    pass


class RandomAP(AutoPlayer):
    @classmethod
    def pick_move(cls, player, b):
        # return Move(player, random.randint(0, 5), b)
        m = None
        while True:
            try:
                m = Move(player, random.randint(0, 5), b)
                break
            except Exception:
                pass
        return m
