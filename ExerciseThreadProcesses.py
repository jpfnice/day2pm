import random
import multiprocessing
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

def main():
    
    numberOfProcesses=5
    q=multiprocessing.Queue()
     
    procs=[]  
    for i in range(numberOfProcesses):
        t=multiprocessing.Process(target=computeFactorial, args=(dataset[i*20:(i+1)*20], q))
        t.start()
        procs.append(t)
        
    for t in procs:
        t.join()
    
#         
#     while not q.empty():
#         print(q.get())
        
# if __name__ == '__main__': 
#     main()   
if __name__ == '__main__':       
    import timeit
    print(timeit.timeit("main()", setup="from __main__ import main", number=10))
  
 
 