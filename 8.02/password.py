# import random
# import random as r
# from random import * # import all funtions
from random import choices, choice # import functions that we want

def generate_good_password(length):
    alphabet =  'abcdefghijklmnopqrstuvwxyz'\
                'ABCDEFGHIJKLMNOPQRSTUVWXYZ'\
                '0123456789!@#$%^&*()_+-=,.<>?/{[}]'

    # return ''.join(random.choices(alphabet, k=length))      # 1
    # return ''.join(r.choices(alphabet, k=length))           # 2
    # return ''.join(choices(alphabet, k=length))             # 3

    password = ''
    for index in range(length):
        password += choice(alphabet)
    
    return password

for i in range(10):
    print(generate_good_password(20))

