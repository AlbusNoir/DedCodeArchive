'''
    Solve tower of hanoi using recursive functions
'''

source = ([4, 3, 2, 1], 'A')
target = ([], 'B')
helper = ([], 'C')

print(source, target, helper)


def hanoi(n, source, helper, target):
    if n > 0:
        # move tower of size n - 1 to helper(C):
        hanoi(n - 1, source, target, helper)
        # move disk from source(A) peg to target(B) peg
        if source[0]:
            disk = source[0].pop()
            print('moving ' + str(disk) + ' from ' + source[1] + ' to ' + target[1])
            target[0].append(disk)
        # move tower of size n-1 from helper(C) to target(B)
        hanoi(n - 1, helper, source, target)



source = ([4, 3, 2, 1], 'A')
target = ([], 'B')
helper = ([], 'C')
hanoi(len(source[0]), source, helper, target)
print(source, target, helper)
