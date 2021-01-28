'''
    Binary search
    In a normal, unsorted list, searches occur in O(n) time, or sequetial time. Binary searches occur in O(logn) time, which is far more efficient. If n is a billion, logn is only 30.

    Basic forumla for binary search: mid = [low + high / 2]
    if the target equals data[mid], we found the item
    if target < data[mid] we recur and search the first half of the sequence, so entries from low to mid - 1
    if target > data[mid] we recur and search the second half of the sequence, so entries from mid + h to high
'''


def binary_search(data, target, low, high):
    '''Return True if target is found in indicated portion of list
    only data[low] and data[high] are considered inclusive'''
    if low > high:
        return False  # interval empty, no match
    else:
        mid = (low + high) // 2
        if target == data[mid]:  # found match
            return True
        elif target < data[mid]:
            # recur on left portion
            return binary_search(data, target, low, mid - 1)
        else:
            # recur on right portion
            return binary_search(data, target, mid + 1, high)
