import multiprocessing
import threading
import time
import random

def epicstyle():
    # wait = random.randint(1, 20)
    # time.sleep(wait)
    # print('owned libtards epic style by waiting ' + str(wait))
    total = 0
    for i in range(1000000):
        total += random.randint(1, 1337)
    #print('Done.  Total is ' + str(total))

if __name__ == '__main__':

    thread_count = multiprocessing.cpu_count()

    # Vanilla bean
    t0 = time.time()
    for i in range(thread_count):
        epicstyle()
    t1 = time.time()
    print("Total computation time is " + str(t1-t0))

    # Fake news threads
    threads = []
    t0 = time.time()
    for i in range(thread_count):
        x = threading.Thread(target=epicstyle)
        threads.append(x)
        x.start()
    for thread in threads:
        thread.join()
    t1 = time.time()
    print("Total threading computation time is " + str(t1-t0))

    # Multiprocessing
    processes = []
    t0 = time.time()
    for i in range(thread_count):
        x = multiprocessing.Process(target=epicstyle)
        processes.append(x)
        x.start()
    for proc in processes:
        proc.join()
    t1 = time.time()
    print("Total process computation time is " + str(t1-t0))