'''
    Progression by arithmetic
    Like multiples
    0, 4, 8, ...
'''
from numericprogression import Progression


class ArithmeticProgression(Progression):
    '''inherits progression'''

    def __init__(self, increment=1, start=0):
        '''create new arithmetic progression

        increment - fixed constant to add each term. def 1
        start - first term. def 0
        '''
        super().__init__(start)  # initialize base class progression
        self._increment = increment

    def _advance(self):
        '''update current by adding fixed increment
        overrides inherited version
        '''
        self._current += self._increment
