import random

def sample_method(num):
    r = random.randint(30, len(num)+1)
    sample_list = random.sample(num, r)
    return sample_list