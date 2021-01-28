"""
  Fibonacci Rewrite because Kevin's was instant
  Removing recursion to produce instant output
  Author: KBSego

  Side note: I win
"""

# testing useage to quickly see result
# f = 20


def run():
    # uncomment to take input from the user
    f = int(input("Enter number for sequence: "))

    # first two terms
    n1 = 0
    n2 = 1
    count = 0

    # check if the number of terms is valid
    if f <= 0:
        print("Please enter a positive integer")
    elif f == 1:
        print("Fibonacci sequence up to", f, ":")
        print(n1)
    else:
        print("Fibonacci sequence up to", f, ":")
        while count < f:
            print(n1, end='\n')
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1

    repeat()


def repeat():
    r = input('Run another sequence? yN: ')
    if r.lower() == 'y':
        run()
    else:
        quit()  # lazy quit


run()
