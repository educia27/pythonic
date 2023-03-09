x = [True, True, False, True]

print(any(x))

print(all(x))

numbers  = [11,22,33,44,55,66,77,88,99]

even = lambda x: x % 2 == 0

result = [even(number) for number in numbers]

print(result)

if any(result):
    print("one or more numbers are even")
else:
    print("no # is even")


if all(result):
    print("All numbers are even")
