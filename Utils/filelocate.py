'''
    Locate file by given type in given dir
'''
import os


def locate_file():
    file_type = input('Enter the file type to find using .xyz format\n')
    get_dir = input('Enter the directory to search\n')

    find_file = os.listdir(get_dir)
    for file in find_file:
        if file.endswith(file_type):
            print(f'Listing files with {file_type}:')
            print(file)

    else:
        file_not_found(file_type, get_dir)

    repeat_locate()


def file_not_found(file_type, get_dir):
    print(f'Either no files found with {file_type} or all files found with {file_type} in {get_dir}')
    repeat_locate()


def repeat_locate():
    repeat = input('Find another file type? yN')
    if repeat.lower() == 'y':
        locate_file()
    elif repeat.lower() == 'n':
        exit()
    else:
        print(f'{repeat} is not valid.')
        repeat_locate()


locate_file()
