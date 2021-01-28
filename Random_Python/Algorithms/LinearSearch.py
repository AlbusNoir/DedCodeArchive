# Linear Search Algorithm
# Looks for item in a list


def linearsearch (myItem, myList):
    found = False
    position = 0
    while position < len(myList) and not found:
        if myList[position] == myItem:
            found = True
        position = position +1
    return found

if __name__ == "__main__":
    shopping = ["apples","oranges","bananas","grapes"]
    item = input("What item are you looking for? ")
    isFound=linearsearch(item,shopping)

    if isFound:
        print("That item is in the list")
    else:
        print("That item is not in the list")
