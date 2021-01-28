'''
    Exploring a list's size based on length
'''
import sys

data = []
n = 20  # change the value of n to adjust
for k in range(n):  # n must be fixed
    a = len(data)  # num elements
    b = sys.getsizeof(data)  # actual byte size
    print(f'Length: {a:3d}; Size in bytes: {b:4d}')
    data.append(None)  # increase length by one
