"""
Modify the following example in order to transform the script into:

 1) a multi-threaded script
    (for instance you could create 5 threads each of them in charge of computing 20 factorials)
 2) a multi-process script
    (for instance you could create 5 processes each of them in charge of computing 20 factorials)
    
You could then try to determine the most efficient version with the help of the module timeit

"""
import random
import threading
import queue
random.seed(1)   
 
dataset=[]
for i in range(100):
    dataset.append(random.randint(1,15))
    
def factorial(n):
    total=1
    for i in range(1,n+1):
        total *= i
    return total    


def computeFactorial(data, q):
    for i in data:
        q.put((i,factorial(i)))
            
def versionWithThreads():

    numberOfThreads=5
    
    q=queue.Queue()    
    threads = []
    for i in range(numberOfThreads):
        t=threading.Thread(target=computeFactorial, args=(dataset[i*20:(i+1)*20], q))
        t.start()
        threads.append(t)
        
    for t in threads:
        t.join()
        
#     while not q.empty():
#         print(q.get())


if __name__ == '__main__':       
    import timeit
    print(timeit.timeit("versionWithThreads()", setup="from __main__ import versionWithThreads", number=1000))
        


