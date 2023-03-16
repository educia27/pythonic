import threading

event = threading.Event()

def myfunc():
    print("Waiting for event to trigger \n")
    event.wait()
    print("performing action")

t1 = threading.Thread(target=myfunc)

t1.start()

x = input("do you want to trigger the event? Yes/No \n")

if x == "Yes":
    event.set()
