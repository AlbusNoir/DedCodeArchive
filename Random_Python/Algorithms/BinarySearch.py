# Binary Search
# Look for an item in a list by dividing the list in half each time


def binarysearch(myItem,myList):
    found = False
    bottom = 0
    top = len(myList) - 1
    while bottom <= top and not found:
        middle = (bottom+top) // 2  # Floor
        if myList[middle] == myItem:
            found = True
        elif myList[middle] < myItem:
            bottom = middle + 1
        else:
            # myList[middle] > myItem
            top = middle - 1
    return found



if __name__=="__main__":
    numberlist = [1,4,6,8,12,15,18,19,24,27,31,42,43,58]
    item= int(input("What number are you looking for? "))
    isFound = binarysearch(item,numberlist)

    if isFound:
        print("Your number is in the list")
    else:
        print("Your number is not in the list")
