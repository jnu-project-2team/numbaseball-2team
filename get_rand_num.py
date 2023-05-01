import random

def get_rand_num(length):

    correct_number = []
    
        for _ in range(length):
            correct_number.append(str(random.randrange(0,10,1)))
        
        print(correct_number)
        return correct_number
