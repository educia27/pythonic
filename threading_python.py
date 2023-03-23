import threading
import time

def function1():
    for x in range(100):
        print("one")
        
def function2():
    for x in range(100):
        print("two")
        
def hello():
    for x in range(50):
        print("Hello")

t1 = threading.Thread(target=function1)

t2 = threading.Thread(target=function2)


t3 = threading.Thread(target=hello)

t3.start()

t3.join()

print("some text")

