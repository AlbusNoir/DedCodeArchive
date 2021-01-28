# generates perms based on what's passed in

import itertools
# uncomment to use static assign
# for p in itertools.permutations('ABCD'):
perm = input('Enter something to permutate: ')
for p in itertools.permutations(perm):
    print(p)
