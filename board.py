class Board(list):
    """
       Player B
    +--+------+--+
    |7 |654321|  |
    |  |89abcd| 0|
    +--+------+--+
       Player A
    """
    PLAYER_A = 'A'
    PLAYER_B = 'B'
    SLOT_A = 8
    SLOT_B = 1
    SLOTS_PER_SIDE = 6

    def __init__(self):
        super().__init__(([0] + [4] * self.SLOTS_PER_SIDE) * 2)

    def avail_pieces(self):
        return sum(self.a_side()) + sum(self.b_side())

    def a_side(self):
        return self[self.SLOT_A:self.SLOT_A + self.SLOTS_PER_SIDE]

    def b_side(self):
        return self[self.SLOT_B:self.SLOT_B + self.SLOTS_PER_SIDE]

    def winning_player(self):
        return self.PLAYER_B if self.b_score > self.a_score else self.PLAYER_A

    def score_of(self, player):
        return getattr(self, '{}_score'.format(player.lower()))

    @property
    def a_score(self):
        return self[self.SLOT_B - 1]

    @property
    def b_score(self):
        return self[self.SLOT_A - 1]

    def __str__(self):
        a_side = ''.join(['{0: >2}'.format(val) for val in self.a_side()])
        b_side = ''.join(['{0: >2}'.format(val) for val in reversed(self.b_side())])
        return """
              Player B
        {sep}
        |{b_score: >2}|{b_side}|{whitesp: >2}|
        |{whitesp: >2}|{a_side}|{a_score: >2}|
        {sep} n={avail}
              Player A
        """.format(sep='+--+------------+--+', whitesp='  ',
                   a_score=self.a_score, b_score=self.b_score,
                   a_side=a_side, b_side=b_side, avail=self.avail_pieces())

    def _test(self):
        a_side = ''.join(['{0: >2}'.format(val) for val in range(self.SLOT_A,self.SLOT_A + self.SLOTS_PER_SIDE)])
        b_side = ''.join(['{0: >2}'.format(val) for val in reversed(range(self.SLOT_B, self.SLOT_B + self.SLOTS_PER_SIDE))])
        return """
              Player B
        {sep}
        |{b_score: >2}|{b_side}|{whitesp: >2}|
        |{whitesp: >2}|{a_side}|{a_score: >2}|
        {sep} n={avail}
              Player A
        """.format(sep='+--+------------+--+', whitesp='  ',
                   a_score=self.SLOT_B - 1, b_score=self.SLOT_A - 1,
                   a_side=a_side, b_side=b_side, avail=self.avail_pieces())

    def opposite_player(self, player):
        return self.PLAYER_A if player == self.PLAYER_B else self.PLAYER_B

    def make_move(self, move):
        i = move.slot
        cnt = move.cnt
        print('{} picked up all {} pieces from {} and moved them accordingly'
              .format(move.player, cnt, move.offset))
        self[i] = 0
        while cnt > 0:
            i = (i + 1) % len(self)

            if i + 1 == self.retrieve_slot_for(move.player):
                continue

            self[i] += 1
            cnt -= 1

        offset = i - self.retrieve_slot_for(move.player) + 1
        if offset in range(6) and self[i] == 1:
            i = (6 - offset) + self.retrieve_slot_for(self.opposite_player(move.player))
            self.increment_pot(self.opposite_player(move.player), self[i])
            print('Landed on an empty slot on our side, picked up all {} pieces from {} and moved them to my pot'
                  .format(self[i], offset))
            self[i] = 0

    def retrieve_slot_for(self, player):
        return getattr(self, 'SLOT_{}'.format(player))

    def is_game_over(self):
        if sum(self.a_side()) == 0 or sum(self.b_side()) == 0:
            return True
        else:
            return False

    def increment_pot(self, player, amt):
        self[self.retrieve_slot_for(player) - 1] += amt
