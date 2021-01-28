"""
    utilize overloading to iterate
"""


class SequenceIterator:
    """an iterator for any Python sequence type"""

    def __init__(self, sequence):
        """create iterator for given sequence"""
        self._seq = sequence  # keep ref of underlying data
        self._k = -1  # will increment to 0 on first call to next function

    def __next__(self):
        """return next element or raise StopIteration error"""
        self._k += 1  # here is where it iterates to 0
        if self._k < len(self._seq):
            return(self._seq[self._k])  # return data element
        else:
            raise StopIteration()  # there are no more elements

    def __iter__(self):
        """returns self as an iterator. This is convention"""
        return self
