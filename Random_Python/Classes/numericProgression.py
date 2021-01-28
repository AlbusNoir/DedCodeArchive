'''
    Creating class that increments whole nums
    0, 1, 2, ...
    This is generic progression
'''
class Progression:

    def __init__(self, start=0):
        '''initialize current to first val'''
        self._current = start

    def _advance(self):
        '''update self._current to new val

        Should be overridden by subclass to customize progression

        By convention, if current is set to None, this designates the end of finite progression
        '''
        self._current += 1

    def __next__(self):
        '''return next element, or raise StopIteration error'''
        if self._current is None:  # convention to end progression
            raise StopIteration()
        else:
            answer = self._current  # record current val to return
            self._advance()  # advance to prep for next time
            return answer  # return

    def __iter__(self):
        '''by convention, iterator must return itself'''
        return self

    def print_progression(self, n):
        '''print next n values of progression'''
        print(' '.join(str(next(self)) for j in range(n)))
