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

    def make_move(self, player, offset):
        i = self.retrieve_slot_for(player) + offset
        cnt = self[i]
        print('{} picked up all {} pieces from {} and moved them accordingly'.format(player, cnt, offset))
        self[i] = 0
        while cnt > 0:
            i = (i + 1) % len(self)

            if i + 1 == self.retrieve_slot_for(player):
                continue

            # log('Incrementing {}'.format(i))
            self[i] += 1
            cnt -= 1

    def retrieve_slot_for(self, player):
        return getattr(self, 'SLOT_{}'.format(player))

    def is_game_over(self):
        if sum(self.a_side()) == 0:
            return self.PLAYER_A
        if sum(self.b_side()) == 0:
            return self.PLAYER_B
        else:
            return None
