"""
    Loading bar
"""
import time


loading_bar = []


print('Please wait for something really cool...\n')


def load():
    dashes = 1
    spaces = 10
    for i in range(11):
        print('Loading[', end="")
        for x in range(dashes):
            dash = '|'
            loading_bar.append(dash)
            print(loading_bar[x], end="")
        for y in range(spaces):
            print(end=" ")
        time.sleep(1)
        dashes += 1
        spaces -= 1
        print(']')


load()

print('\nlittle longer...\n')
time.sleep(3)
print('almost there...\n')
time.sleep(3)
load()
time.sleep(5)
print('\nlol wow still waiting? Almost done...\n')
time.sleep(5)
load()
time.sleep(5)
print('\nReally surprised you waited. You satisfied? This is it. Seriously.\n')
time.sleep(5)
print('\nWait... Oh wrong result... uh hold on...\n')

load()

print('\nSorry about that. Almost done...\n')
time.sleep(10)
print('\nUuuh slight issue. Please wait a bit longer\n')
time.sleep(5)
print('\nHmmm... You uh really want this\n')
time.sleep(7)
print('\nOh okay yeah I fixed it hold on\n')
time.sleep(3)
load()
print('\nLittle more\n')
load()
print('\nAlmost\n')
time.sleep(5)
load()
print('\nAh fuck it. Fuck you. fuck this. Outtie 5000\n')
time.sleep(5)
load()
print('\n')
load()
print('\n\n\n\n\n\n\n')
input('\nKk Done :) ')