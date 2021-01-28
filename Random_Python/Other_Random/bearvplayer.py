'''
    Just a dumb little program that pits player v bear
    Entire thing just asks player to choose to do something, and depending on the choice the program responds appropriately
'''
import datetime as dt

def start():
    print('What is your name?')
    name = input('> ')

    print(f'''Hello {name}. Welcome to this random cave.
            You're not sure how you got here.
            We're not sure how you got here.
            All we know is that it's just you, and a bear.
            How would you like to proceed?
    ''')

    print('''
    1. Sneak up on the bear
    2. Throw something at the bear
    3. Sit and wait
    4. Leave the cave
    ''')

    choice = input('> ')
    things(choice)


def things(choice):
    '''pass choice in and do things'''
    hibernate = ['01', '02', '03', '04', '09', '10', '11', '12']  # months bears hibernate

    month = dt.datetime.now().strftime('%m')  # returns cur month like 02 03 etc
    month_proper = dt.datetime.now().strftime('%B')  # returns the month as name

    if choice == '1':           # sneak
        if month in hibernate:
            print(f'Oh, you are in luck. It is {month_proper}. The bear is sleeping. You manage to sneak up on it and punch it. Not sure why but good job?')
            dead('Dude you literally punched a bear. What did you expect to happen?')
        else:
            dead('Ouch. You attempt to sneak up on the bear. It is awake. It mauls you to death.')
    elif choice == '2':         # throw
        dead('You throw a rock at the bear. It charges at you and mauls you to death.')
    elif choice == '3':         # sit
        if month in hibernate:
            dead('You wait until you die of starvation. Congrats?')
        else:
            dead('The bear eventually notices you. It charges you and mauls you to death.')
    elif choice == '4':         # leave
        if month in hibernate:
            print('You leave the cave. You are no fun')
        else:
            dead('You trip over a rock. The bear hears you and charges you. It mauls you to death.')
    else:                     # plyr = dumb
        print('Okay. Really need you to read the choices. How about you try again?')
        start()


def dead(death):
    print('Congrats! You died!')
    print('Reason: ', death)
    input('Sorry. Try again next time')


'''initial call'''
start()
