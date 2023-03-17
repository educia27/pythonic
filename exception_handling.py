try: 
    x = int(input("first number: "))
    y = int(input("second number: "))
    print(x/y)
except ValueError:
    print("please enter a valid number ")

except ZeroDivisionError:
    print("Cannot divide by 0")
    y=1
    print(x/y)
finally:
    print("DONE!")


def func():
    if True:
        raise ValueError("something went wrong")

print(func())

x = 10
y = 20

assert(x < y)