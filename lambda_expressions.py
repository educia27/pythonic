import dis

mysquare = lambda x: x * x 

print(mysquare(5))

mysum = lambda x,y: x + y

print(mysum(4,5))

titled_elegance = lambda first, last: f'First name is {first.title()} and last name is {last.title()}'
print(type(titled_elegance))
print(dis.dis(titled_elegance))
print(titled_elegance("Uhtred", "Ragnarson"))


other_sum = lambda *args: sum(args)

print(other_sum(3,4,5))


# this is known as an immediately invoked functino expression IIFE ie iffy , direct wih print statement
print("we are lit: ",(lambda x: x * x)(2))


numbers = [8,34,566,76,12,3,9, 77,40]


def filterfunction(x):
    return x % 2 == 0


even = list(filter(lambda x: x % 2 == 0, numbers))

squared_numbers = list(map(lambda y: y*y, numbers))

print("these are the squared numbers ", squared_numbers)


def myfunc(num):
    return lambda x: x * num

ten_multiplier = myfunc(10)

print(ten_multiplier(10))


