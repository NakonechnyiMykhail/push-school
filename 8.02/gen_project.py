
import os, sys

def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: creating folder: ' + directory)

name = input('Enter the name of project: ')
create_folder(name)
# create_folder(name + '/css')
# create_folder(name + '/js')
# create_folder(name + '/img')
# create_folder(name + '/img2/test')
