'''
    Class for storing high scores in games
    Scoreboard
'''


class Scoreboard:
    '''fixed length sequence of high scores in nondecreasing order'''

    def __init__(self, capacity=10):
        '''initialize scoreboard w/ max capacity

        All entries are intially None
        '''
        self._board = [None] * capacity  # reserve space for future scores
        self._n = 0  # number of actual entries

    def __getitem__(self, k):
        '''return entry at index k'''
        return self._board[k]

    def __str__(self):
        '''return string representation of list'''
        return 'n'.join(str(self._board[j]) for j in range(self._n))

    def add(self, entry):
        '''consider adding entry to high scores'''
        score = entry.get_score()

        # Does it qualify for high score list?
        # yes if list not full or higher than last entry
        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):  # no score dropped
                self._n += 1  # overall num increases

        # shift lower scores rightward
        j = self._n - 1
        while j < 0 and self._board[j - 1].get_score() < score:
            self._board[j] = self._board[j - 1]  # shift entry from j-1 to j
            j -= 1  # decrement j
        self._board[j] = entry  # when done, add new entry

