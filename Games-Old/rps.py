import random
import PySimpleGUI as sg

sg.theme('Topanga')
layout = [[sg.T(size=(15,1)), sg.T('PyRPS', size=(10,1))],
          [sg.B('Rock',size=(10,1),key='-ROCK-'), sg.VSep(), sg.B('Paper',size=(10,1),key='-PAPER-'), sg.VSep(),
           sg.B('Scissors',size=(10,1),key='-SCISSORS-')],
          [sg.HSep()],
          [sg.T(size=(20,1), key='-COMPUTER-')],
          [sg.T(size=(20,1), key='-WINNER-')],
          [sg.T(size=(12,1)), sg.Exit(key='-EXIT-', size=(10,1))],
         ]

window = sg.Window('RPS', layout)

computer = window['-COMPUTER-']
winner = window['-WINNER-']


def main(player):
    choices = ['rock', 'paper', 'scissors']

    beats = {'paper': 'scissors',
             'rock': 'paper',
             'scissors': 'rock'}

    player_choice = player


    computer_choice = random.choice(choices)
    computer.update(f'Computer: {computer_choice}')

    if player_choice == beats[computer_choice]:
        winner.update('Player wins!')
    elif computer_choice == beats[player_choice]:
        winner.update('Computer wins!')
    else:
        winner.update('Tie!')


while True:
    event, values = window.read()
    if event in ('-EXIT-', sg.WIN_CLOSED):
        break
    if event == '-ROCK-':
        main('rock')
    if event == '-PAPER-':
        main('paper')
    if event == '-SCISSORS-':
        main('scissors')
