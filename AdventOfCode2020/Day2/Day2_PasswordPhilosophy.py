'''
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password.
The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid.
For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid.
The middle password, cdefg, is not; it contains no instances of b, but needs at least 1.
The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?
'''
passwords = []

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        stripped = line.rstrip('\n')
        passwords.append(stripped)

good_pws = 0

# for loop that separates out the info we need to do the things
for pw in passwords:
    password = pw[pw.index(': ')+2:]
    policy = pw[:pw.index(':')]
    pol_min = int(policy[:policy.index('-')])
    pol_max = int(policy[policy.index('-')+1:policy.index(' ')])
    check_letter = policy[policy.index(' ')+1:policy.index(' ')+2]
    letters = {}
    for ltr in password:
        if ltr in letters:
            letters[ltr] += 1
        else:
            letters[ltr] = 1
    if check_letter in letters:
        if pol_min <= letters[check_letter] <= pol_max:
            good_pws += 1

print('Part1')
print(f'Total num of valid passwords, per policy: {good_pws}')


'''PT2
The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! 
The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. 
(Be careful; Toboggan Corporate Policies have no concept of "index zero"!) 
Exactly one of these positions must contain the given letter. 
Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according to the new interpretation of the policies?'''

# using same input.txt file as above
good_pws = 0

# this part is same mostly, just checking for placement of letters instead of a min max
for pw in passwords:
    password = pw[pw.index(': ')+2:]
    policy = pw[:pw.index(':')]
    first_let = int(policy[:policy.index('-')])
    second_let = int(policy[policy.index('-')+1:policy.index(' ')])
    check_letter = policy[policy.index(' ')+1:policy.index(' ')+2]

    if password[first_let-1] == check_letter:
        if password[second_let-1] != check_letter:
            good_pws += 1
    elif password[second_let-1] == check_letter:
        if password[first_let-1] != check_letter:
            good_pws += 1

print('Part2')
print(f'Total num of valid passwords, per policy: {good_pws}')