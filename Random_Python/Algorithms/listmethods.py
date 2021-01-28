'''
    Mimic list things
    Append, remove, extending, constructing
'''
def insert(self, k, value):
    '''insert value at index k, shift subsequent values right'''
    # assume 0 <= k <= n
    if self._n == self._capacity:  # not enough room
        self._resize(2 * self._capacity)  # double size
    for j in range(self._n, k, -1):  # shift rightmost first
        self._A[j] = self._A[j - 1]
    self._A[k] = value  # store new element
    self._n += 1


def remove(self, value):
    '''remove first occurance of value or raise ValueError. Does not shrink dynamic array'''
    for k in range(self._n):
        if self._A[k] == value:  # match!
            for j in range(k, self._n - 1):  # shift others to fill gap
                self._A[j] = self._A[j + 1]
            self._A[self._n - 1] = None  # garbage collection
            self._n -= 1  # one less item
            return  # immediate exit
    raise ValueError('Value not found')  # did not find match


'''extending a list'''
for element in other:
    data.append(element)

'''constructing new lists'''
squares = []
for k in range(1, n + 1):
    squares.append(k * k)
