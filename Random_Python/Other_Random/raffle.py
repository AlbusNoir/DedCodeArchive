import random

tickets = []

loop = True

print('''Raffle Picker
Enter name, enter amount
Enter 'q' for the name to quit
''')

while loop:
    n = input('Name: ')

    if n != 'q':
        t = int(input('Amount: '))
        for i in range(t):
            tickets.append(n)
    else:
        loop = False


win = random.choice(tickets)

print(f'Winner is {win}')


while win in tickets:
    tickets.remove(win)

print(tickets)

input('Press any key to exit...')
