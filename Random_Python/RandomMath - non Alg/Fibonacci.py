# Fibonacci sequence


def fib(f):
    # recursively print
    if f <= 1:
        return f
    else:
        return(fib(f - 1) + fib(f - 2))


def repeat():
    r = input('Run another sequence? yN: ')
    if r.lower() == 'y':
        fib_run()
    else:
        quit()  # lazy quit


def fib_run():
    f = int(input('Enter number for sequence: '))

    # check if the number of terms is valid
    if f <= 0:
        print("Can only Fibonacci positive numbers")
        repeat()
    else:
        print('Fibonacci sequence up to', f, ':')
        for i in range(f):
            print(fib(i))

        repeat()


fib_run()
