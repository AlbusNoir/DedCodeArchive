'''
    from Python crash course
    rolling a die in plotly
'''
from random import randint


class Die:
    '''class for representing a die'''

    def __init__(self, num_sides=6):
        '''assume 6 sided die'''
        self.num_sides = num_sides

    def roll(self):
        '''return a random value between 1 and num_sides'''
        return randint(1, self.num_sides)
