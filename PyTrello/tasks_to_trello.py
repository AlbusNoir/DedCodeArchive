# driver for trello automation
import os
from PyTrello import create_board, create_list, create_card

'''
Process flow:
Enter name of board
Enter name of list
Enter name of card
Magic
Poof
'''

username = '{your_username}'

# board creation
name_board = input('Enter a name for the board: ')
board_id = create_board(f"{name_board}")

# list creation
stop = False

while not stop:
    name_list = input('Enter a name for a list or q to quit: ')
    if name_list != 'q':
        with open(f'{name_list}.txt', 'w+') as file:
            card_stop = False
            while not card_stop:
                name_card = input(f'Enter a name for a card in {name_list} or q to quit: ')
                if name_card != 'q':
                    file.write(name_card + '\n')
                else:
                    card_stop = True
    else:
        stop = True

for filename in os.listdir():
    if filename.endswith('.txt'):
        filename = os.path.splitext(filename)[0]
        make_list = create_list(board_id, filename.title())
        with open(f'{filename}.txt', 'r') as list_file:
            for card in list_file.readlines():
                if card != '':
                    create_card(make_list, card)
                else:
                    break

print(f'''
Board/Lists/Cards created.
You can find your board here: https://trello.com/{username}/boards
''')

# TODO: gui?
