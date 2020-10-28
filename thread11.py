'''
Synchronizing threads using Semaphore
Semaphore(), Lock()
'''
import logging

import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s (%(threadName)-2s) %(message)s',
                    )


class ActivePool(object):
    '''
    This class simply serves as a convenient way to 
    track which threads are able to run at a given moment. 
    Here it is just used to hold the names of the active threads 
    to show that only three are running concurrently.
    '''
    def __init__(self):
        super(ActivePool, self).__init__()
        self.active = []
        self.lock = threading.Lock()
    def makeActive(self, name):
        with self.lock:
            self.active.append(name)
            logging.debug('Running: %s', self.active)
    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)
            logging.debug('Running: %s', self.active)

def worker(s, pool):
    logging.debug('Waiting to join the pool')
    with s:
        name = threading.currentThread().getName()
        pool.makeActive(name)
        time.sleep(0.1)
        pool.makeInactive(name)

pool = ActivePool()
s = threading.Semaphore(3)
for i in range(7):
    t = threading.Thread(target=worker, name=str(i), args=(s, pool))
    t.start()
