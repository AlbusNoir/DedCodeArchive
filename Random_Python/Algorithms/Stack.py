# Stack

def useStack():
    stack = []
    choice = -1
    while choice !=4:
        print("1. Push on to stack")
        print()
        print("2. Pop from stack")
        print()
        print("3. Print stack")
        print()
        print("4. Exit")
        choice = int(input("Enter choice >>"))
        if choice == 1:
            nextItem = input("What do you want to add to the stack?")
            stack.append[nextItem]
        if choice ==2:
            # take from top
            print("The last in was",stack[-1])
            print("Deleting that one")
            del stack[-1]
        if choice == 3:
            for counter in range(len(stack)-1,1,-1):
                print(stack[counter])
