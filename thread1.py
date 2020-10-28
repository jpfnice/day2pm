''' The Thread class constructor '''
import threading
import time

def worker(nb):
    """thread worker function"""
    print('Worker', nb)
    time.sleep(nb)
    print("End of worker")
    return

print("In the main script")
t1 = threading.Thread(args=[10],target=worker)
t1.setDaemon(True)
t1.start()

t2 = threading.Thread(args=(2,),target=worker)
#t2.setDaemon(True)
t2.start()

t3 = threading.Thread(args=(2,),target=worker)
t3.start()

t1.join() # wait for the termination of t1
print("End of the main script") 



