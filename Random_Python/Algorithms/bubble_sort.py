"""
    Bubble Sort algorithm
    ask user for list
    pass in a list and sort in order
"""
import time


def sort(listy):
    print(listy)
    for i in range(len(listy)):
        for j in range(i + 1, len(listy)):
            if listy[j] < listy[i]:
                listy[j], listy[i] = listy[i], listy[j]  # this swaps them
                print(listy)
                time.sleep(1)  # suspend 1 sec
    repeat()


def repeat():
    r = input('Would you like to sort another list? yN: ')
    if r.lower() == 'y':
        setList()
    else:  # lazy quit
        quit()


def setList():
    # define num of elements passing
    n = int(input('How many elements will you be adding? '))
    # define list and map input var
    listy = list(map(int, input('Enter elements, seperated by a space.\nPress enter when done:\n').strip().split()))[:n]

    sort(listy)


setList()
