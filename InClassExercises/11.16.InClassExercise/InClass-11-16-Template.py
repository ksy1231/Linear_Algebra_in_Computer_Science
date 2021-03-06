# Author: Kelvin Sung
# Inclass Exercise Starting Template
# Date: Nov 12, 2018
    
# Import the necessary libraries
import random
import traceback
    # https://docs.python.org/3/library/traceback.html

def read_data(fname):
    '''
    '''
    file = open(fname)
    for line in file:
        row = line.split(",")
        l = [float(row[v]) for v in range(2, len(row))]
        print("Row:", l)

def add_num(a, b):
    try:
        assert(a > 0 and b > 0)
    except AssertionError:
        print(f"!!ERROR!!: not both larger than zero")
        traceback.print_stack(None, 2)
        return 0
    return a + b

def test_random():
    l = list()
    for i in range(10):
        l.append(random.randrange(-8, 8))
    return l

print("A: Understanding seed and testing random")
print("   10 random numbers without seed call :", test_random())
random.seed(0)
print("   10 random numbers after seed(0) call: ", test_random())
random.seed(0)
print("   10 random numbers after seed(0) call: ", test_random())
print()

print("B: Understanding assert")
print("add_num(10, 20)", add_num(10, 20))
print("add_num(10, -20)", add_num(10, -20))
print()

print("C: Reading data file")
read_data("my.data")
