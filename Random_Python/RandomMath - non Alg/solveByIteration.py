"""
    This is a higher level maths concept
    Iterations are used to solve equations otherwise not really solveable
    You start with xsub0 and iterate using the prior answer to eventually get close enough to a suitable solution
    An iteration can "converge" (get closer) or "diverge" (get worse) -> the GOAL is to converge

    Iterations are hella useful for solving stuff like cubic equations

    formula example: X(subn+1)=(2+1)/X(subn)

    it's a bunch of substitutions really

    Yeah, okay, whatever, start the program...
"""
import time
import math


def iterate():
    print('This is just an example/proof of concept: Solving: X' + chr(0x00B2) + '-x-5=0 by iteration')
    a = int(input('Enter the initial value of X' + chr(0x2080) + ': '))  # this is xsub0

    # using list to hold xsub values
    subs = [0x2080, 0x2081, 0x2082,
            0x2083, 0x2084, 0x2085,
            0x2086, 0x2087, 0x2088, 0x2089
            ]

    string = ''

    for i in range(0, 10):
        string = 'X' + chr(subs[i]) + '=' + str(a)
        a = math.pow(6 + a, 0.5)
        print(string)
        time.sleep(1)  # time before doing next print


iterate()

input('Press enter to quit')
