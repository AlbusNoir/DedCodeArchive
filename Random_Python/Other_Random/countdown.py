'''
    Simple countdown
'''
from time import sleep


''' grab input and pass'''
seconds = int(input('Enter the number of seconds you want to count down from: '))


def timer(seconds):
    '''carry input and then do something with it'''
    while seconds:
        min, sec = divmod(seconds, 60)  # mod to get min
        count = f'{min:2d}:{sec:2d}'  # placeholder for printing
        print(count, end='\r')  # print and clear
        sleep(1)
        seconds -= 1  # decrement

    input('Time up! Press any key to exit...')


timer(seconds)
