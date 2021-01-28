'''geometric progression
    multiplies prev value by a base
    0, 2, 4, ...
'''
from numericprogression import Progression


class GeometricProgression(Progression):
    '''inherits progression'''

    def __init__(self, base=2, start=1):
        '''create new geo progression
        base - fixed constant to mult by (def 2)
        start - first term (def 1)
        '''
        super().__init__(start)
        self._base = base

    def _advance(self):
        '''overrides inherited
        updates curr val based on multple by base
        '''
        self._current += self._base
