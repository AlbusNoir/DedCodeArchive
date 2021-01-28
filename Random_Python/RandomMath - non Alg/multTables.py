# displays multiplication tables from 1 to 12

for i in range(1,13):
    for j in range(1,13):
        print("{1} times {0} is {2}".format(i, j, i*j))
    print("========================")

input('press enter to exit')
