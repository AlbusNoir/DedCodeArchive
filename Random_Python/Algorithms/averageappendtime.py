'''
    computer the average list append time
'''
from time import time


def computer_average(n):
    '''perform n appends to empty list and return average time elapsed'''
    data = []
    start = time()  # record start in secs
    for k in range(n):
        data.append(None)
    end = time()  # record end time in secs
    return (end - start) / n  # comp avg
