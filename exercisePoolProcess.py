import random
import multiprocessing
from functools import partial

dataset=[]
for i in range(10):
    dataset.append([])
    for j in range(10):
        dataset[i].append(random.randint(1,15))

def factorial(n):
    total=1
    for i in range(1,n+1):
        total *= i
    return total    

def computeFactorial(data, resultQueue):
    """
    Here, each process will compute 10 numbers.
    dataset is a list of list of 10 numbers
    data is an element of the list dataset
    """
    print(f"computeFactorial: {data}")
    for i in data:
        q.put((i,factorial(i)))

def main(numberOfProcesses,q):

    with multiprocessing.Pool(numberOfProcesses) as p:
        # map assign to each worker in turn an item of the list dataset
        # the second argument of computerFactorial always receives the same value: a reference to the Queue
        p.map(partial(computeFactorial, resultQueue=q), dataset)
           
    while not q.empty():
        print(q.get())

if __name__ == '__main__':
    
    numberOfProcesses=5
    m = multiprocessing.Manager()
    q = m.Queue()
    main(numberOfProcesses, q) 
