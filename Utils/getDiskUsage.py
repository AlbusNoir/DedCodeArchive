'''
    Using os module to get disk usage
    Using recursion to get full usage of children dis too
'''
import os


path = input('Please specify the path you would like to display usage of: ')


def disk_usage(path):
    '''return num of bytes used by file/folder and descendents'''
    total = os.path.getsize(path)  # account for dir usage
    if os.path.isdir(path):  # if is dir
        for filename in os.listdir(path):  # for each child
            childpath = os.path.join(path, filename)  # compose full child path
            total += disk_usage(childpath)  # add to total usage

    print(f'{total:<10}:{path:<20}')
    return total

disk_usage(path)
