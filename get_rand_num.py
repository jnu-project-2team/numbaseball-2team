import random
from is_available import *

def get_rand_num(length):
    error_code = 1

    correct_number = []
    while error_code != 0 :
        for _ in range(length):
            correct_number.append(str(random.randrange(0,10,1)))
        error_code = is_available(correct_number, length)

        return correct_number
