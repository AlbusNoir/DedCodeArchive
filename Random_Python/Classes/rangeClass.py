"""
    Uses overloading to create range class
"""

class Range:
    """ mimicing the built in range class"""

    def __init__(self, start, stop=None, step=1):
        """initialize range instance
            similar to built in class
        """
        if step == 0:
            raise ValueError('Step cannot be 0')

        if stop is None:  # special case of range(n)
            start, stop = 0, start  # range(0, n)

        # calculate effective length once
        self._length = max(0, (stop - start + step - 1) // step)

        # need start and step (not stop) to use __getitem__
        self._start = start
        self._step = step

    def __len__(self):
        """return num of entries in range"""
        return self._length

    def __getitem__(self, k):
        """return entry at index k"""
        if k < 0:
            k += len(self)  # attempt to convert negative index

        if not 0 <= k < self._length:
            raise IndexError('Index out of range')

        return self._start + k * self._step
