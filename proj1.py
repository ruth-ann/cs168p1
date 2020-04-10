import random
import numpy as np

def simulate_1(n):
    print(n)
    print(np.random.randint(1,int(n), size=30))

#def simulate_2(n):

#def simulate_3(n):

#def simulate_4(n):


if __name__ == '__main__':
    n = input("Number of bins:")
    simulate_1(n)
    # print simulate2(n)
    # print simulate3(n)
    # print simulate4(n)