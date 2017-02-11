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