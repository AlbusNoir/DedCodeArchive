'''fibonacci progression
    produces fib sequence
    0, 1, 1, 2, 3, 5, ...
'''
from numericprogression import Progression


class FibProgression(Progression):

    def __init__(self, first=0, second=1):
        '''new fib seq
        first - first term (def 0)
        second - second term (def 1)
        '''
        super().__init__(first)  # start at first
        self._prev = second - first  # fictituous value preceeding first

    def _advance(self):
        '''update curr val by summing prev 2'''
        self._prev, self._current = self._current, self._prev + self._current
