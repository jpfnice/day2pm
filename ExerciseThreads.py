"""
Modify the following example in order to transform the script into:

 1) a multi-threaded script
    (for instance you could create 5 threads each of them in charge of computing 20 factorials)
 2) a multi-process script
    (for instance you could create 5 processes each of them in charge of computing 20 factorials)
    
You could then try to determine the most efficient version with the help of the module timeit
"""

import random
random.seed(1) # To ensure we generate the same pseudo-random numbers at each run

dataset=[]
for i in range(100):
    dataset.append(random.randint(1,15))
    
def factorial(n):
    total=1
    for i in range(1,n+1):
        total *= i
    return total    

def computation():
    return [(e,factorial(e)) for e in dataset] # list comprehension

# import timeit
# print(timeit.timeit("computation()", setup="from __main__ import computation", number=10000))

print("The result:", computation())