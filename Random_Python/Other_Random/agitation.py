"""
    Agrivation
    Agitation
    Alliteration
    Loading
    Loading
    Loading
    Loading
    UGh
"""
import time
import sys


animation = '|/-\\'

a = int(input('Enter a number between 1 and 9999: '))

for i in range(a):
    time.sleep(0.1)
    sys.stdout.write('\r' + animation[i % len(animation)] + ' llllloading')
    sys.stdout.flush()

input('\nHope you enjoyed waiting!')
