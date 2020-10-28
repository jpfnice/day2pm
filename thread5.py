''' Sub-classing the Thread class '''
import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',)

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self) # or super().__init__()
        self.OkToRun=True
    def stop(self):
        self.OkToRun=False
    def worker(self):
        """thread worker function"""
        import random
        pause = random.randint(1,3)
        logging.debug('sleeping %s', pause)
        time.sleep(pause)
        logging.debug('ending')
        return
    def run(self):          # re-definition of run() (we "override" the run method)
        while self.OkToRun:
            self.worker()
            

t = MyThread()
t.start()

time.sleep(8)
t.stop()

print("The end")
