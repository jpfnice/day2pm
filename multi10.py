'''
Creation of a Process via sub-classing
'''
import multiprocessing

class Worker(multiprocessing.Process):

    def run(self):
        print(f'In {self.name}')
        return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = Worker()
        jobs.append(p)
        p.start()
    # The following is not mandatory
    for j in jobs:
        j.join()