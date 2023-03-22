import threading 

import time

x = 8192

lock = threading.Lock()


def double():
    global x, lock
    lock.acquire()
    while x < 16384:
        x *= 2
        print(x)
        time.sleep(1)
    print("reached the max!")
    lock.release()

def halve():
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)
    print("reached the minimum")
    lock.release()
        
d1 = threading.Thread(target=halve)
d2 = threading.Thread(target=double)

d1.start()
d2.start()